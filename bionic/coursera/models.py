from django.db import models

# Create your models here.

class Group(models.Model):

   group = models.CharField(
       max_length=255,
   )

   def __str__(self):
       return self.group


class Student(models.Model):

    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    group = models.ForeignKey('Group')

    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])


