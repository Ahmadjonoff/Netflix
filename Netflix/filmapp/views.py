from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class Hello(APIView):
    def get(self, request):
        malumot = {'xabar' : 'Salom Dunyo!'}
        return Response(malumot)
    def post(self, request):
        d = {"xabar" : "Ma`lumotingiz qabul qilindi!"}
        return Response(d)

class ActorAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        malumot = ActorSerializer(actors, many=True)
        return Response(malumot.data)
    def post(self, request):
        ser = ActorSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        a = Actor.objects.get(id = pk)
        ser = ActorSerializer(a, request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)