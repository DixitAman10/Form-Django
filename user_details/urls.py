from django.urls import path
from . import views


app_name = 'user_details'

urlpatterns = [
    path('', views.CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:user_id>', views.UserProfileView.as_view(), name='user_profile')
]
