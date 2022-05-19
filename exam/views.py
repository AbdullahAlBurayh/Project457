from unicodedata import name
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from exam.models import Exam, ExamSet, Question
# Create your views here.


def register_view(request):
    if 'first_name' in request.POST and 'last_name' in request.POST \
            and 'email' in request.POST and 'password' in request.POST:
        user = User(first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    username=request.POST['email'])
        user.set_password(request.POST['password'])
        user.save()
        login(request, user)
        return redirect(reverse('index'))
    return render(request, 'register.html')


def login_view(request):
    status = 0
    if 'email' in request.POST and 'password' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect(reverse('index'))
            else:
                status = 1
        except User.DoesNotExist:
            status = 2
    return render(request, 'login.html', {'status': status})


@login_required
def index_view(request):
    return render(request, 'index.html')


@login_required
def exam(request, exam_name):
    if request.method == 'POST':
        print(request.POST)
        exam = Exam.objects.get(name=exam_name)
        questions = exam.questions
        score = 0
        wrong = 0
        correct = 0
        total = 0
        test = 't'
        for q in questions.all():
            total += 1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer == request.POST.get(q.question):
                score += 10
                correct += 1
                test = request.POST.get(q.question)
            else:
                wrong += 1
                test = request.POST.get(q.question)
        percent = score/(total*10) * 100
        eSet = ExamSet.objects.create(exam, request.user, correct)
        eSet.save()
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
        }
        return render(request, 'result.html', context)
    else:
        exam = Exam.objects.get(name=exam_name)
        questions = exam.questions
        context = {
            'questions': questions
        }
        return render(request, 'exam.html', context)
