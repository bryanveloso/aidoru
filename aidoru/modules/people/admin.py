# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from django.contrib import admin

from modules.people.models import Idol


admin.site.register(Idol)
