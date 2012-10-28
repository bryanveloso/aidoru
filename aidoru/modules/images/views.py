import random

from django.views.generic import DetailView, View

from braces.views import JSONResponseMixin
from modules.images.models import Image


class IndexView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        json_dict = {
            'resources': {
                '/random': 'A random picture of a Japanese idol.',
                '/bomb(?count=5)': 'Bomb idols. Optionally, set how many you\'d like to bomb.',
                '/count': 'The number of idols we have.'
            },
            'source': 'https://github.com/bryanveloso/aidoru',
            'thanks': [
                'http://aigaki.tumblr.com/',
                'http://fyeahrokkies.tumblr.com/'
            ]
        }
        return self.render_json_response(json_dict)


class RandomImageChoiceView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        self.object = Image.objects.random()

        json_dict = {}
        json_dict['idol']['token'] = self.object.token
        json_dict['idol']['url'] = self.object.url
        return self.render_json_response(json_dict)


class CountTheImagesView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        json_dict = {'count': Image.objects.all().count()}
        return self.render_json_response(json_dict)


class BombIdolsView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        bombs = int(self.request.GET.get('id', 5))
        count = Image.objects.all().count()
        random_ids = sample(xrange(1, count), bombs)

        json_dict = {}
        json_dict['idols'] = [image.url for image in Image.objects.filter(id__in=random_ids)]
        return self.render_json_response(json_dict)
