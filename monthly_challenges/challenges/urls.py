from . import views
from django.urls import path
#from rest_framework import routers
#router = routers.DefaultRouter()

#router.register('challenges', views.index)

urlpatterns = [
    path('' , views.hello ),
    path('<int:month_int>' , views.redirect ),
    #path('<int:month_int>' , views.index ),
    path("<str:month>", views.hybrid),
   
]

