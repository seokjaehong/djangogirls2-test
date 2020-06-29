from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",views.post_list, name='post_list'),
    path("post/<int:pk>/",views.post_detail, name='post_detail'),
    path("post/<int:pk>/edit/",views.post_edit, name='post_edit'),
]
