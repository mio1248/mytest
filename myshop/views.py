from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from shop.forms import PizzaLoginForm, PizzaSignupForm


class ShopLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = PizzaLoginForm
    redirect_authenticated_user = True


class ShopLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    http_method_names = ['post', 'options']



def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = PizzaSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PizzaSignupForm()

    return render(request, 'registration/signup.html', {'form': form})
