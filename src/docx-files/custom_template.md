$if(tables)$
$for(tables)$
:::{custom-table}
$table$
:::
$endfor$
$endif$

$if(images)$
$for(images)$
:::{custom-image}
![Image]($src$)($alt$){width=50%}
:::
$endfor$
$endif$
