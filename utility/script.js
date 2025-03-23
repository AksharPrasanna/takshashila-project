document.addEventListener("DOMContentLoaded", function () {
    const titleBlock = document.getElementById("title-block-header");
    const contentBlock = document.getElementById("quarto-content");

    if (titleBlock && contentBlock) {
        contentBlock.parentNode.insertBefore(titleBlock, contentBlock);
    }
});
