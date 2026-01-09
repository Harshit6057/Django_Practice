from django.shortcuts import render
from .models import AppVariaty , Store
from django.shortcuts import get_object_or_404
from .forms import AppVariatyForm
# Create your views here.

def all_app(request):
  apps = AppVariaty.objects.all()
  return render(request, 'app/all_app.html', {'apps': apps})


def app_detail(request, app_id):
  app = get_object_or_404(AppVariaty, pk=app_id)
  return render(request, 'app/app_detail.html', {'app': app})


def app_store(request):
  stores = None
  if request.method == 'POST':
    form = AppVariatyForm(request.POST)
    if form.is_valid():
      app_variety = form.cleaned_data['app_variety_name']
      stores = Store.objects.filter(chai_varieties=app_variety)
      
  else:
    form = AppVariatyForm()
  return render(request, 'app/app_store.html', {'stores' : stores,'form': form})

