from django.urls import path
from myapi.core import views
from django.conf.urls import url

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Questionaire API",
      default_version='v1',
      description="Test project to simulate Questionnaire APIs",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('list', views.QuestionnaireView.as_view(), name='Questionnaire'),
	path('sync', views.SyncDataView.as_view(), name='mobileapitask'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
