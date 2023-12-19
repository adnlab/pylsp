# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assessee(models.Model):
    id = models.OneToOneField('User', models.DO_NOTHING, db_column='id', primary_key=True)
    role = models.CharField(max_length=1)
    certificate = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessee'


class AssesseeForm(models.Model):
    id = models.IntegerField(primary_key=True)
    schedule = models.ForeignKey('Schedule', models.DO_NOTHING)
    template = models.ForeignKey('FormTemplate', models.DO_NOTHING)
    form = models.JSONField()

    class Meta:
        managed = False
        db_table = 'assessee_form'


class Assessor(models.Model):
    id = models.OneToOneField('User', models.DO_NOTHING, db_column='id', primary_key=True)
    role = models.CharField(max_length=1)
    supervisor = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessor'


class FormTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    unit = models.ForeignKey('Unit', models.DO_NOTHING)
    form = models.JSONField()

    class Meta:
        managed = False
        db_table = 'form_template'


class Schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    schema = models.ForeignKey('Schema', models.DO_NOTHING)
    test_agency = models.ForeignKey('TestingAgency', models.DO_NOTHING)
    assessee = models.ForeignKey(Assessee, models.DO_NOTHING)
    assessor = models.ForeignKey(Assessor, models.DO_NOTHING)
    certification_date = models.DateField(blank=True, null=True)
    graduation_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class Schema(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    title = models.CharField()

    class Meta:
        managed = False
        db_table = 'schema'


class TestingAgency(models.Model):
    id = models.OneToOneField('User', models.DO_NOTHING, db_column='id', primary_key=True)
    role = models.CharField(max_length=1)
    address = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_agency'


class Unit(models.Model):
    id = models.IntegerField(primary_key=True)
    schema = models.ForeignKey(Schema, models.DO_NOTHING)
    unit_name = models.CharField()
    unit_description = models.CharField()
    standarization = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit'


class User(models.Model):
    fullname = models.CharField(max_length=64)
    email = models.CharField(unique=True, max_length=319)
    password = models.CharField()
    role = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('id', 'role'),)
