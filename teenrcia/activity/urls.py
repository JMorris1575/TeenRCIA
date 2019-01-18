from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import WelcomeView, SummaryView, SectionView, ItemCreateView

app_name = 'activity'

urlpatterns = [
    path('welcome/', login_required(WelcomeView.as_view()), name='welcome'),
    path('<int:activity_index>/', login_required(SummaryView.as_view()), name='summary'),
    path('<int:activity_index>/<int:section_index>/', login_required(SectionView.as_view()), name='section'),
    path('<int:activity_index>/<int:section_index>/create_item/',
         login_required(ItemCreateView.as_view()), name='item_create'),
]