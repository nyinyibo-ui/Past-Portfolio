select ls.name set_name, year, pt.name parent_theme_name,ls.theme_name,is_licensed
from lego_sets ls
inner join parent_themes pt
On ls.parent_theme=pt.name
where pt.name ='Star Wars';




