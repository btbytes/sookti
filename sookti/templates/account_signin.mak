<h1>Sign In</h1>
% remote_user = request.environ.get('REMOTE_USER')
% if remote_user:
<p>
You are signed in as <% remote_user %>.
</p>
%else:
%    if c.message:
<h2>Message:</h2>
<p>
%{c.message}
</p>
%    else:
<h2>Enter your username and password</h2>
${ h.start_form(h.url_for(controller="account", action="signin_check"), method="post") }
  username: ${ h.text_field("username", value="admin") }
  <br/>
  password: ${ h.text_field("password", value="pylons") }
  <br/>
  <input type="submit" value="signin">
${ h.end_form() }
% endif 
% endif