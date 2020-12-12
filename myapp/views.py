from django.shortcuts import render

def index(request):
  context = {
    'name': 'sawaking',
  }
  return render(request, 'myapp/index.html', context)