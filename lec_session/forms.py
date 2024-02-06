from django import forms
from .models import Lecture_Session

class Create_session(forms.ModelForm):

    class Meta:
        model = Lecture_Session
        fields = ['session_id','subject_name','stud_div','machine_id','branch']

    def __init__(self, *args, **kwargs):
        super(Create_session, self).__init__(*args, **kwargs)
        self.fields['session_id'].widget.attrs['placeholder'] = 'Enter session_id'
        self.fields['subject_name'].widget.attrs['placeholder'] = 'Enter subject_name'
        self.fields['stud_div'].widget.attrs['placeholder'] = 'Enter stud_div'
        self.fields['machine_id'].widget.attrs['placeholder'] = 'Enter machine_id'
        self.fields['branch'].widget.attrs['placeholder'] = 'Enter branch'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
