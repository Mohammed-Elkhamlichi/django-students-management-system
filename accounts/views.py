from django.shortcuts import render
from accounts.models import Student
from django.http import HttpResponseRedirect
from accounts.forms import StudentForm
# Create your views here.

# Students Details.
def base(request):
    students = Student.objects.all()
    form = StudentForm()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        form = StudentForm(request.POST)
        if first_name and last_name and email:
            form.first_name= first_name
            form.last_name = last_name
            form.email = email
            form.save(True)
            return HttpResponseRedirect('http://127.0.0.1:8000/')
        else:
            form = StudentForm()
            return HttpResponseRedirect('.')
    context = {
        "dev": 'Mohammed',
        'form': form
    }
    return render(request, 'base.html', context)