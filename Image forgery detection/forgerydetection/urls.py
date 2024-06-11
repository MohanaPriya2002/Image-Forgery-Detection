from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('Admin_login/',views.Admin_login,name='Admin_login'), 
    path('Stylish_login/',views.Stylish_login,name='Stylish_login'), 
    path('User_login/',views.User_login,name='User_login'), 
    path('Register/',views.Register,name='Register'), 
    path('StylishRegister/',views.StylishRegister,name='StylishRegister'), 
    path('logout/',views.logout,name='logout'),
    path('ViewUsers/',views.ViewUsers,name='ViewUsers'), 
    path('Stylish_Chat/',views.Stylish_Chat,name='Stylish_Chat'),    
    path('User_Chat/',views.User_Chat,name='User_Chat'),    
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('User_CP/',views.User_CP,name='User_CP'),
    path('MyDetails/',views.MyDetails,name='MyDetails'),
    path('ViewStylish/',views.ViewStylish,name='ViewStylish'),
   
    path('AcceptStylish/',views.AcceptStylish,name='AcceptStylish'),
    path('ManageSubscription/',views.ManageSubscription,name='ManageSubscription'),
    path('AcceptRequest/<int:id>',views.AcceptRequest,name='AcceptRequest'),
    path('UpdateSubs/',views.UpdateSubs,name='UpdateSubs'),
    path('Chatreply/', views.Chatreply, name='Chatreply'),
    path('StylishChatreply/', views.StylishChatreply, name='StylishChatreply'),
    path('FillUserChat/', views.FillUserChat, name='FillUserChat'),
    path('FillStylishChat/', views.FillStylishChat, name='FillStylishChat'),
    path('UpdateSubscription/', views.UpdateSubscription, name='UpdateSubscription'),
   
    ]

