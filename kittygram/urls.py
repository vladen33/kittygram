from django.urls import path

from cats.views import cat_list, hello

urlpatterns = [
   path('cats/', cat_list),
   path('hello/', hello),
]



