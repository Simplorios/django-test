from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler

from django.conf.urls import url

from django_plotly_dash.consumers import MessageConsumer, PokePipeConsumer
from django_plotly_dash.util import pipe_ws_endpoint_name, http_endpoint, http_poke_endpoint_enabled


http_routes = [
    ]

if http_poke_endpoint_enabled():
    http_routes.append(url(http_endpoint("poke"), PokePipeConsumer))

http_routes.append(url("^", AsgiHandler))

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                url(pipe_ws_endpoint_name(), MessageConsumer),

            ]
        )
    ),
    'http': AuthMiddlewareStack(URLRouter(http_routes)),
    })



