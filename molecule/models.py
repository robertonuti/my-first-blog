from django.db import models


class Molecule(models.Model):
	name = models.CharField(max_length=150)
	#id_mol = models.ForeignKey('cod.id')
	struct = models.TextField()
	target = models.CharField(max_length=200)
	activity = models.FloatField(null=True, blank=True, default=None)

	def __str__(self):
		return self.name

	def show(self):
		print(self.name)
		print(self.id_mol)
		print(self.target)
		print(self.activity)
		self.save()
# Create your models here.
