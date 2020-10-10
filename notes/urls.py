from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('temp', views.temp, name='temp'), # delete later
    path('', views.index, name='home'),
    path('take_note/', views.add_note, name='take_note'),
    path('view/<str:pk>/', views.view_note, name='view_note'),
    path('delete/<str:pk>/', views.delete_note, name='delete_note'),
    path('edit/<str:id>/', views.edit_note, name='edit_note'),
    path('archived/', views.archived_note, name='archived'),

    # Register urls
    path('register/', views.register, name='register'),

    # Password Change urls
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),
         name='password_change'),

    # Password Reset urls
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset1'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done1'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm1'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete1'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
