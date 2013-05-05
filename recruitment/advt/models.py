from django.db import models

class details(models.Model):
    Applicant_name=models.CharField(max_length=20)
    Applicant_mail=models.EmailField(max_length=30)
    Applicant_channel=models.CharField(max_length=20,default='refer or companysite or advt')
    Date_of_birth=models.DateField(default='/ separator')
    Mobile_number=models.IntegerField(max_length=10)
    year_gaps=models.IntegerField(max_length=2)
    SSC_percentage=models.FloatField(max_length=5)
    Inter_or_equi_percentage=models.FloatField(max_length=5)
    Graduation_percentage=models.FloatField(max_length=5)
    Year_passedout=models.CharField(max_length=10)
