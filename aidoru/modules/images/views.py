import random

from django.views.generic import View

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
        json_dict['token'] = self.object.token
        json_dict['url'] = self.object.url
        json_dict['idols'] = [i.slug for i in self.object.idols.all()]
        return self.render_json_response(json_dict)


class CountTheImagesView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        json_dict = {'count': Image.objects.all().count()}
        return self.render_json_response(json_dict)


class BombIdolsView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        bombs = int(self.request.GET.get('count', 5))
        count = Image.objects.all().count()
        random_ids = random.sample(xrange(1, count), bombs)

        json_dict = {}
        json_dict['blast'] = [image.url for image in Image.objects.filter(id__in=random_ids)]
        return self.render_json_response(json_dict)
