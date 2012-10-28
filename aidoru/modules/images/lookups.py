from selectable.base import ModelLookup
from selectable.registry import registry

from modules.images.models import Tag
from modules.people.models import Idol


class IdolLookup(ModelLookup):
    model = Idol
    search_fields = ('name__icontains',)
registry.register(IdolLookup)


class TagLookup(ModelLookup):
    model = Tag
    search_fields = ('name__icontains',)
registry.register(TagLookup)
