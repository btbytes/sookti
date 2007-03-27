<%inherit  file="quotes_list.mak" />

<%def name="list_footer()" >
% if c.paginator.current.previous:
${ h.link_to('previous', url=h.url(action='tag', id=c.tag, page=c.paginator.current.previous))}
% endif
% if c.paginator.current.previous and c.paginator.current.next:
|
% endif
% if c.paginator.current.next:
${ h.link_to('next', url=h.url(action='tag', id=c.tag, page=c.paginator.current.next))}
% endif 
</%def>
