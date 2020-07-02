import  json
from  rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList


class ProductListGetRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label_plural = "products"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, ReturnList):
            _data = json.loads(
                super(ProductListGetRenderer, self).render(data).decode('utf-8')
            )

            return json.dumps({
                self.object_label_plural: _data
            })
