from django.conf.urls import url
from . import views

# Routes
urlpatterns = [
    url(r'^$',views.index, name='index'),    # ^ (starts with)..... $ (ends with)
    url(r'^details/(?P<id>\d+)/$',views.details, name='details')
]