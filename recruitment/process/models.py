from django.db import models

class Vacancy(models.Model):
    Vacancy_id=models.CharField(primary_key=True,max_length=10)
    Role=models.CharField(max_length=20)
    No_positions=models.IntegerField(max_length=2)

class Candidate_details(models.Model):
    cho=['B.tech','mba']
    #from process.models import Vacancy
    #s=Vacancy.objects.all()
    Name=models.CharField(max_length=20)
    Candidate_id=models.CharField(primary_key=True,max_length=30)
    Age=models.IntegerField(max_length=2)
    Mobile=models.IntegerField(max_length=10)
    Mail=models.EmailField(max_length=30)
    Applied_date=models.DateField()
    Vacant_id=models.ForeignKey(Vacancy)
    Education=models.CharField(max_length=20,choices=[(item,item) for item in cho])
    Experience=models.IntegerField(max_length=2)
    
class Employer(models.Model):
    Emp_name=models.CharField(max_length=20)
    Emp_id=models.CharField(primary_key=True,max_length=20)
    Department=models.CharField(max_length=10)
    #Candidate_id=models.CharField(max_length=10)
    Role=models.CharField(max_length=10)
    Date_join=models.DateField()
    Salary=models.IntegerField(max_length=8)
    #Vacancy_id=models.CharField(max_length=10)

class Flow(models.Model):
    Flow_id=models.CharField(primary_key=True,max_length=10)
    Description=models.CharField(max_length=100)
    Active=models.CharField(max_length=10)

class Panel(models.Model):
    Panel_id=models.CharField(primary_key=True,max_length=10)
    Vacancy_id=models.ForeignKey(Vacancy)
    Start_date=models.DateField()
    End_date=models.DateField()
    Flow_id=models.ForeignKey(Flow)
    Emp_id=models.ForeignKey(Employer)

class Application(models.Model):
    Candidate_id=models.CharField(max_length=30)
    Vacant_id=models.ForeignKey(Vacancy)
    Applied_date=models.DateField()

class Flowstep(models.Model):
    Flow_id=models.ForeignKey(Flow)
    Flow_step=models.CharField(max_length=10)
    Panel_id=models.ForeignKey(Panel)

class Recruit(models.Model):
    Candidate_id=models.ForeignKey(Candidate_details)
    Flow_id=models.ForeignKey(Flow)
    Panel_id=models.ForeignKey(Panel)
    Date=models.DateField()
    Result=models.CharField(max_length=10)

class Cand_asses(models.Model):
    Candidate_id=models.ForeignKey(Candidate_details)
    #Recruit_id=models.CharField(max_length=10)
    Flow_id=models.ForeignKey(Flow)
    Asses_comment=models.CharField(max_length=30)
    Actual_value=models.FloatField(max_length=5)
    Panel_id=models.ForeignKey(Panel)

class Asses_template(models.Model):
    Asses_type=models.CharField(max_length=20)
    Flow_id=models.ForeignKey(Flow)
    state=models.CharField(max_length=10)

class Asses_step(models.Model):
    Flow_id=models.ForeignKey(Flow)
    Question=models.CharField(max_length=20)
    Answer=models.CharField(max_length=20)

class Result(models.Model):
    Candidate_id=models.ForeignKey(Candidate_details)
    Flow_id=models.ForeignKey(Flow)
    Result=models.CharField(max_length=10)

class Role(models.Model):
    Role=models.CharField(max_length=10)
    Role_description=models.CharField(max_length=30)

class Panel_members(models.Model):
    Panel_id=models.CharField(max_length=10)
    Emp_id=models.ForeignKey(Employer)

