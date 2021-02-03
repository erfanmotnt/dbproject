from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views.tagview import *
router = DefaultRouter()
# router.register('questionproperties', QuestionPropertiesView)
# router.register('questionproperties/<int:pk>', QuestionPropertiesView)

urlpatterns = [
    path('tag/', tagview),
    
]

urlpatterns += router.urls
