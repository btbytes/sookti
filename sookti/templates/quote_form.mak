<%inherit  file="base.mak" />
<h2>Quote editor</h2>
${c.form.start(name="form", action=h.url_for(action='edit'), method="POST") }
${c.form.layout.simple_start()}

${c.form.layout.entry(
    c.form.field.text_area('content'),
    name='Quote',
    error=c.form.get_error('content')
)}

${c.form.layout.entry(
    c.form.field.text('who'),
    name='Who',
    error=c.form.get_error('who')
)}

${c.form.layout.entry(
    c.form.field.text('tags'),
    name='Tags',
    error=c.form.get_error('tags')
)}

${c.form.layout.entry(
    c.form.field.submit('submit', value="Submit")
)}

${c.form.layout.simple_end()}
${ c.form.end() }