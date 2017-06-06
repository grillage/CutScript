from django.shortcuts import render, get_object_or_404, redirect
from .models import Design
from .forms import DesignForm

def drawing_list(request):
    designs = Design.objects.order_by('title')
    return render(request, 'draw/drawing_list.html', {'designs':designs})

def designer(request, pk):
    drawing = get_object_or_404(Design, pk=pk)
    if request.method == "POST":
        form = DesignForm(request.POST, instance=drawing)
        if form.is_valid():
            form.save()
    else:
        form = DesignForm(instance=drawing)
    return render(request, 'draw/designer.html', {'form': form})

def new_design(request):
    if request.method == "POST":
        form = DesignForm(request.POST)
        if form.is_valid():
            design = form.save()
            return redirect('designer', pk=design.pk)
    else:
        form = DesignForm()
    return render(request, 'draw/designer.html', {'form': form})

