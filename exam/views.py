from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout
from django.core.mail import send_mail
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
    user = request.user
    exams = user.examSet_set
    context = {
        'exams': exams,
    }
    return render(request, 'index.html', context)


def ranking(request):
    try:
        users = User.objects.all()
        PreRanking = []
        ranking = []
        for user in users:
            for exam_set in user.examSet_set.all():
                PreRanking.append((exam_set.user, exam_set.exam,
                                   exam_set.marks, exam_set.highest))

        ranking.append(
            sorted(PreRanking, key=lambda grade: grade[2], reverse=True))
        context = {
            'ranking': ranking,
        }

        return render(request, 'index.html', context)
    except:
        pass
