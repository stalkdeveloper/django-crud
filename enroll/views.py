from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    students = User.objects.all()
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save()
            
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            
            user = User(name=name, email=email, password=password)
            user.save()
            return redirect('addandshow')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/addandshow.html', {'form' :fm, 'students' :students})

def update_data(request, id):
    if request.method == 'POST':
        student = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=student)
        if fm.is_valid():
            fm.save()
            
        return redirect('addandshow')
    else:
        student = User.objects.get(pk=id)
        fm = StudentRegistration(instance=student)
    return render(request, 'enroll/updatestudent.html', {'form' :fm}) 


def deleteStudent(request, id):
    if request.method == 'POST':
        student = get_object_or_404(User, pk=id)
        student.delete()
        return redirect('addandshow')
    
    