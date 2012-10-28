# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from django import forms
from django.contrib import admin

import selectable.forms as selectable

from modules.images.models import Image
from modules.images.lookups import IdolLookup


class ImageAdminForm(forms.ModelForm):
    class Meta(object):
        model = Image
        widgets = {
            'idols': selectable.AutoCompleteSelectMultipleWidget(lookup_class=IdolLookup),
        }


class ImageAdmin(admin.ModelAdmin):
    form = ImageAdminForm


admin.site.register(Image, ImageAdmin)
