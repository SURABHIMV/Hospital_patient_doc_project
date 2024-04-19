"""
URL configuration for myproject project.

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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup_hospital/',views.signupPage_hospital,name='signup_hospital'),
    path('login_hospital/',views.loginPage_hospital,name='login_hospital'),
    path('adding_doc_patients/',views.admin_dashboard1,name='adding_doc_patients'),
    path('adding_doc_patients1/',views.admin_dashboard2,name='adding_doc_patients1'),
    path('adding_doc_patients2/',views.admin_dashboard3,name='adding_doc_patients2')

]

