from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import studentRegistration, feedbackform, studentattendance, studentexam
from .models import students, extenduser, attendance, feedback


# Create your views here.
def login_index(request):
    return render(request, 'login_index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'login_index.html')
        else:
            messages.info(request, 'invalid Credential')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def staff_register(request):
    if request.method == 'POST':
        first_name = request.POST['input_Firstname']
        last_name = request.POST['input_Lasttname']
        username = request.POST['input_Username']
        email = request.POST['input_Email']
        Password = request.POST['input_Password']
        password2 = request.POST['input_Password']
        date = request.POST['input_Doj']
        contactnumber = request.POST['input_Contact']
        address = request.POST['input_Address']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        email=email, password=Password, date_joined=date)
        nextend = extenduser(phone_num=contactnumber, address=address, user=user)
        nextend.save()
        userdata = extenduser.objects.all()
        messages.info(request, "User created")

        return render(request, 'staff_registration.html', )
    else:
        return render(request, 'staff_registration.html')


def show_data(request):
    data1 = User.objects.all()
    return render(request, 'staff_detail.html', {'datas': data1})


# this function register data
def student_register(request):
    if request.method == 'POST':
        fm = studentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = studentRegistration()
    else:
        fm = studentRegistration()
    studentsdata = students.objects.all()
    return render(request, 'StudentAdmission.html', {'form': fm, 'studentdata': studentsdata})


def studentdetail(request):
    if request.method == 'POST':
        answer = request.POST['results']
        fm = studentRegistration()
        studentsdata = students.objects.filter(student_id=answer)
        return render(request, 'test.html', {'form': fm, 'studentdata': studentsdata, 'ans': answer})
    else:
        fm = studentRegistration()
        studentsdata = students.objects.all()
        return render(request, 'student_detail.html', {'form': fm, 'studentdata': studentsdata})


# this function delete students data
def delete_data(request, id):
    if request.method == 'POST':
        pi = students.objects.get(pk=id)
        pi.delete()
        fm = studentRegistration()
        studentsdata = students.objects.all()
        return render(request, 'StudentAdmission.html', {'form': fm, 'studentdata': studentsdata})


# this function update the students data
def update_data(request, id):
    if request.method == 'POST':
        pi = students.objects.get(pk=id)
        fm = studentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = students.objects.get(pk=id)
        fm = studentRegistration(instance=pi)
    return render(request, 'Update_student.html', {'form': fm})


def student_attendance(request):
    if request.method == 'POST':
        fms = studentattendance(request.POST)
        if fms.is_valid():
            fms.save()
            fms = studentattendance()
    else:
        fms = studentattendance()
    attdata = attendance.objects.all()
    return render(request, 'Student_attendance.html', {'form': fms, 'attdata': attdata})


def student_exam(request):
    if request.method == 'POST':
        fms = studentexam(request.POST)
        if fms.is_valid():
            fms.save()
            fms = studentexam()
    else:
        fms = studentexam()
    return render(request, 'student_exam.html', {'form': fms})


def feedback_form(request):
    if request.method == 'POST':
        fms = feedbackform(request.POST)
        if fms.is_valid():
            fms.save()
            fms = feedbackform
    else:
        fms = feedbackform()
    return render(request, 'feedback_form.html', {'form': fms})

def showfeedback(request):
    feedbackdata = feedback.objects.all()
    return render(request,'showfeedback.html',{'feedback':feedbackdata})

def logout(request):
    auth.logout(request)
    return redirect('login')
