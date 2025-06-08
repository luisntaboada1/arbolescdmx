from django.shortcuts import render
from django.views import View
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse

def tree_registration(request):
    # retun a render that shows the tree registration success or failure
    form = treeForm()
    if request.method == 'POST':
        form = treeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'treecontrol1/tree_registration.html', {'form': form, 'success': True})
        else: 
            return render(request, 'treecontrol1/tree_registration.html', {'form': form, 'error': True})
    else:
        form = treeForm()
        return render(request, 'treecontrol1/tree_registration.html', {'form': form} )


def tree_index(request):
    #Si presionan algun boton
    if request.method == "GET": 
        trees = Trees.objects.all()
        return render(request, 'treecontrol1/tree-index.html', {'trees': trees})



@require_POST
def tree_delete(request, pk):
    tree = get_object_or_404(Trees, pk=pk)
    tree.delete()
    url = reverse('treecontrol1:tree-index')
    return HttpResponseRedirect(url)


def tree_edit(request, pk):
    tree = get_object_or_404(Trees, pk=pk)
    
    if request.method == 'POST':
        form = treeForm(request.POST, request.FILES, instance=tree)
        if form.is_valid():
            form.save()
            return redirect('tree-index/')
    else:
        form = treeForm(instance=tree)
    
    return render(request, 'treecontrol1/tree_edit.html', {'form': form})