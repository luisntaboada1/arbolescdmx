from django import forms
from .models import *

class treeForm(forms.ModelForm):
    class Meta:
        model = Trees
        exclude = ["id"]

class healthStatusForm(forms.ModelForm):
    class Meta:
        model = HealthStatuses
        fields = '__all__'

class actionsForm(forms.ModelForm):
    class Meta:
        model = NecessaryActions
        fields = '__all__'

class photoForm(forms.ModelForm):
    class Meta:
        model = TreePhotos
        fields = '__all__'

#Not meant to add new species
class speciesForm(forms.ModelForm):
    class Meta:
        model = TreeSpecies
        fields = '__all__'

#Not meant to add new structures
class structureForm(forms.ModelForm):
    class Meta:
        model = TrunkStructures
        fields = '__all__'