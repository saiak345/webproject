from django.shortcuts import render
from college.models import student
from college.forms import studentmodelform
# Create your views here.

from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def logoutuser(request):
    print('sucessfully logged out')
    return homepage(request)


def login(request):
    return render(request,'registration/login.html')

def homepage(request):
    return render(request,'home.html')

@login_required()
def studentcell(request):

    return render(request,'student/studentcell.html')

@login_required()
@permission_required('college.change_student')
def addstd(request):
    form=studentmodelform
    studentform={'form':form}

    if request.method=='POST':
        form=studentmodelform(request.POST)
        if form.is_valid():
            form.save()
        return studentcell(request)

    return render(request,'student/addstudent.html',studentform)

@login_required()
@permission_required('college.view_student')
def stdreport(request):
    result=student.objects.all(); #select * from student
    #it returns objects in query form


    students={'allstudents':result}

    return render(request,'student/studentreport.html',students)

@login_required
@permission_required('college.delete_student')
def deletestudent(request,id):
    s=student.objects.get(id=id)
    s.delete()
    return studentcell(request)

@login_required
@permission_required('college.change_student')
def updatestudent(request,id):
    s=student.objects.get(id=id)
    form=studentmodelform(instance=s)
    dict={'form':form}

    if request.method=='POST':
        form=studentmodelform(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return studentcell(request)
    return render(request,'student/updated.html',dict)




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
