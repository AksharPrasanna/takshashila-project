# Takshashila Institution Website

Deployment Details
- Website URL: https://aksharprasanna.github.io/takshashila-project/
- Digital Oean Deployment URL: http://159.89.162.204/

This repository contains the source code for the Takshashila Institution website, built using [Quarto](https://quarto.org/).

## Project Overview

The Takshashila Institution is an independent center for research and education in public policy. This website showcases the institution's research, publications, team members, and various initiatives.

## Folder Structure

```
takshashila-project/
├── _fonts.scss                  # Font declarations
├── _quarto.yml                  # Quarto configuration
├── _variables.scss              # SCSS variables
├── _variables.yml               # YAML variables
├── assets/                      # Static assets (images, etc.)
├── components/                  # Reusable page components
├── configs/                     # Configuration files
├── content/                     # Main content files
│   ├── blogs/                   # Blog posts
│   ├── books/                   # Books information
│   ├── news/                    # News articles
│   ├── podcasts/                # Podcast episodes
│   ├── programs/                # Program information
│   └── publications/            # Publication documents
├── includes/                    # HTML/EJS includes & templates
│   ├── analysis-card.ejs        # Template for analysis cards
│   ├── content-card-carousel.ejs # Carousel template
│   ├── footer.html              # Site footer
│   ├── listing-card.ejs         # Template for listing cards
│   ├── news-card.ejs            # Template for news cards
│   ├── podcast-card.ejs         # Template for podcast cards
│   ├── social-icons.html        # Social media icons
│   └── title-block.html         # Page title block
├── index.qmd                    # Homepage
├── pages/                       # Static pages
│   ├── about.qmd                # About page
│   ├── mission.qmd              # Mission page
│   ├── research_areas/          # Research areas pages
│   └── team_takshashila.qmd     # Team page
├── styles/                      # Styling
│   ├── common/                  # Common styles
│   ├── components/              # Component-specific styles
│   └── sections/                # Section-specific styles
├── takshashila.scss             # Main SCSS file
└── utility/                     # Utility scripts
    ├── script.js                # General JavaScript utilities
    └── sidenote.js              # Sidenote functionality
```

## Key Components

### Content Structure

- **Publications**: Research papers and analysis documents
- **Blogs**: Regular blog posts on various topics
- **Team Members**: Information about the Takshashila team
- **Research Areas**: Different research domains of the institution
- **Events & Media**: News, podcasts, and media appearances

### Style Components

The site uses a systematic approach to styling with:

- **Main Colors**: 
  - Primary: `#610d3d` (burgundy)
  - Secondary: `#ffeef8` (light pink)
  - Accent: `#f2a321` (gold)

- **Responsive Design**: Uses modern CSS techniques including:
  - CSS Grid for layouts
  - Flexbox for component alignment
  - Media queries for different device sizes
  - CSS variables for consistent theming
  - Clamp() function for responsive typography and spacing

### Templates

The site uses several EJS templates for dynamic content:

- `listing-card.ejs`: Generic content cards
- `content-card-carousel.ejs`: Carousel displays for content
- `news-card.ejs`: News article displays
- `podcast-card.ejs`: Podcast episode displays

## Development Setup

### Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) (latest version)
- [Node.js](https://nodejs.org/) (for running scripts)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/aksharprasanna/takshashila-project.git
   cd takshashila-project
   ```

2. Preview the website:
   ```
   quarto preview
   ```

3. Build the website:
   ```
   quarto render
   ```

### Creating Content

#### Adding a Blog Post

Create a new `.qmd` file in the `content/blogs/` directory:

```yaml
---
title:
date:
description:
categories: 
  - "Category1"
  - "Category2"

listing:
  - id: authors
    contents: ../../pages/team/*.qmd
    type: grid
    sort-ui: false
    filter-ui: false
    categories: false
    template: ../../includes/listing-card.ejs
    include:
      title:
        - "Author1"
        - "Author2"

format:
  html:
    toc: true
    toc-depth: 2
    toc-expand: true
    toc-location: left
---

Your blog content goes here...
```

#### Adding a Publication

Create a new `.qmd` file in the `content/publications/` directory:

```yaml
---
title:
date:
description:
categories: 
  - "Category1"
  - "Category2"

listing:
  - id: authors
    contents: ../../pages/team/*.qmd
    type: grid
    sort-ui: false
    filter-ui: false
    categories: false
    template: ../../includes/listing-card.ejs
    include:
      title:
        - "Author1"
        - "Author2"

format:
  html:
    toc: true
    toc-depth: 2
    toc-expand: true
    toc-location: left
---

::: {#overview-section}

::: {#executive-summary}
## Executive Summary
...
:::

## Authors
::: {#authors}
:::

:::

Rest of the Publication Content goes here ...
```

#### Adding Footnotes

Footnotes without reference numbers:
```
[Footnote Content]{.aside}
```

Footnotes with reference numbers:
```
^[Footnote Content]
```

## Deployment

The site is configured to be deployed automatically through GitHub Pages. The generated site is available at: https://aksharprasanna.github.io/takshashila-project/

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

Copyright © 2024 The Takshashila Institution. All rights reserved.
