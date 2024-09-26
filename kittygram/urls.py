from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet
# from cats.views import APICat, APICatDetail, hello
# from cats.views import CatDetail, CatList

router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
   # path('cats/', CatList.as_view()),
   # path('cats/<int:pk>/', CatDetail.as_view())
   # path('cats/', APICat.as_view()),
   # path('cats/<int:pk>/', APICatDetail.as_view()),
   # path('hello/', hello),
]



