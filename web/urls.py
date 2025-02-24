from .                              import views
from django.urls                    import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_request/', views.create_request_page, name='create_request'),
    path('track_request/<int:id>/', views.track_request_page, name='track_request'),
    path('account_info/', views.account_info, name='account_info'),
]
