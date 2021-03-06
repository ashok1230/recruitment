from django.http import HttpResponse,HttpResponseRedirect
from advt.models import details
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.base import TemplateView
from advt.forms import *
class advt(TemplateView):
    template_view='advt.html'
    def get(self, request):
        #s=detail.objects.all()
        return render_to_response('advt.html',locals(),context_instance=RequestContext(request))

class Add(TemplateView):
    template_view='add.html'
    def get(self,request):
         form=TestForm()
         return render_to_response('add.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=TestForm(request.POST)
        if form.is_valid():
             name = form.cleaned_data['Applicant_name']
             mail = form.cleaned_data['Applicant_mail']
             channel=form.cleaned_data['Applicant_channel']
             birth=form.cleaned_data['Date_of_birth']
             mobile=form.cleaned_data['Mobile_number']
             gaps=form.cleaned_data['year_gaps']
	     SSC=form.cleaned_data['SSC_percentage']
	     inter=form.cleaned_data['Inter_or_equi_percentage']
	     Graduation=form.cleaned_data['Graduation_percentage']
	     Year=form.cleaned_data['Year_passedout']
             details.objects.create(Applicant_name=name,Applicant_mail=mail,Applicant_channel=channel,Date_of_birth=birth,Mobile_number=mobile,
			year_gaps=gaps,SSC_percentage=SSC,Inter_or_equi_percentage=inter,Graduation_percentage=Graduation,Year_passedout=Year)
             HttpResponseRedirect('/success/')
        else:
             return HttpResponseRedirect('/error/')
        return HttpResponseRedirect('/success/')

class error(TemplateView):
    def get(self,request):
        return render(request,'error.html')
class success(TemplateView):
    def get(self,request):
        return render(request,'success.html')




