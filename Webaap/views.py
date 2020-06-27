from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import student, More_Info, upadte_info
from .serializer import studentSerializer, More_InfoSerializer, upadteinfoSerializer


class studentList(APIView):

    def get(self, request):
        student1 = student.objects.all()
        serializer = studentSerializer(student1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class More_InfoList(APIView):

    def get(self, request):
        Info = More_Info.objects.all()
        serializer = More_InfoSerializer(Info, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class updte_infoList(APIView):
    def get(self, request):
        upinfo = upadte_info.objects.all()
        serializer = upadteinfoSerializer(upinfo, many=True)
        return Response(serializer.data)

# Create your views here.
