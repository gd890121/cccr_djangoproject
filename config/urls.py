from django.contrib import admin
from django.urls import include, path
from table import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', include('table.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]
