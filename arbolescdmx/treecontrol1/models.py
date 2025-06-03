# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HealthStatuses(models.Model):
    tree = models.ForeignKey('Trees', models.DO_NOTHING)
    condition = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'health_statuses'


class NecessaryActions(models.Model):
    tree = models.ForeignKey('Trees', models.DO_NOTHING)
    action_description = models.CharField(max_length=255)
    urgency = models.IntegerField()
    cause_description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'necessary_actions'


class TreePhotos(models.Model):
    id = models.BigAutoField(primary_key=True)
    tree = models.ForeignKey('Trees', models.DO_NOTHING)
    photo = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'tree_photos'


class TreeSpecies(models.Model):
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tree_species'


class Trees(models.Model):
    id = models.BigAutoField(primary_key=True)
    species = models.ForeignKey(TreeSpecies, models.DO_NOTHING, db_column='species')
    alcaldia = models.CharField(max_length=350)
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


class TrunkStructures(models.Model):
    structure_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'trunk_structures'