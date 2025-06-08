from django import forms
from .models import *

class treeForm(forms.ModelForm):
    

    class Meta:
        model = Trees
        exclude = ["id"]
        widgets = {
            'species': forms.NumberInput(attrs={'class': 'species_selection'}),
            'alcaldia': forms.Select(attrs={'class': 'ialcaldia'}),
            'colonia': forms.TextInput(attrs={'class': 'icolonia', 'placeholder': 'Colonia'}), 
            'calle': forms.TextInput(attrs={'class': 'icalle', 'placeholder': 'Calle'}),
            'num': forms.TextInput(attrs={'class': 'inum', 'placeholder': 'Número'}),
            'cp': forms.TextInput(attrs={'class': 'icp', 'placeholder': 'C.P.'}),
            'latitude': forms.NumberInput(attrs={'class': 'ilatitude', 'placeholder': 'Latitud'}),
            'longitude': forms.NumberInput(attrs={'class': 'ilongitude', 'placeholder': 'Longitud'}),
            'reference': forms.TextInput(attrs={'class': 'ireference', 'placeholder': 'Referencias'}),
            'height': forms.NumberInput(attrs={'class': 'iheight', 'placeholder': 'Altura'}),
            'base_diameter': forms.NumberInput(attrs={'class': 'ibase_diameter', 'placeholder': 'Diámetro de base'}),
            'trunk_diameter': forms.NumberInput(attrs={'class': 'itrunk_diameter', 'placeholder': 'Diámetro del tronco'}),
            'crown_diameter': forms.NumberInput(attrs={'class': 'icrown_diameter', 'placeholder': 'Diámetro de la copa'}),
            'trunk_inclination': forms.NumberInput(attrs={'class': 'itrun_inclination', 'placeholder': 'Inclinación del tronco'}),
        }

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