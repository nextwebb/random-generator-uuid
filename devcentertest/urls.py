from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# base project url patterns
# django provides an easy to use router for all your apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<version>/', include('api.urls'))

]
