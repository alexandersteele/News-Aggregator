from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .models import NewsStory, Author, User
from .serializers import StorySerializer
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

class StoryView(viewsets.ModelViewSet):
    queryset = NewsStory.objects.all()
    serializer_class = StorySerializer

@csrf_exempt
def user_login(request):

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if (user is not None):
            login(request, user)
            if (user.is_authenticated):

                return HttpResponse("Welcome " + username, status=200, content_type="text/plain")
            else:
                return HttpResponse("Failed authentication", status=400, content_type="text/plain")
        else:
            return HttpResponse("User not found", status=400, content_type="text/plain")

@csrf_exempt
def user_logout(request):
    if (request.method == 'POST'):
        return HttpResponse("Goodbye", status=200, content_type="text/plain")
    else:
        return HttpResponse("Error logging out", status=400, content_type="text/plain")

@csrf_exempt
def post_story(request):

    if (request.method == 'POST'):

        headline = request.POST.get('headline')
        category = request.POST.get('category')
        region = request.POST.get('region')
        details = request.POST.get('details')

        if (request.user.is_authenticated):
            
            user = User.objects.get(username=request.user)
            author = Author.objects.get(user = user)

            story = NewsStory(author=author, headline=headline, category=category, region=region, details=details)
            story.save()
            return HttpResponse("Success", status=201, content_type="text/plain")
        else:
            return HttpResponse("Story could not be created", status=503, content_type="text/plain")

@csrf_exempt
def delete_story (request):
    if (request.method == 'POST'):

        id = request.POST.get('id')

        if (request.user.is_authenticated):
            story = NewsStory.objects.get(id=id)
            story.delete()
            return HttpResponse("Story deleted", status=201, content_type="text/plain")
        else:
            return HttpResponse("Story could not be deleted", status=503, content_type="text/plain")    


@csrf_exempt
def get_stories(request):
    if (request.method == 'GET'):
        category = request.GET.get('category')
        region = request.GET.get('region')
        date = request.GET.get('date')

        stories = NewsStory.objects.all()

        if (category != "*"):
            stories = stories.filter(category=category)
        if (region != "*"):
            stories = stories.filter(region=region)
        if (date != "*"):
            stories = stories.filter(date=date) 

        if (stories):
            serializer = StorySerializer(stories, many=True)
            output = json.dumps(serializer.data)
            return HttpResponse(output, status=200, content_type="application/json")
        else:
            return HttpResponse("No results found", status=404, content_type="text/plain")