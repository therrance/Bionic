from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from coursera.models import Student
# Create your views here.
class ListStudentView(ListView):
    model = Student
    template_name = 'student_list.html'