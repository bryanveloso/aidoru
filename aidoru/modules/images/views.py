import random

from django.views.generic import DetailView, View

from braces.views import JSONResponseMixin
from modules.images.models import Image


class RandomImageChoiceView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        self.object = Image.objects.random()

        json_dict = {
            'token': self.object.token,
            'url': self.object.url,
        }
        return self.render_json_response(json_dict)


class CountTheImagesView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        json_dict = {'count': Image.objects.count()}
        return self.render_json_response(json_dict)
