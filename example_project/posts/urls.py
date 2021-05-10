from django.urls import path
from .views import HomePageView,CreatePostView
urlpatterns = [
    path('enroll/', HomePageView.as_view(), name = 'home'),
    path('enroll/post/', CreatePostView.as_view(), name = 'add_post'),

]