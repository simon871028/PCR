from django.shortcuts import get_object_or_404, render
from .models import Character
from django.http import Http404
from django.http import HttpResponse



def index(request):
    latest_character_list = Character.objects.order_by('pk')
    context = {'latest_character_list': latest_character_list}
    return render(request, 'gantt/index.html', context) 


def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'gantt/detail.html', {'character': character})