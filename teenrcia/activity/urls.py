from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import WelcomeView

app_name = 'activity'

urlpatterns = [
    path('welcome/', login_required(WelcomeView.as_view()), name='welcome'),
]