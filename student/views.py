from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import StudentSignupForm, StudentLoginForm
from.models import Student

# Student Signup View
def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('student_login')  # Redirect to login page 
    else:
        form = StudentSignupForm()

        return render(request, 'student_signup.html', {'form': form})

# Student Login View
def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('student_list')  # Redirect to student list page after successful login
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = StudentLoginForm()

    return render(request, 'student_login.html', {'form': form})
# student list

def student_list(request):
    students = Student.objects.all()  # Fetch all student records
    return render(request, 'student_list.html', {'students': students})
