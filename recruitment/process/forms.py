from django.forms import ModelForm
from process.models import Candidate_details
class TestForm(ModelForm):
    class Meta:
        model=Candidate_details
from process.models import Vacancy
class Test(ModelForm):
    class Meta:
        model=Vacancy
from process.models import Asses_step
class Testass(ModelForm):
    class Meta:
        model=Asses_step

from process.models import Panel
class Testpa(ModelForm):
    class Meta:
        model=Panel
from process.models import Flow
class Testflow(ModelForm):
    class Meta:
        model=Flow
from process.models import Flowstep
class Testflowstep(ModelForm):
    class Meta:
        model=Flowstep
from process.models import Recruit
class Testrecruitment(ModelForm):
    class Meta:
        model=Recruit
from process.models import Cand_asses
class Testcass(ModelForm):
    class Meta:
        model=Cand_asses
from process.models import Asses_template
class Testassestem(ModelForm):
    class Meta:
        model=Asses_template


