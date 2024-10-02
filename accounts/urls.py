from django.urls import path, re_path
from accounts.views import login_view, logout_view, signup_view
# from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    #login
    path('login/', login_view, name='login'),
    #logout
    path('logout/', logout_view, name='logout'),
    #registration / Sighn-Up
    path('signup', signup_view, name='signup'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() ,name='password_reset_confirm'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view() , name="resetdone"),
    # #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html') ,name='resetconfirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view() , name='password_reset_complete'),
]