from .models import User
from .serializer import ComplaintsSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Complaints

@api_view(['GET','POST'])
def complain(request, format=None):
    if request.method == 'GET':
        complaints = Complaints.objects.all()
        serializer = ComplaintsSerializer(complaints, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ComplaintsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status = status.HTTP_201_CREATED)
            complaints_data = serializer.data
            response_data = {
                'success': True,
                'details': complaints_data
            }
            return JsonResponse(response_data, status=201)
        else:
            # You can provide a more specific error message based on the validation errors
            return JsonResponse({'error': 'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@api_view(['GET','PUT','DELETE','POST'])
def complain_detail(request, id, format=None):

    try:
        complaints = Complaints.objects.get(pk=id)
    except Complaints.DoesNotExist:
        #To check is something is a valid request
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #Takes object in get
        serializer = ComplaintsSerializer(complaints)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ComplaintsSerializer(complaints, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        complaints.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        # Increment likes here
        complaints.likes += 1
        complaints.save()
        serializer = ComplaintsSerializer(complaints)
        return Response(serializer.data)