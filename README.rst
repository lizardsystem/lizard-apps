lizard-apps
===========

Lizard-apps is a simple, Google-apps like Django app for switching between web applications built on top of the `lizard-nxt <https://github.com/nens/lizard-nxt>`_ back end. An example of such an application is `lizard-client <https://github.com/nens/lizard-client>`_. A recognizable but contrived example:

.. figure:: lizard-apps.png
   :align: center

Quick start
-----------

1. Add "lizard_apps" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'lizard_apps',
    ]

2. Include the lizard_apps URLconf in your project urls.py like this::

    url(r'^lizard_apps/', include('lizard_apps.urls')),

3. Add 'django.template.context_processors.media' in the 'context_processors' option of TEMPLATES, so {{ MEDIA_URL }} can be used in the `script.js <lizard_apps/templates/lizard_apps/script.js>`_ template.