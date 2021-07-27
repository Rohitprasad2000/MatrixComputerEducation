from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class extenduser(models.Model):
    phone_num = models.CharField(max_length=15)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class students(models.Model):
    student_id = models.AutoField(primary_key=True,auto_created=True)
    student_fname = models.CharField(max_length=50)
    student_lname = models.CharField(max_length=50, null=True)
    student_email = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=2)
    student_username = models.CharField(max_length=50)
    student_password = models.CharField(max_length=50)
    student_address = models.TextField()
    student_course = models.CharField(max_length=50)
    student_contactnumber = models.CharField(max_length=10)
    student_createdate = models.DateTimeField(null=True)

    def __int__(self):
        return self.student_id


class staffs(models.Model):
    objects = None
    staff_id = models.IntegerField(primary_key=True)
    staff_fname = models.CharField(max_length=50)
    staff_lname = models.CharField(max_length=50)
    staff_email = models.CharField(max_length=100)
    staff_gender = models.CharField(max_length=2)
    staff_username = models.CharField(max_length=50)
    staff_password = models.CharField(max_length=50)
    staff_address = models.TextField()
    staff_contactnumber = models.CharField(max_length=10)

    def __int__(self):
        return self.staff_id


class feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback_message = models.TextField()
    feedback_date = models.DateTimeField()
    student = models.ForeignKey(students, on_delete=models.CASCADE)

    def __int__(self):
        return self.feedback_id


class attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    attendance_markattendance = models.CharField(max_length=5)
    attendance_date = models.DateTimeField()
    student = models.ForeignKey(students, on_delete=models.CASCADE)

    def __int__(self):
        return self.attendance_id


class exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_markattendance = models.CharField(max_length=5)
    exam_date = models.DateTimeField()
    exam_marks = models.IntegerField()
    exam_subject = models.CharField(max_length=50)
    student_id = models.ForeignKey(students, on_delete=models.CASCADE)

    def __int__(self):
        return self.exam_id
