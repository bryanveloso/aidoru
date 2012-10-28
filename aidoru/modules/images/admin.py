# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from django import forms
from django.contrib import admin
from django.db.models import get_model

import selectable.forms as selectable

from modules.images.models import Image, Tag
from modules.images.lookups import IdolLookup, TagLookup


class ImageAdminForm(forms.ModelForm):
    class Meta(object):
        model = Image
        widgets = {
            'idols': selectable.AutoCompleteSelectMultipleWidget(lookup_class=IdolLookup),
            'tags': selectable.AutoCompleteSelectMultipleWidget(lookup_class=TagLookup)
        }


class ImageAdmin(admin.ModelAdmin):
    form = ImageAdminForm


admin.site.register(Image, ImageAdmin)
admin.site.register(Tag)
