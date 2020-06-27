from django.db import models


class student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.first_name


class More_Info(models.Model):
    Branch_name = models.CharField(max_length=10)
    Year = models.IntegerField()

    def __str__(self):
        return self.Branch_name


class upadte_info(models.Model):
    Student = models.OneToOneField(student, on_delete=models.CASCADE)
    info = models.OneToOneField(More_Info, on_delete=models.CASCADE)

    def __str__(self):
       return  self.Student

    def __str__(self):
        return self.info
    # Create your models here.
