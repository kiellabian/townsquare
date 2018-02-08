from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.urls import reverse

from .models import Message


class LoginSignupView(TemplateView):
    template_name = 'login_signup.html'


class ChatView(TemplateView):
    template_name = 'chat.html'

    def post(self, request, **kwargs):
        message = Message.objects.create(content=request.POST['content'])
        return HttpResponse(message.content)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.order_by('when')
        context['action'] = reverse('chat')
        return context
