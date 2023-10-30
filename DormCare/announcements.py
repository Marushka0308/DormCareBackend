from .models import Announcements
from .serializer import AnnouncementsSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Announcements

@api_view(['GET','POST'])
def announcement(request, format=None):
    if request.method == 'GET':
        announcements = Announcements.objects.all()
        serializer = AnnouncementsSerializer(announcements, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AnnouncementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status = status.HTTP_201_CREATED)
            announcement_data = serializer.data
            response_data = {
                'success': True,
                'details': announcement_data
            }
            return JsonResponse(response_data, status=201)
        else:
            # You can provide a more specific error message based on the validation errors
            return JsonResponse({'error': 'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
