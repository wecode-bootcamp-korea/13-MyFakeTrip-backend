from django.urls import path
from user.views import EmailSignUpView, EmailSignInView

urlpatterns = [
    path('/signup', EmailSignUpView.as_view()),
    path('/signin', EmailSignInView.as_view())
]
