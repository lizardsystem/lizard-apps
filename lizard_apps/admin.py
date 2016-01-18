# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans, see LICENSE.rst.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import admin

from lizard_apps import models


def get_image_tag(app):
    if app.icon:
        return '<img src="{}{}" />'.format(settings.MEDIA_URL, app.icon)
    else:
        return '-'


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return get_image_tag(obj)

    image_tag.allow_tags = True
    image_tag.short_description = 'Preview'


class ApplicationScreenInline(admin.TabularInline):
    model = models.ApplicationScreen
    readonly_fields = ['image_tag']
    verbose_name = 'Application'
    verbose_name_plural = 'Applications'
    extra = 1

    def image_tag(self, obj):
        return get_image_tag(obj.application)

    image_tag.allow_tags = True
    image_tag.short_description = 'Preview'


class ScreenAdmin(admin.ModelAdmin):
    inlines = [ApplicationScreenInline]


admin.site.register(models.Application, ApplicationAdmin)
admin.site.register(models.Screen, ScreenAdmin)
