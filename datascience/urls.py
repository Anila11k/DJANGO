from django.urls import path
from.import views
urlpatterns=[
    path('name/',views.datas,name="datas"),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('homepage/',views.homepage,name='homepage')
]