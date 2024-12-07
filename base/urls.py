from django.urls import path
from . import views

urlpatterns = [
    
    # Authentication
    path('login/', views.loginPage, name="login"), #login_registration
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    
    # Home and Rooms
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name="room"),
    
    #Profiles
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    
    #Room Management
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    
    path('jobDetails/', views.jobDetails, name='job-details'),
    
    # Project Management
    path('project/', views.project, name='project'),
    # path('projects/create/', views.createProject, name='create-project'),
    # path('projects/delete/<str:pk>/', views.deleteProject, name='delete-project'),
    
]