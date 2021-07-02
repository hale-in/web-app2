from django.urls import path

from accountapp.views import nd_project

app_name = 'accountapp'

urlpatterns =[
    path('nd_project', nd_project, name='nd_project')
]