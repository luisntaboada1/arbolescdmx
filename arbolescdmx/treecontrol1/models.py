# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HealthStatuses(models.Model):
    tree = models.ForeignKey('Trees', on_delete=models.CASCADE, related_name='health_statuses')
    condition = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'health_statuses'


class NecessaryActions(models.Model):
    ACT_CHOICES = [
        ('podar', 'Podar'),
        ('talar', 'Talar'),
        ('desinfectar', 'Desinfectar'),
        ('transplantar', 'Transplantar'),
        ('otro', 'Otro')
    ]

    DESC_CHOICES = [
        ('obstruccion', 'Obstruccion de propiedad'),
        ('riesgo de caida', 'Riesgo de caida'),
        ('plagas', 'Plagas'),
        ('otro', 'Otro')
    ]

    URGENCY_CHOICES = [
        (1,'Muy Baja'),
        (2,'Moderada'),
        (3,'Alta'),
        (4,'Muy Alta')
    ]

    tree = models.ForeignKey('Trees', on_delete=models.CASCADE, related_name='necessary_actions')
    action_description = models.CharField(max_length=255, choices=ACT_CHOICES)
    urgency = models.IntegerField()
    cause_description = models.CharField(max_length=255, choices=DESC_CHOICES)

    class Meta:
        managed = False
        db_table = 'necessary_actions'



class TreeSpecies(models.Model):
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tree_species'

    def __str__(self):
        return self.common_name


class Trees(models.Model):
    ALCALDIA_CHOICES = [
        ('alvaro_obregon', 'Alvaro Obregon'),
        ('azcapotzalco', 'Azcapotzalco'),
        ('benito_juarez', 'Benito Juarez'),
        ('coyoacan', 'Coyoacan'),
        ('cuajimalpa_de_morelos', 'Cuajimalpa de Morelos'),
        ('cuauhtemoc', 'Cuauhtemoc'),
        ('gustavo_a_madero', 'Gustavo A. Madero'),
        ('iztapalapa', 'Iztapalapa'),
        ('la_magdalena_contreras', 'La Magdalena Contreras'),
        ('miguel_hidalgo', 'Miguel Hidalgo'),
        ('milpa_alta', 'Milpa Alta'),
        ('tlahuac', 'Tlahuac'),
        ('tlalpan', 'Tlalpan'),
        ('xochimilco', 'Xochimilco'),
        ('venustiano_carranza', 'Venustiano Carranza')
    ]
    
    id = models.BigAutoField(primary_key=True)
    species = models.ForeignKey(TreeSpecies, models.DO_NOTHING, db_column='species')
    alcaldia = models.CharField(max_length=350, choices=ALCALDIA_CHOICES)
    colonia = models.CharField(max_length=350)
    calle = models.CharField(max_length=500)
    num = models.CharField(max_length=10)
    cp = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    reference = models.CharField(max_length=500, blank=True, null=True)
    height = models.FloatField()
    base_diameter = models.FloatField()
    trunk_diameter = models.FloatField()
    crown_diameter = models.FloatField()
    trunk_inclination = models.FloatField()
    structure = models.ForeignKey('TrunkStructures', models.DO_NOTHING, db_column='structure')
    health_status = models.IntegerField()
    last_inspection = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trees'




class TreePhoto(models.Model):
    tree  = models.ForeignKey(
        Trees,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    image = models.ImageField(upload_to='tree_photos/')

    def __str__(self):
        return f"Photo #{self.pk} of {self.tree}"
    




class TrunkStructures(models.Model):
    structure_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'trunk_structures'

    def __str__(self):
        return self.structure_type