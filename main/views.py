from typing import ContextManager
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from main.models import Answers, Quizzes, User, Ways
from django.http import JsonResponse

# Create your views here.

class FirstView(View):
    def get(self, request):
        ans = Answers.objects.get(id=3)
        print(ans.ans_quizz)
        return render(request, 'home.html')

class Register(View):
    def get(self, request):
        try:
            if request.session['user_id']:
                return redirect('/ways')
        except:
            pass
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
            last = User.objects.last()
            request.session['user_id'] = last.id
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
    'user':request.session['user_id']
    }
    
    return render(request, 'tests.html', context)

def answer(request):
    user_id = int(request.GET.get('user'))
    ans_id = int(request.GET.get('id'))
    quiz_id = int(request.GET.get('quiz'))
    user = User.objects.get(id=user_id)
    answer = Answers.objects.get(id=ans_id)
    quiz = Quizzes.objects.get(id=quiz_id)
    if answer.true_or_false == True:
        try:
            user.false_a.remove(quiz)
        except:
            pass
        user.true_a.add(quiz)
    else:
        try:
            user.true_a.remove(quiz)
        except:
            pass
        user.false_a.add(quiz)
    
    return JsonResponse({'status':'true'})


def results(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    context = {
        'user':user
    }
    return render(request, 'results.html', context)

def del_session(request):
    request.session.clear()
    return redirect('/')