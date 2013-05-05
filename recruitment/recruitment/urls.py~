from django.conf.urls import patterns, include, url
from process import views
from process.views import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',  home.as_view(),name='home'),
    url(r'add/$',  Add.as_view(),name='add'),
    url(r'^error/$', error.as_view(),name='error'),
    url(r'^success/$', success.as_view(),name='success'),
    url(r'^addvd/$', addvd.as_view(),name='addvd'),
    url(r'^Vacancy_details/$', Vacancy_details.as_view(),name='Vacancy_details'),
    url(r'^Candidate_details/$', Candidate_detail.as_view(),name='Candidate_details'),
    url(r'^application/$', Applications.as_view(),name='Applications'),
    url(r'^addas/$', addass.as_view(),name='addass'),
    url(r'^asses_details/$',Asses_details.as_view(),name='asses_detail'),
    url(r'^panel/$', addpanel.as_view(),name='panel'),
    url(r'^panel_details/$',Panel_details.as_view(),name='panel_details'),
    url(r'^emp_details/$',Employer_details.as_view(),name='emp_details'),
    url(r'flow/$',  addflow.as_view(),name='addflow'),
    url(r'^flow_details/$',Flow_details.as_view(),name='flow_details'),
    url(r'^flow_step/$',addflowstep.as_view(),name='flow_step'),
    url(r'^recruitment_details/$',Recruitment_details.as_view(),name='recruitment_details'),
    url(r'^recruitment/$',recruitment.as_view(),name='recruitment'),
    url(r'^result/$',Results.as_view(),name='result'),
    url(r'^cand_asses/$', candasses.as_view(),name='candasses'),
    url(r'^casse_details/$', casses_details.as_view(),name='casse_details'),
    url(r'^assestemplate/$', assestemplates.as_view(),name='asssestemplate'),
    url(r'^assesment_details/$', assestemplate_details.as_view(),name='assesment_details'),
    #url(r'^time/$', time.as_view(),name='time'),
    url(r'^panelmember/$', panelmembers.as_view(),name='panelmembers'),
    url(r'^show/(?P<id>\w+)/$', Show.as_view(),name='show'),
    url(r'^showemp/(?P<id>\w+)/$', Showemp.as_view(),name='show'),
)
