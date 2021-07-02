from django.urls import path

from accountapp.views import write_correct

app_name = 'accountapp'

urlpatterns =[
    path('2nd_project', write_correct, name='2nd_project')
]