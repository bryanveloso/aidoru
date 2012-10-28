# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

import random

from django.db import models
from django.db.models import Count, signals
from django.dispatch import receiver

from model_utils.models import TimeStampedModel
from modules.people.models import Idol
from taggit.managers import TaggableManager


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
    tags = TaggableManager()
    idols = models.ManyToManyField(Idol)

    # Managers
    objects = ImageManager()

    def __unicode__(self):
        return u'%s' % self.token


@receiver(signals.post_save, sender=Image)
def create_token(instance, created, *args, **kwargs):
    from multiprocessing.dummy import list
    ALPHABET = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    if created:
        i = instance.id
        if i == 0:
            return ALPHABET[0]
        s = ''
        base = len(ALPHABET)
        while i > 0:
            s += ALPHABET[i % base]
            i /= base
        instance.token = s[::-1]
        instance.save()
