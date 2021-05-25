from django.shortcuts import render
from .models import Card
import json
from rest_framework import response, status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def postRequest(request):
    requestContent = json.loads(request.body)
    try:
        cardName = requestContent['name']
        cardStatus = requestContent['status']
        cardContent = requestContent['content']
        cardCategory = requestContent['category']
        cardAuthor = requestContent['author']
    except KeyError:
        return response.Response({'error': 'Invalid JSON input'}, status=status.HTTP_400_BAD_REQUEST)
    card = Card.objects.create(name = cardName, status = cardStatus, content = cardContent, category = cardCategory, author = cardAuthor)
    card.save()
    return response.Response(data='Create card successful', status=status.HTTP_200_OK)

@api_view(['PUT'])
def updateRequest(request, blog_id):
    requestContent = json.loads(request.body)
    try:
        cardName = requestContent['name']
        cardStatus = requestContent['status']
        cardContent = requestContent['content']
        cardCategory = requestContent['category']
        cardAuthor = requestContent['author']
    except KeyError:
        return response.Response({'error': 'Invalid JSON input'}, status=status.HTTP_400_BAD_REQUEST)
    updateCard = Card.objects.get(pk=blog_id)
    if updateCard.author == cardAuthor:
        updateCard.name = cardName
        updateCard.status = cardStatus
        updateCard.content = cardContent
        updateCard.category = cardCategory
        updateCard.save()
        return response.Response(data='Update card successful', status=status.HTTP_200_OK)
    else:
        return response.Response({'error': 'Not an authorized author'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
def deleteRequest(request, blog_id):
    requestContent = json.loads(request.body)
    try:
        cardName = requestContent['name']
        cardAuthor = requestContent['author']
    except KeyError:
        return response.Response({'error': 'Invalid JSON input'}, status=status.HTTP_400_BAD_REQUEST)
    deleteCard = Card.objects.get(pk=blog_id)
    if deleteCard.author == cardAuthor:
        deleteCard.delete()
        return response.Response(data='Delete card successful', status=status.HTTP_200_OK)
    else:
        return response.Response({'error': 'Not an authorized author'}, status=status.HTTP_401_UNAUTHORIZED)
