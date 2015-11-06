from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=100)
	period = models.ForeignKey('Period', blank=True, null=True)
	professors = models.ManyToManyField('Prof', blank=True)
	term = models.ForeignKey('Term', blank=True, null=True)
	dept = models.ForeignKey('Dept', null=True, blank=True)
	number = models.CharField(max_length=100, blank=True, null=True)
	section = models.CharField(max_length=100, blank=True, null=True)
	CRN = models.CharField(max_length=10, blank=True, unique=True)
	limit = models.CharField(max_length=100, default="-")
	enrollment = models.CharField(max_length=100, default="-")
	building = models.CharField(max_length=100, blank=True, null=True)
	room = models.CharField(max_length=100, blank=True, null=True)
	distribs = models.ManyToManyField('Distrib', blank=True)
	WC = models.ForeignKey('WC', blank=True, null=True)
	description = models.CharField(max_length=1000, blank=True)

	def __str__(self):
		return self.name

class Prof(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	fullname = models.CharField(max_length=50, blank=True, unique=True)
	dept = models.ForeignKey('Dept', null=True, blank=True)

	def __str__(self):
		return self.fullname

class Dept(models.Model):
	name = models.CharField(max_length=100, unique=True)
	abbrv = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.name

class Term(models.Model):
	name = models.CharField(max_length=50, unique=True)
	abbrv = models.CharField(max_length=3, unique=True)

	def __str__(self):
		return self.name

class Period(models.Model):
	name = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.name

class Distrib(models.Model):
	name = models.CharField(max_length=50, unique=True)
	abbrv = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.name

class WC(models.Model):
	name = models.CharField(max_length=50, unique=True)
	abbrv = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.name