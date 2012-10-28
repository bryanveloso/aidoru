from selectable.base import ModelLookup
from selectable.registry import registry

from modules.images.models import Tag


class TagLookup(ModelLookup):
    model = Tag
    search_fields = ('name__icontains',)

registry.register(TagLookup)
