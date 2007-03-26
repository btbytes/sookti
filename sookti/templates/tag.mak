<%inherit  file="base.mak" />
<h2>Quotes tagged with ${c.tag} </h2>
<ul>
% for quote in c.quotes:
  <li>${quote}</li>
% endfor
</ul>