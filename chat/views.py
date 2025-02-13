from django.shortcuts import render, redirect
from .models import ChatMessage


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    
    messages = ChatMessage.objects.all()
    context = {"messages": messages}
    return render(request, "chat/chatPage.html", context)




