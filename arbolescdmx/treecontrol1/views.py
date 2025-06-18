# imports
from django.shortcuts import render
from django.views import View
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse



##
def tree_registration(request):
    # in the future, this should retun a render that shows the tree registration success or failure
    if request.method == 'POST':
        form = treeForm(request.POST, request.FILES)
        pformset = photoFormSet(request.POST, request.FILES) 
        aform = actionsForm(request.POST, request.FILES)

        #If the tree form, the photos and the actions valid, save the tree
        if form.is_valid() and pformset.is_valid() and aform.is_valid():
            tree = form.save()
            pformset.instance = tree
            pformset.save()
            aform.instance = tree
            aform.save()

            #If theres actions registered, insert the tree instance and save them to their tables
            return render(request, 'treecontrol1/tree_registration.html', {'form': form, 'pformset':pformset, 'aform':aform ,'success': True})
        
        else: 
            return render(request, 'treecontrol1/tree_registration.html', {'form': form, 'pformset':pformset, 'aform':aform, 'error': True})
    
    else:
        form = treeForm()
        pformset = photoFormSet()
        aform = actionsForm()
        return render(request, 'treecontrol1/tree_registration.html', {'form': form, 'pformset':pformset, 'aform':aform} )



def tree_index(request):
    #Si presionan algun boton
    if request.method == "GET": 
        trees = Trees.objects.prefetch_related('photos').all()
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
        pformset = photoFormSet(request.POST, request.FILES, instance=tree)
        aform = actionsForm(request.POST, request.FILES, instance=tree)

        if form.is_valid() and pformset.is_valid() and aform.is_valid():
            form.save()
            pformset.save()
            aform.save()
            url = reverse('treecontrol1:tree-index')
            return HttpResponseRedirect(url)
    else:
        form = treeForm(instance=tree)
        pformset = photoFormSet(instance=tree)
        aform = actionsForm()
    
    return render(request, 'treecontrol1/tree_edit.html', {'form': form, 'pformset':pformset})