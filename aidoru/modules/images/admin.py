# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from django.contrib import admin

from modules.images.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ['token', 'linked_url', 'attributed_idols', 'attributed_tags']
    list_filter = ['idols']

    raw_id_fields = ('idols',)
    autocomplete_lookup_fields = {'m2m': ['idols']}

    def attributed_idols(self, obj):
        return ', '.join([i.name for i in obj.idols.all()])
    attributed_idols.short_description = 'idols'

    def attributed_tags(self, obj):
        return ', '.join([t.name for t in obj.tags.all()])
    attributed_tags.short_description = 'tags'

    def linked_url(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (obj.url, obj.url)
    linked_url.allow_tags = True
    linked_url.short_description = 'URL'
admin.site.register(Image, ImageAdmin)
