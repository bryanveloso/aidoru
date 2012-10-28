# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

import random

from django.db import models
from django.db.models import Count

from model_utils.models import TimeStampedModel
from modules.people.models import Idol


class ImageManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = random.randint(0, count - 1)
        return self.all()[random_index]


class Image(TimeStampedModel):
    # Identification.
    token = models.CharField(editable=False, max_length=6)
    url = models.URLField('URL', verify_exists=True)

    # Categorization.
    tags = models.ManyToManyField('Tag')
    idols = models.ManyToManyField(Idol)

    # Managers
    objects = ImageManager()

    def __unicode__(self):
        return u'%s' % self.token

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        self.token = self.create_token()
        self.save()

    def create_token(self):
        from multiprocessing.dummy import list
        ALPHABET = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

        i = self.id
        if i == 0:
            return ALPHABET[0]
        s = ''
        base = len(ALPHABET)
        while i > 0:
            s += ALPHABET[i % base]
            i /= base
        return s[::-1]


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name
