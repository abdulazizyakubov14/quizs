from typing import ContextManager
from django.shortcuts import render, redirect
from django.views import View

from main.models import Quizzes, User, Ways

# Create your views here.

class FirstView(View):
    def get(self, request):
        return render(request, 'home.html')

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            tel_num = request.POST.get('tel_num')
            time = request.POST.get('time')
            new = User.objects.create(
                name=name,
                surname=surname,
                tel_num=tel_num,
                times=time,
            )
            new.save()
            return redirect('/ways')
        return render(request, 'register.html')

def ways(request):
    cats = Ways.objects.all()
    context = {
        'cats':cats
    }
    return render(request, 'ways.html', context)


def quiz(request, slug):
    ways = Ways.objects.get(slug=slug)
    quizz = Quizzes.objects.filter(ways=ways)
    context = {
        'quiz':quizz,
    }
    return render(request, 'tests.html', context)