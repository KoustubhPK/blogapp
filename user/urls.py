from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.UserLogin, name='userlogin'),
    path('register/', views.UserRegister, name='userregister'),
    path('logout/', views.UserLogout, name='userlogout'),
    path('profile/', views.UserProfile, name='userprofile'),
    path('profile/edit', views.EditProfile, name='editprofile'),

    path('terms&conditions/', views.UserTerms, name='terms_and_conditions'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'), 
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]
