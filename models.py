# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
	id = models.IntegerField(primary_key=True)
	code = models.CharField(max_length=15, blank=True, null=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	language = models.CharField(max_length=10, blank=True, null=True)
	credit = models.IntegerField(blank=True, null=True)
	curriculumid = models.ForeignKey('Curriculum', models.DO_NOTHING, db_column='curriculumid')

	class Meta:
        # managed = False
		db_table = 'course'


class Curriculum(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
        #managed = False
		db_table = 'curriculum'


class Group(models.Model):
	id = models.IntegerField(primary_key=True)
	code = models.CharField(max_length=15, blank=True, null=True)
	student = models.IntegerField(blank=True, null=True)
	implementationid = models.ForeignKey('Implementation', models.DO_NOTHING, db_column='implementationid')

	class Meta:
        # managed = False
		db_table = 'group'


class Implementation(models.Model):
	id = models.IntegerField(primary_key=True)
	p1 = models.IntegerField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
	p2 = models.IntegerField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
	p3 = models.IntegerField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
	p4 = models.IntegerField(db_column='P4', blank=True, null=True)  # Field name made lowercase.
	p5 = models.IntegerField(db_column='P5', blank=True, null=True)  # Field name made lowercase.
	total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
	courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')

	class Meta:
        # managed = False
		db_table = 'implementation'


class Teacher(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40, blank=True, null=True)
	code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'teacher'


class TeacherImplementation(models.Model):
	id = models.IntegerField(primary_key=True)
	teacherid = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='teacherid', primary_key=True)
	implementationid = models.ForeignKey(Implementation, models.DO_NOTHING, db_column='implementationid')

	class Meta:
        # managed = False
		db_table = 'teacher_implementation'
		unique_together = (('teacherid', 'implementationid'),)
