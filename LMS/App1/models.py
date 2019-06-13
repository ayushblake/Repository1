from django.db import models

# Create your models here.
class Database_1(models.Model):
    laptop_id=models.CharField(max_length=264,unique=True)
    person_id_id=models.CharField(max_length=264,unique=True)
    person_name=models.CharField(max_length=264,unique=True)
    issue_date=models.DateField()
    return_date=models.DateField()

    def __str__(self):
        return self.person_name
