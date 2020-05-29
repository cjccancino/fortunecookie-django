# Django
from django.conf.urls import url
from django.urls import path

# Test App
from test_project.test_app.views import index, update


app_name = 'test_app'

urlpatterns = [
    # url(r'^$', index, name='index'),
    path('', index, name='index'),
    path('<pk>/update', update, name='update')
]
