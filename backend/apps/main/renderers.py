import json

from rest_framework.renderers import JSONRenderer


class CartJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            # Позволим стандартному JSONRenderer обрабатывать ошибку.
            return super(CartJSONRenderer, self).render(data)

        # Наконец, мы можем отобразить наши данные в простанстве имен 'user'.
        return json.dumps({
            'data': data
        })
