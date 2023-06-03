from django.contrib import admin
from django.urls import path
from api.views import RecognizePhoto, RecognizeAndAnswer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recognize/', RecognizePhoto.as_view()),
    path('answer/', RecognizeAndAnswer.as_view()),
]
