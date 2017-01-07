from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^settings$', views.UpdateUserSettingsView.as_view(), name='user_settings'),
]
