from django.contrib import admin
from django.urls import path
from api.views import Receive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recognize/', Receive.as_view())
]
