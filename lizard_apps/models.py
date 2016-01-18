# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans, see LICENSE.rst.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.db import models


class Application(models.Model):
    """An application in the sense of Google Apps.

    Well, `application` is perhaps a bit bombastic. It's just a bookmark
    that will be used to switch between our and third-party websites.

    Icon will be uploaded to MEDIA_ROOT/lizard_apps.

    """
    url = models.URLField()
    icon = models.ImageField(upload_to='lizard_apps/')
    name = models.CharField(
        db_index=True,
        help_text='Descriptive text for labeling the icon',
        max_length=64,
    )

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Screen(models.Model):
    """A collection of applications.

    """
    slug = models.SlugField(max_length=64, unique=True)
    applications = models.ManyToManyField(
        Application,
        related_name='screens',
        through='ApplicationScreen'
    )

    class Meta:
        ordering = ['slug']

    def __unicode__(self):
        return self.slug


class ApplicationScreen(models.Model):
    """Intermediary model for ordering applications on a screen.

    If no order if provided, ordering will be alphabetically.

    """
    screen = models.ForeignKey(Screen)
    application = models.ForeignKey(Application)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['screen', 'order', 'application__name']
        unique_together = ('screen', 'application')

    def __unicode__(self):
        return self.application.url
