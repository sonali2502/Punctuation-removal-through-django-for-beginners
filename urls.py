"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .import views # to use views.py to show data on website

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),                            # first arg= endpoint, here is blank which means http://127.0.0.1:8000
   # path('rempunc', views.rempunc, name='rempunc'),                # first arg= endpoint, here is about which means http://127.0.0.1:8000/rempunc
   # path('capitalizefirst', views.capfirst, name='capitalfirst'),  # sec arg  means the func to be performed on loading the page 
   # path('newlineremove', views.newlineremove, name='newlremove'),     # third arg means the name given to path
   # path('spaceremove', views.spaceremove, name='spacerem'),
   # path('charcount', views.charcount, name='chrcount')
 path('analyze', views.analyze, name='analyze')
   
]









# as soon as we update statement in any .py file it automatically gets updated in server
# strting development provided by django wee are using for practice purpose later we will cfreate our own, http://127.0.0.1:8000/

# # django first reaches urls.py search for urlpatterns then will go to views to to run those func to dispaly a website