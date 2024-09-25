from django.urls import path

# from cats.views import APICat, APICatDetail, hello
from cats.views import CatDetail, CatList

urlpatterns = [
   path('cats/', CatList.as_view()),
   path('cats/<int:pk>/', CatDetail.as_view())
   # path('cats/', APICat.as_view()),
   # path('cats/<int:pk>/', APICatDetail.as_view()),
   # path('hello/', hello),
]



