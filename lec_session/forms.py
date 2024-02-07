from django import forms
from .models import Lecture_Session

department=( 
    ("IT", "Information Technology"), 
    ("CO", "Computer Engineering"), 
    ("EXTC", "Electronics and telecommunication engineering"),
    ("ETRX", "Electronics Engineering"), 
    ("BIO", "Biomedical engineering"), 
) 

class Create_session(forms.ModelForm):

    year_of_admission = forms.IntegerField(label='Admission Year', required=False)
    branch=forms.ChoiceField(choices=department)

    class Meta:
        model = Lecture_Session
        fields = ['year_of_admission','subject_name','stud_div','branch']

    def __init__(self, *args, **kwargs):
        super(Create_session, self).__init__(*args, **kwargs)
        self.fields['year_of_admission'].widget.attrs['placeholder'] = 'Enter year_of_admission'
        self.fields['subject_name'].widget.attrs['placeholder'] = 'Enter subject_name'
        self.fields['stud_div'].widget.attrs['placeholder'] = 'Enter stud_div' 
        self.fields['branch'].widget.attrs['placeholder'] = 'Select branch'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
