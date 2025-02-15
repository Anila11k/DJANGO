from django.urls import path
from.import views
urlpatterns=[
    path('name/',views.datas,name="datas"),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('homepage/',views.homepage,name='homepage'),
    path('recommand/',views.recommand,name='recommand'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('movies/',views.movies,name='movies')
]
