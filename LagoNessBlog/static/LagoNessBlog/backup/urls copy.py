from django.urls import path
from LagoNessBlog import views


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name="Home"),
    # path('success/', views.success, name="Success"),
    path('aboutme/', views.about, name='AboutMe'),
    # path('creation/', views.creationForm, name="Creation"),
    # path('readarticles/', views.readArticles, name="readArticles"),
    # path('deletearticle/<int:article_id>/',
    #     views.deleteArticle, name="deleteArticle"),
    # path('editarticle/<int:article_id>/',
    #     views.editArticle, name="editArticle"),
]

urlpatterns += [
    path('class/list/', views.ArticleListView.as_view(), name="List"),
    path('class/detail/<int:pk>/', views.ArticleDetailView.as_view(), name="Detail"),
    path('class/new/', views.ArticleCreateView.as_view(), name="New"),
    path('class/update/<int:pk>/', views.ArticleUpdateView.as_view(), name="Update"),
    path('class/delete/<int:pk>/', views.ArticleDeleteView.as_view(), name="Delete"),
]
