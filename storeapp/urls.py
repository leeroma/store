from django.urls import path

from storeapp.views import main_page_view


urlpatterns = [
    path('', main_page_view, name='main_page'),
]
