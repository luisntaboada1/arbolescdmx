from django import forms
from .models import *
from django.forms import inlineformset_factory, ClearableFileInput


class actionsForm(forms.ModelForm):
    action_description = forms.ChoiceField(
        choices = NecessaryActions.ACT_CHOICES,
        label='Seleccione una accion',
        widget=forms.Select(
            attrs={
                'class':'select_action'
            }
        )
    )

    urgency = forms.ChoiceField(
        choices = NecessaryActions.URGENCY_CHOICES,
        label='Seleccione la urgencia',
        widget=forms.Select(
            attrs={
                'class':'action_urgency'
            }
        )
    )

    cause_description = forms.ChoiceField(
        choices=NecessaryActions.DESC_CHOICES,
        label='Seleccione la causa o descripcion',
        widget=forms.Select(
            attrs={
                'class':'action_urgency'
            }
        )
    )

    class Meta:
        model = NecessaryActions
        fields = '__all__'



class photoForm(forms.ModelForm):
    class Meta:
        model  = TreePhoto
        fields = '__all__'
        widgets = {
            'image': ClearableFileInput(attrs={
                'class': 'input_foto', 
                'accept': 'image/*',
            }),
        }



photoFormSet = inlineformset_factory(
    parent_model=Trees, model=TreePhoto,
    form = photoForm,
    fields = ['image'],
    extra=4,
    max_num=5
) 



class treeForm(forms.ModelForm):
    
    species = forms.ModelChoiceField(
        queryset=TreeSpecies.objects.all(),
        empty_label='Seleccione una especie'
    )

    structure = forms.ModelChoiceField(
        queryset=TrunkStructures.objects.all(),
        empty_label='---Estructura del tronco---'
    )
    
    class Meta:
        model = Trees
        exclude = "__all__"
        widgets = {
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