from django.shortcuts import render
from .models import AppVariaty
from django.shortcuts import get_object_or_404

# Create your views here.

def all_app(request):
  apps = AppVariaty.objects.all()
  return render(request, 'app/all_app.html', {'apps': apps})


def app_detail(request, app_id):
  app = get_object_or_404(AppVariaty, pk=app_id)
  return render(request, 'app/app_detail.html', {'app': app})
