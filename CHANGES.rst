Changelog of lizard-apps
========================

0.2.11 (unreleased)
-------------------

- Nothing changed yet.


0.2.10 (2024-04-09)
-------------------

- Fixed RemovedInDjango40Warning: django.conf.urls.url() is deprecated in favor
  of django.urls.re_path()

- Fixed image preview in Django Admin.


0.2.9 (2023-08-18)
------------------

- Fix RemovedInDjango40Warning: django.conf.urls.url() is deprecated in favor
  of django.urls.re_path()


0.2.8 (2023-07-06)
------------------

- Fix bug in JS version of the view.


0.2.7 (2023-07-06)
------------------

- Added a JSON version of the view.


0.2.6 (2020-03-06)
------------------

- Fixed code compatibility with Django 2.2.


0.2.5 (2020-03-06)
------------------

- Changed __unicode__ of models into __str__.

- Fixed ordering in template view.

- Fixed performance of template view (fetch everything in a single query).


0.2.4 (2020-01-24)
------------------

- Added support for dumping and loading of fixtures by natural key(s).


0.2.3 (2020-01-23)
------------------

- Get rid of template literals (backticks), because this ECMAScript 6 feature
  is not widely supported yet.


v0.2.1 (2016-03-10)
-------------------

- Update version in setup.py.


v0.2 (2016-03-10)
-----------------

- Fix style.css to be less `lizard`-y

- Match instructions on usage with reality.

- Return 404 instead of incorrect JS file when screen does not exist.

- Only allow alphanumeric-dash-underscore in screens slug URL.


v0.1.2 (2016-02-16)
-------------------

- Update version in setup.py.

v0.1.1 (2016-02-16)
-------------------

- Added migrations to manifest.


v0.1 (2016-02-16)
-----------------

- Added icon used in the html snippet in the js script as svg

- Style is stolen from the lizard interface

- Readme adjusted to support the new structure

- The plugin now expects 2 dom elements present
