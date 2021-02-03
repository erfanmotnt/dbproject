from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views.tagview import *
from .views.problemview import *
from .views.accountview import *
from .views.trigers import *
router = DefaultRouter()
# router.register('questionproperties', QuestionPropertiesView)
# router.register('questionproperties/<int:pk>', QuestionPropertiesView)

urlpatterns = [
    path('tag/', tagview),
    path('subtag/', subtagview),
    path('problem/', problemview),
    path('account/', accountview),
    path('initial/', initial),
]

urlpatterns += router.urls
