from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    firstname=models.CharField(max_length=30,null=True)
    lastname=models.CharField(max_length=30,null=True)
    organisation = models.CharField(max_length=30,choices=[("Profesor", "Profesor"), ("Student", "Student")])
    semester = models.CharField(max_length=1,choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8',
    '8')],null=True)
    passout_year=models.IntegerField(null=True)
    placement_year=models.IntegerField(null=True)
    branch=models.CharField(max_length=30,choices=[("CSE", "CSE"), ("CIVIL", "CIVIL"),("ECE", "ECE"),("MECH", "MECH")],null=True)
    