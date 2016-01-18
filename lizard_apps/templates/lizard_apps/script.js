{% comment %}

- Our reverse proxy must be configured to pass the original host header in X-Forwarded-Host.
- Django must be configured to use the X-Forwarded-Host header in preference to the Host header: USE_X_FORWARDED_HOST = True.
- MEDIA_URL must end in a slash if set to a non-empty value as per docs; assumed is that it also starts with one.
- Add 'django.template.context_processors.media' in the 'context_processors' option of TEMPLATES.

{% endcomment %}

var e = document.getElementById('lizard-apps-container');

e.innerHTML = `

<svg viewBox="0, 0, 30, 30" style="background-color: black;">
  <rect x="8" y="0" width="3" height="100%" style="fill: white;"/>
  <rect x="19" y="0" width="3" height="100%" style="fill:white;"/>
  <rect x="0" y="8" width="100%" height="3" style="fill:white;"/>
  <rect x="0" y="19" width="100%" height="3" style="fill:white;"/>
</svg>

<div id="lizard-apps" class="lizard-apps-off">
{% for app in view.screen.applications.all %}
  <div class="lizard-apps-icon">
    <div>
      <a href="{{ app.url }}"><img src="//{{ request.get_host }}{{ MEDIA_URL }}{{ app.icon }}"></img></a>
    </div>
    {{ app.name }}
  </div>
{% endfor %}
</div>

`;

e.onclick = function() {
  var e = document.getElementById('lizard-apps');
  e.className = e.className === 'lizard-apps-off' ? 'lizard-apps-on' : 'lizard-apps-off';
};
