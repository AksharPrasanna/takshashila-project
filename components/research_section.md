---
params:
  config: "configs/featured_research.yml"
---

## Research Papers
::: {.grid}
::: {.g-col-12 .g-col-md-8}
::: {.card .featured}
![{{ featured.title }}]({{ featured.image }}){.card-img-top}

### [{{ featured.title }}]({{ featured.link }})

**Category:** {{ featured.category }}  
**Date:** {{ featured.date }}  

{{ featured.summary }}

[Read More]({{ featured.link }}){.btn .btn-primary}
:::
:::

::: {.g-col-12 .g-col-md-4}
{{# articles }}
::: {.card}
![{{ title }}]({{ image }}){.card-img-top}

### [{{ title }}]({{ link }})

**Category:** {{ category }}  
**Date:** {{ date }}  

{{ summary }}

[Read More]({{ link }}){.btn .btn-primary}
:::
{{/ articles }}
:::
:::
