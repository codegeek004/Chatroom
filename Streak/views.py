from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
	return render(request, 'index.html', {})

def room(request, room_name):
	return render(request, 'room.html', {'room_name':room_name})

# def enter_room(request):
# 	if request.method == 'POST':
# 		room_name = request.POST.get("room_name")
# 		if room_name:
# 			return redirect(reverse('chat_room', kwargs={'room_name': room_name}))
# 	return redirect('index')

# def chat_room(request, room_name):
# 	return render(request, chat_room.html, {'room_name': room_name})
