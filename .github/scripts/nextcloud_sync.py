#!/usr/bin/env python3
"""
Script to sync content from Nextcloud to the local repository
"""

import os
import hashlib
import json
import shutil
import sys
from pathlib import Path
from datetime import datetime

try:
    import requests
    import owncloud
except ImportError:
    print("Required packages not installed. Install with: pip install requests pyocclient")
    sys.exit(1)

# Configuration from environment variables
NEXTCLOUD_URL = os.environ.get("NEXTCLOUD_URL")
NEXTCLOUD_USERNAME = os.environ.get("NEXTCLOUD_USERNAME")
NEXTCLOUD_PASSWORD = os.environ.get("NEXTCLOUD_PASSWORD")
NEXTCLOUD_CONTENT_PATH = os.environ.get("NEXTCLOUD_CONTENT_PATH", "/content")
LOCAL_CONTENT_PATH = "content"  # Relative to repository root

# Ensure environment variables are set
if not all([NEXTCLOUD_URL, NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD]):
    print("Error: Missing required environment variables.")
    print("Please set NEXTCLOUD_URL, NEXTCLOUD_USERNAME, and NEXTCLOUD_PASSWORD.")
    sys.exit(1)

def setup_nextcloud_client():
    """Initialize and return a Nextcloud client."""
    client = owncloud.Client(NEXTCLOUD_URL)
    try:
        client.login(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD)
        print(f"Successfully connected to Nextcloud at {NEXTCLOUD_URL}")
        return client
    except Exception as e:
        print(f"Error connecting to Nextcloud: {e}")
        sys.exit(1)

def list_files_recursively(client, remote_path):
    """List all files in the remote path recursively."""
    all_files = []
    
    try:
        contents = client.list(remote_path)
        for item in contents:
            if item.is_dir():
                # Recursively list files in subdirectory
                all_files.extend(list_files_recursively(client, item.path))
            else:
                all_files.append(item)
    except Exception as e:
        print(f"Error listing files at {remote_path}: {e}")
    
    return all_files

def calculate_file_hash(file_path):
    """Calculate MD5 hash of a file."""
    if not os.path.exists(file_path):
        return None
    
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_relative_path(full_path, base_path):
    """Get the path relative to base_path."""
    return full_path.replace(base_path, '').lstrip('/')

def sync_content():
    """Sync content from Nextcloud to local repository."""
    client = setup_nextcloud_client()
    
    # Get list of all remote files
    remote_files = list_files_recursively(client, NEXTCLOUD_CONTENT_PATH)
    
    # Create a manifest of synced files
    manifest = {
        "last_sync": datetime.now().isoformat(),
        "files": []
    }
    
    # Track remote file paths to detect deletions
    remote_file_paths = set()
    
    # Ensure local content directory exists
    os.makedirs(LOCAL_CONTENT_PATH, exist_ok=True)
    
    # Track files to be updated
    updated_files = []
    
    # Process each remote file
    for remote_file in remote_files:
        relative_path = get_relative_path(remote_file.path, NEXTCLOUD_CONTENT_PATH)
        local_file_path = os.path.join(LOCAL_CONTENT_PATH, relative_path)
        
        # Add to remote file paths set
        remote_file_paths.add(relative_path)
        
        # Ensure local directory exists
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        
        # Check if file needs updating
        remote_mtime = remote_file.attributes.get('{DAV:}getlastmodified')
        remote_size = remote_file.attributes.get('{DAV:}getcontentlength')
        
        update_needed = True
        if os.path.exists(local_file_path):
            local_hash = calculate_file_hash(local_file_path)
            
            # Download file to temporary location to check hash
            temp_path = f"{local_file_path}.temp"
            client.get_file(remote_file.path, temp_path)
            remote_hash = calculate_file_hash(temp_path)
            
            if local_hash == remote_hash:
                update_needed = False
                os.remove(temp_path)  # Clean up temp file
            else:
                shutil.move(temp_path, local_file_path)
                updated_files.append(relative_path)
        else:
            # New file
            client.get_file(remote_file.path, local_file_path)
            updated_files.append(relative_path)
        
        # Add to manifest
        manifest["files"].append({
            "path": relative_path,
            "updated": update_needed,
            "size": remote_size,
            "last_modified": remote_mtime
        })
    
    # Check for deleted files
    local_files = []
    for root, _, files in os.walk(LOCAL_CONTENT_PATH):
        for file in files:
            # Skip the manifest file
            if file == '.sync-manifest.json':
                continue
                
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, LOCAL_CONTENT_PATH)
            
            # Convert Windows paths if needed
            relative_path = relative_path.replace('\\', '/')
            
            # If file exists locally but not in remote, delete it
            if relative_path not in remote_file_paths:
                print(f"Deleting file: {relative_path}")
                os.remove(local_path)
                updated_files.append(f"DELETED: {relative_path}")
    
    # Write manifest file
    with open(os.path.join(LOCAL_CONTENT_PATH, '.sync-manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    
    # Print summary
    print(f"Sync completed. {len(updated_files)} files updated.")
    for file in updated_files:
        print(f"  - {file}")

if __name__ == "__main__":
    sync_content()