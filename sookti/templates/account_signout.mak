<%inherit  file="base.mak" />
<p>
${c.message}
</p>

<p>
${h.link_to('sign in', url=h.url(controller='account', action='signin'))}.
</p>
