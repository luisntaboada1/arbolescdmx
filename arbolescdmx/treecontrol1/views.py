from django.shortcuts import render
from django.views import View
from .forms import *


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