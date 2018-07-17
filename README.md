# Description

On  the  website  of  the  kazakhstan  stock  exchange  (KASE)  was  created  an  application  for  television  show  as  a  part  of  the  promotion  of  IT  products.  Users  can  see  episodes  of  television  show "Фондовый Рынок - Статус  PRO"  on  the  pages  of  that  application.  More  details  about  television  show  you  can  find  on  official  website  of  ["Atameken  Business  Channel"](https://abctv.kz/).

# Features  of  implementation

As  part  of  the  Django’s  common  web  application  tools,  Django  offers  a  few  classes  to  manage  paginated  data.  In  this  project  we  use  paginate  using  class-based  views  (ListView).  As  you  know  pagination  is  an  essential  part  of  platforms  where  one  needs  to  list  many  items.  Instead  of  displaying  all  the  times,  say  50,000  records,  pagination  allows  the  user  to  browse  through  the  entire  collection  in  steps,  only  seeing  a  part  of  the  entire  collection.

![](https://github.com/NogerbekNurzhan/StatusPro/blob/master/static/images/1.jpg)

I  was  faced  with  two  issues:

1. Pagination  widget  became  unwieldy  when  number  of  pages  are  large.
2. When  user  navigate  to  the  pages  by  pagination  widget  he/she  can  see  incorrect  url  address.

Custom  template  tags  and  filters  were  used  to  solve  the  above  problems.

**pagination.py:**

```
from django import template


register = template.Library()


@register.filter(name='pagination')
def pagination(paginator, current_page, neighbors=10):
    if paginator.num_pages > 2 * neighbors:
        start_index = max(1, current_page - neighbors)
        end_index = min(paginator.num_pages, current_page + neighbors)
        if end_index < start_index + 2 * neighbors:
            end_index = start_index + 2 * neighbors
        elif start_index > end_index - 2 * neighbors:
            start_index = end_index - 2 * neighbors
        if start_index < 1:
            end_index -= start_index
            start_index = 1
        elif end_index > paginator.num_pages:
            start_index -= (end_index - paginator.num_pages)
            end_index = paginator.num_pages
        page_list = [f for f in range(start_index, end_index + 1)]
        return page_list[:(2 * neighbors + 1)]
    return paginator.page_range
```

**pagination_url.py:**
```
from django import template
import re


register = template.Library()


@register.filter(name='pagination_url')
def pagination_url(path, page_number):
    output = re.search('(page=\d+)', path)
    if output is not None:
        print(str(output.group(1)))
        return path.replace(str(output.group(1)), "page={page_number}")
    if re.search('(page=\d+)', path):
        path.replace()
    page_number = str(page_number)
    if '?' in path:
        return path + "&page=" + page_number
    return path + "?page=" + page_number
```

Example of page about an episode of the television show:

![](https://github.com/NogerbekNurzhan/StatusPro/blob/master/static/images/2.png)
