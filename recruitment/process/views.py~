from django.http import HttpResponse,HttpResponseRedirect
from process.models import Candidate_details,Application,Panel_members
from process.models import Vacancy,Employer,Flow,Recruit,Result
from process.models import Cand_asses
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.base import TemplateView
from process.forms import *

class home(TemplateView):
    template_view='home.html'
    def get(self,request):
         return render_to_response('home.html',locals(),context_instance=RequestContext(request))
class Add(TemplateView):
    template_view='add.html'
    def get(self,request):
         form=TestForm()
         return render_to_response('add.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=TestForm(request.POST)
        if form.is_valid():
             name = form.cleaned_data['Name']
             mail = form.cleaned_data['Mail']
             Id=form.cleaned_data['Candidate_id']
	     age=form.cleaned_data['Age']
 	     mobile=form.cleaned_data['Mobile']
 	     education=form.cleaned_data['Education']
	     Vacant=form.cleaned_data['Vacant_id']
	     experience=form.cleaned_data['Experience']
	     date=form.cleaned_data['Applied_date']
             Candidate_details.objects.create(Name=name,Mail=mail,Candidate_id=Id,Age=age,Mobile=mobile,Education=education,Experience=experience,Applied_date=date,Vacant_id=Vacant)
	     Application.objects.create(Candidate_id=Id,Vacant_id=Vacant,Applied_date=date)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')
class Candidate_detail(TemplateView):
    template_view='Candidate_details.html'
    def get(self, request):
        ss=Candidate_details.objects.all()
        return render_to_response('Candidate_details.html',locals(),context_instance=RequestContext(request))

class error(TemplateView):
    def get(self,request):
        return render(request,'error.html')
class success(TemplateView):
    def get(self,request):
        return render(request,'success.html')
class addvd(TemplateView):
    template_view='addvd.html'
    def get(self,request):
         form=Test()
         return render_to_response('addvd.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=Test(request.POST)
        if form.is_valid():
             name = form.cleaned_data['Vacancy_id']
             mail = form.cleaned_data['Role']
             Id=form.cleaned_data['No_positions']
             Vacancy.objects.create(Vacancy_id=name,Role=mail,No_positions=Id)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')
class Vacancy_details(TemplateView):
    template_view='Vacancy_details.html'
    def get(self, request):
        s=Vacancy.objects.all()
        return render_to_response('Vacancy_details.html',locals(),context_instance=RequestContext(request))

class Applications(TemplateView):
    template_view='application.html'
    def get(self, request):
	s=Vacancy.objects.all()
        ss=Candidate_details.objects.all()
        return render_to_response('application.html',locals(),context_instance=RequestContext(request))

class addass(TemplateView):
    template_view='addas.html'
    def get(self,request):
         form=Testass()
         return render_to_response('addas.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=Testass(request.POST)
        if form.is_valid():
             Id = form.cleaned_data['Flow_id']
             question = form.cleaned_data['Question']
             answer=form.cleaned_data['Answer']
             Asses_step.objects.create(Flow_id=Id,Question=question,Answer=answer)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')

class Asses_details(TemplateView):
    template_view='asses.html'
    def get(self, request):
	s=Asses_step.objects.all()
        return render_to_response('asses.html',locals(),context_instance=RequestContext(request))

class addpanel(TemplateView):
    template_view='panel.html'
    def get(self,request):
         form=Testpa()
         return render_to_response('panel.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=Testpa(request.POST)
        if form.is_valid():
             Id = form.cleaned_data['Panel_id']
             Vid = form.cleaned_data['Vacancy_id']
             sdate=form.cleaned_data['Start_date']
	     edate=form.cleaned_data['End_date']
	     fid=form.cleaned_data['Flow_id']
	     Emp_id=form.cleaned_data['Emp_id']
             Panel.objects.create(Panel_id=Id,Vacancy_id=Vid,Start_date=sdate,End_date=edate,Flow_id=fid,Emp_id=Emp_id)
	     Panel_members.objects.create(Panel_id=Id,Emp_id=Emp_id)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')

class Panel_details(TemplateView):
    template_view='panel_details.html'
    def get(self, request):
	s=Panel.objects.all()
        return render_to_response('panel_details.html',locals(),context_instance=RequestContext(request))


class Employer_details(TemplateView):
    template_view='emp_details.html'
    def get(self, request):
	s=Employer.objects.all()
        return render_to_response('emp_details.html',locals(),context_instance=RequestContext(request))

class addflow(TemplateView):
    template_view='flow.html'
    def get(self,request):
         form=Testflow()
         return render_to_response('flow.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=Testflow(request.POST)
        if form.is_valid():
             Id = form.cleaned_data['Flow_id']
             des = form.cleaned_data['Description']
             active=form.cleaned_data['Active']
	     #result=form.cleaned_data['Result']
             Flow.objects.create(Flow_id=Id,Description=des,Active=active)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')

class Flow_details(TemplateView):
    template_view='flow_details.html'
    def get(self, request):
	s=Flow.objects.all()
        return render_to_response('flow_details.html',locals(),context_instance=RequestContext(request))

class addflowstep(TemplateView):
    template_view='flow_step.html'
    def get(self,request):
         form=Testflowstep()
         return render_to_response('flow_step.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=Testflowstep(request.POST)
        if form.is_valid():
             Id = form.cleaned_data['Flow_id']
             step=form.cleaned_data['Flow_step']
	     panel=form.cleaned_data['Panel_id']
             Flowstep.objects.create(Flow_id=Id,Flow_step=step,Panel_id=panel)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')

class recruitment(TemplateView):
    template_view='recruitment.html'
    def get(self,request):
         form=Testrecruitment()
         return render_to_response('recruitment.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=Testrecruitment(request.POST)
        if form.is_valid():
             Id = form.cleaned_data['Candidate_id']
             fid=form.cleaned_data['Flow_id']
	     date=form.cleaned_data['Date']
	     pid=form.cleaned_data['Panel_id']
   	     result=form.cleaned_data['Result']
             Recruit.objects.create(Candidate_id=Id,Flow_id=fid,Date=date,Result=result,Panel_id=pid)
	     Result.objects.create(Candidate_id=Id,Result=result,Flow_id=fid)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')

class Recruitment_details(TemplateView):
    template_view='recruitment_details.html'
    def get(self, request):
	s=Recruit.objects.all()
        return render_to_response('recruitment_details.html',locals(),context_instance=RequestContext(request))

class Results(TemplateView):
    template_view='result.html'
    def get(self, request):
	s=Result.objects.all()
        return render_to_response('result.html',locals(),context_instance=RequestContext(request))

class candasses(TemplateView):
    template_view='cand_asses.html'
    def get(self,request):
         form=Testcass()
         return render_to_response('cand_asses.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=Testcass(request.POST)
        if form.is_valid():
             Id = form.cleaned_data['Candidate_id']
             fid=form.cleaned_data['Flow_id']
	     comment=form.cleaned_data['Asses_comment']
	     value=form.cleaned_data['Actual_value']
	     Panel_id=form.cleaned_data['Panel_id']
             Cand_asses.objects.create(Candidate_id=Id,Flow_id=fid,Asses_comment=comment,Actual_value=value,Panel_id=Panel_id)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')

class casses_details(TemplateView):
    template_view='casse_details.html'
    def get(self, request):
	s=Cand_asses.objects.all()
        return render_to_response('casse_details.html',locals(),context_instance=RequestContext(request))

class assestemplates(TemplateView):
    template_view='assestemplate.html'
    def get(self,request):
         form=Testassestem()
         return render_to_response('assestemplate.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=Testassestem(request.POST)
        if form.is_valid():
             atype = form.cleaned_data['Asses_type']
             flow=form.cleaned_data['Flow_id']
	     state=form.cleaned_data['state']
             Asses_template.objects.create(Asses_type=atype,Flow_id=flow,state=state)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')

class assestemplate_details(TemplateView):
    template_view='Assesment_details.html'
    def get(self, request):
	s=Asses_template.objects.all()
        return render_to_response('Assesment_details.html',locals(),context_instance=RequestContext(request))

class panelmembers(TemplateView):
    template_view='panelmember_details.html'
    def get(self, request):
	s=Panel_members.objects.all()
        return render_to_response('panelmember_details.html',locals(),context_instance=RequestContext(request))

class Show(TemplateView):
    template_view='show.html'
    def get(self,request,id):
        s=Candidate_details.objects.get(Candidate_id=id)
        return render_to_response('show.html',locals(),context_instance=RequestContext(request))

class Show(TemplateView):
    template_view='show.html'
    def get(self,request,id):
        s=Candidate_details.objects.get(Candidate_id=id)
        return render_to_response('show.html',locals(),context_instance=RequestContext(request))

class Showemp(TemplateView):
    template_view='showemp.html'
    def get(self,request,id):
        s=Employer.objects.get(Emp_id=id)
        return render_to_response('showemp.html',locals(),context_instance=RequestContext(request))

