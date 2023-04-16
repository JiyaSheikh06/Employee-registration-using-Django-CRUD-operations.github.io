from django import forms
from .models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model= Employee
        # fields='__all__'
        fields= ('fullname','mobile','emp_code','position')
        labels={
            'fullname':'Full name',
            'emp_code':'EMP. code'

        }
    def __init__(self,*args,**kwargs):
        super(Employeeform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['emp_code'].required=False