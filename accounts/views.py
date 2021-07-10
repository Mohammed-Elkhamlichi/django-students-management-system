from django.shortcuts import render
from accounts.models import Student
from django.http import HttpResponseRedirect

# Create your views here.
def base(request):
    students = Student.objects.all()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        if first_name and last_name and email:
            Student.objects.create(first_name=first_name, last_name=last_name, email=email)
            print(first_name, last_name, email)
        else:
            return HttpResponseRedirect('.')
    context = {
        "dev": 'Mohammed'
    }
    return render(request, 'base.html', context)