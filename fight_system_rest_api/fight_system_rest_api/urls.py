"""fight_system_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from heroes import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^heroes/$', views.HeroesList.as_view()),
    url(r'^heroes/(?P<pk>[0-9]+)/$', views.HeroesDetail.as_view()),
    url(r'^heroes/ranking/$', views.HeroesRanking.as_view()),
    url(r'^heroes/deads/$', views.HeroesDeads.as_view()),
    url(r'^heroes/kill/(?P<pk>[0-9]+)/$', views.HeroesKill.as_view()),
    url(r'^battles/$', views.BattleList.as_view()),
    url(r'^battles/(?P<pk>[0-9]+)/$', views.BattleDetail.as_view()),
    url(r'^battles/random/$', views.BattleRandom.as_view()),
    
    #url(r'^users/$', views.UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
