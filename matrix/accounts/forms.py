from django import forms
from .models import *
from django.contrib.auth.models import User
import datetime
from django.core import validators


class studentRegistration(forms.ModelForm):
    class Meta:
        model = students
        fields = ['student_id', 'student_fname', 'student_lname', 'student_email', 'student_gender', 'student_username',
                  'student_password', 'student_address', 'student_course', 'student_contactnumber',
                  'student_createdate']
        widgets = {
            # 'student_id': forms.TextInput(attrs={'class':'form-control'}),
            'student_fname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_lname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_email': forms.TextInput(attrs={'class': 'form-control'}),
            'student_gender': forms.TextInput(attrs={'class': 'form-control'}),
            'student_username': forms.TextInput(attrs={'class': 'form-control'}),
            'student_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'student_address': forms.Textarea(attrs={'class': 'form-control'}),
            'student_course': forms.TextInput(attrs={'class': 'form-control'}),
            'student_contactnumber': forms.TextInput(attrs={'class': 'form-control'}),
            'student_createdate': forms.TextInput(attrs={'class': 'form-control'})
        }


class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['feedback_id', 'feedback_message', 'feedback_date', 'student']
        widgets = {
                'feedback_id': forms.TextInput(attrs={'class': 'form-control'}),
                'feedback_message': forms.Textarea(attrs={'class': 'form-control'}),
                'feedback_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            # 'student': forms.TextInput(attrs={'class': 'form-control'})
        }

#
# class att(forms.Form):
#     class selectattendance(forms.Form):
#         Mark1 = 'P'
#         Mark2 = 'A'
#         markchoice = {
#             (Mark1, u"P"),
#             (Mark2, u"A")
#         }
#         atten = forms.ChoiceField(choices=markchoice)


class studentattendance(forms.ModelForm):
    class Meta:
        model = attendance
        fields = ['attendance_id', 'attendance_markattendance', 'attendance_date', 'student']
        widgets = {
            'attendance_id': forms.TextInput(attrs={'class': 'form-control'}),
            'attendance_markattendance': forms.TextInput(attrs={'class': 'form-control'}),
            'attendance_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            # 'student': forms.TextInput(attrs={'class': 'form-control'}),
        }


class studentexam(forms.ModelForm):
    class Meta:
        model = exam
        fields = ['exam_id', 'exam_markattendance', 'exam_date', 'exam_marks', 'exam_subject', 'student_id']
        widgets = {
            'exam_id': forms.TextInput(attrs={'class': 'form-control'}),
            'exam_markattendance': forms.TextInput(attrs={'class': 'form-control'}),
            'exam_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'exam_subject': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'exam_marks': forms.DateTimeInput(attrs={'class': 'form-control'}),
            # 'student': forms.TextInput(attrs={'class': 'form-control'})
        }
