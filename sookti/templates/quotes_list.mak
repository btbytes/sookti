<%inherit  file="base.mak" />

% for quote in c.quotes:  
  ${print_quote(quote)}
% endfor

${self.list_footer()}


<%def name="list_footer()" >
  <!-- list footer Eg: pagination etc... -->
</%def>

<%def name="print_quote(quote)">
  <blockquote>
  <p class="quote">${quote.content}</p>
  </blockquote>
  <p class="who">${quote.who}</p>
  <p class="tags">
%  for tag in quote.tags:
   ${ h.link_to(tag, url=h.url(action='tag', id=tag)) }, 
%  endfor
  </p>
  <p class="qct">
<% remote_user = request.environ.get('REMOTE_USER') %>

% if remote_user:
    ${ h.link_to('edit', url=h.url(action='edit', id=quote.id)) }|
    ${ h.link_to("delete", url=h.url(action='delete', id=quote.id), confirm="Are you sure?") }.
% endif
  </p> 
  <hr/>  
</%def>