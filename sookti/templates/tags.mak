<%inherit  file="base.mak" />
<ul>
% for tag in c.tags:
<li>${ h.link_to(tag.name, url=h.url(action='tag', id=tag.name)) }</li>  
% endfor
</ul>
