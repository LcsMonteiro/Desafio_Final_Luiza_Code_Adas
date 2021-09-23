from django.http.response import HttpResponse, HttpResponseRedirect, ResponseHeaders
from django.shortcuts import redirect, render
from app.models import Segmentos, Marcas, Produtos
from app.forms import SegmentosForm, MarcasForm, ProdutosForm
from django.http import HttpResponseRedirect

'''
Funções para renderização do template
'''
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {'form': SegmentosForm()}
    return render(request, 'form.html', data)

def create(request):
    form = SegmentosForm(request.POST or None)
    form1 = MarcasForm(request.POST or None)
    form2 = ProdutosForm(request.POST or None)
    if form.is_valid() and form1.is_valid() and form2.is_valid():
        form.save()
        form1.save()
        form2.save()
        return HttpResponseRedirect("/")

def view(request, pk):
    data = {}
    data = {'db', Segmentos.objects.get(pk=pk)}
    return render(request, 'view.html, data')