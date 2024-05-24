from django.contrib.auth.forms import UserCreationForm
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
            username = form.changed_data.get('username')
            password = form.changed_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('')
        
        context = {
            'form': form
        }

        return render(request, self.template_name, context)
