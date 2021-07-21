from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import nd_project, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns =[
    path('nd_project/', nd_project, name='nd_project'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
]