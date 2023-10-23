from django.shortcuts import render
from LagoNessBlog.models import Article
# from LagoNessBlog.forms import CreationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# navbar --> html templates are still missing


def home(request):
    return render(request, "LagoNessBlog/index.html")


def about(request):
    return render(request, 'LagoNessBlog/aboutme.html')


def register(request):
    return render(request, "LagoNessBlog/register.html")


def login(request):
    return render(request, "LagoNessBlog/login.html")


def others(request):
    return render(request, "LagoNessBlog/others.html")


def youtube(request):
    return render(request, "LagoNessBlog/youtube.html")


def travelling(request):
    return render(request, "LagoNessBlog/travelling.html")


def sports(request):
    return render(request, "LagoNessBlog/sports.html")


# CRUD


# # def create(request):
#     return render(request, "LagoNessBlog/articleCreation.html")


# # def success(request):
#     return render(request, "LagoNessBlog/success.html")


# def creationForm(request):

#     if request.method == "POST":

#         newArticle = CreationForm(request.POST)

#         if newArticle.is_valid():
#             info = newArticle.cleaned_data
#             article = Article(
#                 name=info["name"],
#                 category=info["category"],
#                 description=info["description"],
#                 date=info["date"],
#                 emailContact=info["emailContact"],
#                 image=info["image"])
#             article.save()
#             return render(request, "LagoNessBlog/success.html")
#     else:
#         newArticle = CreationForm()

#     return render(request, "LagoNessBlog/articleCreation.html", {"newArticle": newArticle})


# # def readArticles(request):

#     articles = Article.objects.all()
#     context = {"articles": articles}

#     return render(request, "LagoNessBlog/readArticles.html", context)


# # def deleteArticle(request, article_id):
#     article = Article.objects.get(id=int(article_id))
#     article.delete()

#     return readArticles(request)


# # def editArticle(request, article_id):

#     if request.method == "POST":

#         newArticle = CreationForm(request.POST)

#         if newArticle.is_valid():
#             info = newArticle.cleaned_data
#             article = Article.objects.get(id=int(article_id))
#             article.name = info["name"],
#             article.category = info["category"],
#             article.description = info["description"],
#             article.date = info["date"],
#             article.emailContact = info["emailContact"],
#             article.image = info["image"]
#             article.save()
#             return render(request, "LagoNessBlog/successEdition.html")
#     else:
#         article = Article.objects.get(id=int(article_id))
#         newArticle = CreationForm(initial={"name": article.name, "category": article.category, "description": article.description,
#                                   "date": article.date, "emailContact": article.emailContact, "image": article.image})

#     return render(request, "LagoNessBlog/articleEdition.html", {"newArticle": newArticle})


class ArticleCreateView(CreateView):
    model = Article
    template_name = "LagoNessBlog/articleCreateView.html"
    success_url = reverse_lazy("List")
    fields = ['name', 'category', 'description', 'emailContact', 'image']


class ArticleListView(ListView):
    model = Article
    template_name = "LagoNessBlog/articleListView.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "LagoNessBlog/articleDetailView.html"


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "LagoNessBlog/articleUpdateView.html"
    success_url = reverse_lazy("List")
    fields = ['name', 'category', 'description', 'emailContact', 'image']


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("List")
    template_name = "LagoNessBlog/articleDeleteViewConfirmation.html"
