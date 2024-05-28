from login_app.forms import UserCreationForm
from login_app.utils import send_email_for_verify

from django.contrib.auth import authenticate, login
from django.views import View


from django.shortcuts import render, redirect

class Register(View):
    template_name = 'registration/register.html'


    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)

            send_email_for_verify()
            return redirect('confirm_email')

            # login(request, user)
            # return redirect('main_menu')
        
        context = {
            'form': form
        }

        return render(request, self.template_name, context)
