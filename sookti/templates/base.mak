<html>
<head>
<title>
Sookti: Quotes Page
</title>
<link href="/quotes.css" type="text/css" rel="stylesheet" />
<% h.javascript_include_tag('/javascripts/effects.js', builtins=True)  %>
</head>

<body>
<div id="container">
<h1>Sookti - the Quote Server</h1>
<div id="quote">
${ next.body()}
<div id="cfooter">
<% remote_user = request.environ.get('REMOTE_USER') %>

<p>
<span style="text-align:left">

</span>
% if remote_user:
(${remote_user}) 
% endif
${h.link_to('Home', url=h.url(controller='quote', action='index'))} 
% if remote_user:
| ${h.link_to('list', url=h.url(controller='quote', action='list', id=''))} |
${h.link_to('random', url=h.url(controller='quote', action='random', id=''))}|
${h.link_to('add new', url=h.url(controller='quote', action='edit', id=''))}|
${h.link_to('sign out', url=h.url(controller='account', action='signout', id=''))}.
% endif


</p>
</div>
</div><!-- quote -->
</div><!-- container -->
</body>
</html>