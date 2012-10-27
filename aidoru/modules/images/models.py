# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from django.db import models

from model_utils.models import TimeStampedModel


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name


class Image(TimeStampedModel):
    # Identification.
    token = models.CharField(max_length=6)
    url = models.URLField(verify_exists=True)

    # Categorization.
    tags = models.ManyToManyField(Tag)
    idols = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.url
