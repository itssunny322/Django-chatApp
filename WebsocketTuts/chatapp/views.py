from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


from .serializers import UserSerializer, ThreadSerializer, ChatMessageSerializer
from .models import User
# Create your views here.


@api_view(['GET'])
@permission_classes((AllowAny,))
def getchat(request):
    if request.method == 'GET':
        serializer_class = ChatMessageSerializer
        data = request.query_params
        user = request.user
        user_to = User.objects.get(id=user_id)
        thread = Thread.objects.filter(Q(user_from=user, user_to=user_to) | Q(user_from=user_to, user_to=user)).first()
        if thread:
            messages = ChatMessage.objects.filter(thread=thread)
            serializer = ChatMessageSerializer(messages, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response({'message': 'No messages found'}, status=HTTP_200_OK)
    return Response({'message': 'Invalid request'}, status=HTTP_400_BAD_REQUEST)


# Ignore the code below,its for MVT not for API


def home(request):
    if request.user.is_authenticated:
        users = User.objects.exclude(id=request.user.id)
        return render(request, 'home.html', {'users': users})
    else:
        return redirect('login_web')
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('home')
    return render(request, 'register.html')


def login_web(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user)
            return redirect('home')
        else:
            print('Invalid username or password')
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })


def personal(request, user_id):
    return render(request, 'personal.html', {
        'user_id': user_id
    })




