# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

import random

from django.db import models
from django.db.models import Count

from model_utils.models import TimeStampedModel


class ImageManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = random.randint(0, count - 1)
        return self.all()[random_index]


class Image(TimeStampedModel):
    # Identification.
    token = models.CharField(max_length=6)
    url = models.URLField(verify_exists=True)

    # Categorization.
    tags = models.ManyToManyField('Tag')
    idols = models.TextField(blank=True)

    # Managers
    objects = ImageManager()

    def __unicode__(self):
        return u'%s' % self.url


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name
