"""
URL configuration for project_data project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main_app import views
from project_data import settings

urlpatterns = [
    path('', views.students, name="home"),
    path('login', views.signin, name="login"),
    path('logout', views.signout, name="logout"),
    path('show', views.show_students, name="show"),
    path('search', views.students_search, name="search"),
    path('details/<int:student_id>', views.details, name="details"),
    path('students/delete/<int:student_id>', views.delete_student, name="delete"),
    path('students/update/<int:student_id>', views.update_student, name="update"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# python manage.py --help

# admin@gmail.com
# admin
# 123456

# /details/20
