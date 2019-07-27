"""objective_questions_guru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from static_pages.views import about,contact
from questions.views import question_add,answer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', answer, name='home'),
    path('uncategorized', answer, name='uncategorized'),
    path('excel', answer, name='excel'),
    path('word', answer, name='word'),
    path('powerpoint', answer, name='powerpoint'),
    path('operating_system', answer, name='operating_system'),
    path('computer_misc', answer, name='computer_misc'),
    path('add', question_add, name='add'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
