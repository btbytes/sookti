<%inherit  file="base.mak" />
% for quote in c.quotes:  
  ${print_quote(quote)}
% endfor


<%def name="print_quote(quote)">
  <blockquote>
  <p class="quote">${quote.content}</p>
  </blockquote>
  <p class="who">${quote.who}</p>
  <p class="qct">
  % if remote_user:
    ${ h.link_to('edit', url=h.url(action='edit', id=quote.id)) }|
    ${ h.link_to("delete", url=h.url(action='delete', id=quote.id), confirm="Are you sure?") }.
  % endif
  </p> 
  <hr/>  
</%def>