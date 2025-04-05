document.addEventListener("DOMContentLoaded", function () {
    const titleBlock = document.getElementById("quarto-margin-sidebar");
    const contentBlock = document.getElementById("sidenote");

    if (titleBlock && contentBlock) {
        titleBlock.append(contentBlock);
    }
});
