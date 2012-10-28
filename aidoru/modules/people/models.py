# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from django.db import models


class Idol(models.Model):
    name = models.CharField(editable=False, max_length=255)
    slug = models.SlugField()

    def __unicode__(self):
        return u'%s' % (self.name)
