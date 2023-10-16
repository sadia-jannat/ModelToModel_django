"""modelproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

    path('one_by_one/<str:pk>', views.one_by_one, name='one_by_one'),
    def one_by_one(request,pk):
        fe=Person.objects.get(id=pk)
        context={'fe':fe,}
        return render(request, 'one_by_one.html', context) 
"""
from django.contrib import admin
from django.urls import path

from model.views import PersonDetails,OneDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', PersonDetails.as_view()),
    path('one/<str:id>', OneDetails.as_view()),
    
]
