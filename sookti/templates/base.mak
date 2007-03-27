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
<div id="quote">
<h1>Q Server</h1>
<div id="cfooter">
<% remote_user = request.environ.get('REMOTE_USER') %>

<p>
<span style="text-align:left">

</span>
% if remote_user:
(${remote_user}) 
% endif
${h.link_to('Home', url=h.url(controller='quote', action='index',id=''))}|
${h.link_to('random', url=h.url(controller='quote', action='random', id=''))}|
${h.link_to('list', url=h.url(controller='quote', action='page', id=''))} |

% if remote_user:
${h.link_to('add new', url=h.url(controller='quote', action='edit', id=''))}|
${h.link_to('sign out', url=h.url(controller='account', action='signout',
id=''))}.
% else:
${h.link_to('sign in', url=h.url(controller='account', action='signin',
id=''))}.
% endif
</p>
</div>

% if c.flash:
 <p class="portal_message">  ${c.flash} </p>
% endif
% if c.message:
 <p>  ${c.message} </p>
% endif

${ next.body()}
</div><!-- quote -->
</div><!-- container -->
</body>
</html>