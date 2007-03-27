<%inherit  file="../base.mak" />
<h2>Register</h2>

${c.form.start(name="form", action=h.url_for(action='register'), method="POST") }
${c.form.layout.simple_start()}

${c.form.layout.entry(
    c.form.field.text('username'),
    name='User Name',
    error=c.form.get_error('username')
)}

${c.form.layout.entry(
    c.form.field.text('email'),
    name='Email',
    error=c.form.get_error('email')
)}

${c.form.layout.entry(
    c.form.field.password('password1'),
    name='Password',
    error=c.form.get_error('password1')
)}

${c.form.layout.entry(
    c.form.field.password('password2'),
    name='Retype Password',
    error=c.form.get_error('password2')
)}

${c.form.layout.entry(
    c.form.field.check_box('tos'),
    name='Terms of Service',
    error=c.form.get_error('tos')
)}

${c.form.layout.entry(
    c.form.field.submit('submit', value="Submit")
)}

${c.form.layout.simple_end()}
${ c.form.end() }