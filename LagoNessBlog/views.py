from django.shortcuts import render
from LagoNessBlog.models import Article
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from LagoNessBlog.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# NAVBAR


def home(request):
    return render(request, "LagoNessBlog/index.html")


def about(request):
    return render(request, 'LagoNessBlog/aboutme.html')

# LOGIN/OUT


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            unique_password = form.cleaned_data.get('password')
            user = authenticate(username=user, password=unique_password)

            if user is not None:
                login(request, user)

                return render(request, "LagoNessBlog/index.html", {"notification": f"Welcome {user}"})

            else:
                form = AuthenticationForm()
                return render(request, "LagoNessBlog/login.html", {"notification": "Wrong data", "form": form})

        else:
            return render(request, "LagoNessBlog/login.html", {"notification": "Invalid form"})

    form = AuthenticationForm()

    return render(request, "LagoNessBlog/login.html", {"form": form})


def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "LagoNessBlog/index.html", {"notification": "User has been created!"})

    else:
        form = UserRegisterForm()

    return render(request, "LagoNessBlog/register.html", {"form": form})

# EDIT USER


@login_required
def editUser(request):
    user = request.user

    if request == 'POST':
        editUser = UserEditForm(request.POST)
        if editUser.is_valid():

            info = editUser.cleaned_data

            if info["password1"] != info["password2"]:
                orig_data = {
                    'first_name': user.first_name,
                    'email': user.email
                }
                editUser = UserEditForm(initial=orig_data)

            else:
                user.email = info['email']
                user.username = info['username']
                user.set_password(info['password1'])
                user.last_name = info['last_name']
                user.first_name = info['first_name']
                user.save()

            return render(request, "LagoNessBlog/index.html")

    else:
        data = {'email': user.email,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
                }
        editUser = UserEditForm(initial=data)

    return render(request, "LagoNessBlog/editUser.html", {"editUser": editUser, "user": user})

# CRUD


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "LagoNessBlog/articleCreateView.html"
    success_url = reverse_lazy("List")
    fields = ['name', 'category', 'description', 'emailContact', 'image']


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "LagoNessBlog/articleListView.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "LagoNessBlog/articleDetailView.html"


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "LagoNessBlog/articleUpdateView.html"
    success_url = reverse_lazy("List")
    fields = ['name', 'category', 'description', 'emailContact', 'image']


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("List")
    template_name = "LagoNessBlog/articleDeleteViewConfirmation.html"


# # CREACION INSTRUMENTO

# class InstrumentoCreacion(LoginRequiredMixin, CreateView):
#     model = Instrumento
#     form_class = FormularioNuevoInstrumento
#     success_url = reverse_lazy('home')
#     template_name = 'Base/instrumentoCreacion.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(InstrumentoCreacion, self).form_valid(form)

# # TECLADO

# class TecladoLista(LoginRequiredMixin, ListView):
#     context_object_name = 'teclados'
#     queryset = Instrumento.objects.filter(instrumento__startswith='teclado')
#     template_name = 'Base/listaTeclados.html'

# class TecladoDetalle(LoginRequiredMixin, DetailView):
#     model = Instrumento
#     context_object_name = 'teclado'
#     template_name = 'Base/tecladoDetalle.html'

# class TecladoUpdate(LoginRequiredMixin, UpdateView):
#     model = Instrumento
#     form_class = ActualizacionInstrumento
#     success_url = reverse_lazy('teclados')
#     context_object_name = 'teclado'
#     template_name = 'Base/tecladoEdicion.html'

# class TecladoDelete(LoginRequiredMixin, DeleteView):
#     model = Instrumento
#     success_url = reverse_lazy('teclados')
#     context_object_name = 'teclado'
#     template_name = 'Base/tecladoBorrado.html'