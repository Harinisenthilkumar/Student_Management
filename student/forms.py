from django import forms
from django.contrib.auth.models import User
from .models import Student

# Student signup form
class StudentSignupForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Student
        fields = ['full_name', 'mobile_number', 'course', 'paid_fees']

    def save(self, commit=True):
        # Create the User model instance first
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        
        # Now create the Student model instance linked to this user
        student = super().save(commit=False)
        student.user = user
        
        if commit:
            student.save()
        
        return student

# Student login form
class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
