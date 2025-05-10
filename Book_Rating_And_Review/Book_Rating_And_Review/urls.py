"""
URL configuration for Book_Rating_And_Review project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
    path('', index, name="index"),
    path('profile', profile, name="profile"),
    path('logout', logout, name='logout'),
    path('thankyou', thankyou, name='thankyou'),
    path('add_book', add_book, name='add_book'),
    path('manage_book', manage_book, name='manage_book'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit/<int:id>',edit,name="edit"),
    path('add_review/<int:id>',add_review,name="add_review"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


