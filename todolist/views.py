
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from .models import Todo
from .forms import PostForm

def index(request):
    todos=Todo.objects.all().order_by('-prioridad')

    cantidad=Todo.objects.count()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.prioridad=cantidad
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    context={
            'todos':todos,
            'form': form
        }

    return  render(request,'index.html',context)



def eliminar_actividad(request, activa):
    act = Todo.objects.get(actividad=activa)
    todos=Todo.objects.all()
    cantidad= todos.count()
    for act1 in todos:
        if act1.prioridad>act.prioridad:
            act1.prioridad=act1.prioridad-1
            act1.save()

    act.delete()
    return HttpResponseRedirect("/")

def subir_actividad(request,activa):
    act=Todo.objects.get(actividad=activa)
    todos=Todo.objects.all()
    cantidad=todos.count()
    if act.prioridad<cantidad-1:
        actmayor=Todo.objects.get(prioridad=act.prioridad+1)
        actmayor.prioridad=actmayor.prioridad-1
        act.prioridad=act.prioridad+1
        act.save()
        actmayor.save()
    return HttpResponseRedirect("/")

def bajar_actividad(request, activa):
    act = Todo.objects.get(actividad=activa)
    todos = Todo.objects.all()
    if act.prioridad > 0:
        actmenor = Todo.objects.get(prioridad=act.prioridad - 1)
        actmenor.prioridad = actmenor.prioridad + 1
        act.prioridad = act.prioridad - 1
        act.save()
        actmenor.save()
    return HttpResponseRedirect("/")