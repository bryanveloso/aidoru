from selectable.base import ModelLookup
from selectable.registry import registry

from modules.people.models import Idol


class IdolLookup(ModelLookup):
    model = Idol
    search_fields = ('name__icontains',)
registry.register(IdolLookup)
