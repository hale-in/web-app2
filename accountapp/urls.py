from django.urls import path

from accountapp.views import nd_project, AccountCreateView

app_name = 'accountapp'

urlpatterns =[
    path('nd_project/', nd_project, name='nd_project'),
    path('create/', AccountCreateView.as_view(), name='create')
]