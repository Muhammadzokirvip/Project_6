# from django.urls import path
# from .views import *
# urlpatterns = [
#     path('', index, name='index'),]


from django.urls import path
from .views import HomePageView, categori, latest_news, contact
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('categori', categori, name='categori'),
    path('contact', contact, name='contact'),
    path('latest_news', latest_news, name='latest_news'),
]

