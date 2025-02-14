"""
URL configuration for job_portal project.

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
from django.contrib import admin
from django.urls import path
from jobapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login,name='login'),
    path('register', views.user_register,name='register'),
    path('index', views.index,name='index'),
    path('job/search', views.job_search,name='job_search'),
    path('job/all', views.all_jobs,name='all_jobs'),
    path('job/<int:job_id>/', views.job_details, name='job_details'),
    path('job/apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('company/list', views.company_list, name='company_list'),
    path('user/profile', views.user_profile, name='user_profile'),
    path('user/logout', views.user_logout, name='user_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)