from django.urls import path
from LagoNessBlog import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name="Home"),
    path('aboutme/', views.about, name='AboutMe'),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='LagoNessBlog/logout.html'), name='Logout'),
    path('edituser/', views.editUser, name="EditUser")

]

urlpatterns += [
    path('class/list/', views.ArticleListView.as_view(), name="List"),
    path('class/detail/<int:pk>/', views.ArticleDetailView.as_view(), name="Detail"),
    path('class/new/', views.ArticleCreateView.as_view(), name="New"),
    path('class/update/<int:pk>/', views.ArticleUpdateView.as_view(), name="Update"),
    path('class/delete/<int:pk>/', views.ArticleDeleteView.as_view(), name="Delete"),
]
