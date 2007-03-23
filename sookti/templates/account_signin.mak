<%inherit  file="base.mak" />
<h2>Sign In</h2>
<% remote_user = request.environ.get('REMOTE_USER') %>  

% if remote_user:
<p> You are signed in as <em> ${ remote_user }</em>
</p>
%else:
%    if c.message:
<h2>Message:</h2>
<p>
${c.message}
</p>
%    else:
<h3>Enter your username and password</h3>
${ h.start_form(h.url_for(controller="account", action="signin_check"), method="post") }
  username: ${ h.text_field("username", value="admin") }
  <br/>
  password: ${ h.password_field("password", value="pylons") }
  <br/>
  <input type="submit" value="signin">
${ h.end_form() }
% endif 
% endif