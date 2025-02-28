from django.urls import path
from.import views
urlpatterns=[
     path('',views.index,name='index'),
    
     path('register/',views.register,name='register'),
     path('login_view/',views.login_view,name='login_view'),
     # path('homepage/',views.homepage,name='homepage'),
     path('recommand/',views.recommand,name='recommand'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     # path('movies/',views.movies,name='movies'),
    
]
