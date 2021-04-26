from django.shortcuts import render, HttpResponse
from add_user.models import AddUser


def index(request):

    show_user = AddUser.objects.all()

    context = {
        'show_user': show_user,
    }

    return render(
        template_name='show_user.html',
        request=request,
        context=context,

    )


def add_user(request):

    if request.method == 'POST':

        add_user = AddUser(
            username=request.POST['username'],
            email=request.POST['email'],
        )

        add_user.save()

        context = {
            'username': add_user.username,
            'email': add_user.email,
        }

        return render(
            template_name='new_user.html',
            request=request,
            context=context,
        )


    return render(
        template_name='add_user.html',
        request=request,
        context={},
    )

# Create your views here.
