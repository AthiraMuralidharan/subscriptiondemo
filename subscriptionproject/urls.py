"""subscriptionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from membership import views

urlpatterns = [
    path('membership/', include('membership.urls')),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', views.SignUp.as_view(), name='signup'),
    path('auth/settings', views.settings, name='settings'),
    path('join', views.join, name='join'),
    path('checkout', views.checkout, name='checkout'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),
    path('updateaccounts', views.updateaccounts, name='updateaccounts'),
    path('pausepayments',views.pausepayments,name='pausepayments'),
    path('delete',views.delete,name='delete'),
    path('Resumepayment',views.Resumepayment,name='Resumepayment'),
    path('Updatesubscription',views.Updatesubscription,name='Updatesubscription'),

]