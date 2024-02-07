from django import forms
from .models import Student
from django.core.validators import MinLengthValidator, MaxLengthValidator

department=( 
    ("IT", "Information Technology"), 
    ("CO", "Computer Engineering"), 
    ("EXTC", "Electronics and telecommunication engineering"),
    ("ETRX", "Electronics Engineering"), 
    ("BIO", "Biomedical engineering"), 
) 

class EnrollStudentForm(forms.ModelForm):
   
    # stud_phone = forms.CharField(max_length=10)
    branch=forms.ChoiceField(choices=department) 
    class Meta:
        model = Student
        fields = ['stud_roll_no','stud_name','stud_phone','stud_email','year_of_admission','stud_div','branch','finger_id','stud_profile']
       #fields = ['stud_roll_no', 'stud_name', 'stud_phone', 'stud_email', 'stud_div','branch','finger_id','year_of_admission']

    def __init__(self, *args, **kwargs):
        super(EnrollStudentForm, self).__init__(*args, **kwargs)
        self.fields['stud_roll_no'].widget.attrs['placeholder'] = 'Enter Roll number'
        self.fields['stud_name'].widget.attrs['placeholder'] = 'Enter Student Name'
        self.fields['stud_phone'].widget.attrs['placeholder'] = 'Enter Phone number'
        self.fields['stud_email'].widget.attrs['placeholder'] = 'Enter Student Email'
        self.fields['year_of_admission'].widget.attrs['placeholder'] = 'Enter Admission year'
        self.fields['stud_div'].widget.attrs['placeholder'] = 'Enter Student Division'
        self.fields['branch'].widget.attrs['placeholder'] = 'Select Branch'
        self.fields['finger_id'].widget.attrs['placeholder'] = 'Enter Finger Id'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class EditStudentForm(forms.ModelForm):
    
    # stud_phone = forms.CharField(max_length=10)
    class Meta:
        model = Student
        fields = ['stud_roll_no','stud_name','stud_phone','stud_email','year_of_admission','stud_div','branch','finger_id','stud_profile']
       #fields = ['stud_roll_no', 'stud_name', 'stud_phone', 'stud_email', 'stud_div','branch','finger_id','year_of_admission']

    def __init__(self, *args, **kwargs):
        super(EnrollStudentForm, self).__init__(*args, **kwargs)
        self.fields['stud_roll_no'].widget.attrs['placeholder'] = 'Enter Roll number'
        self.fields['stud_name'].widget.attrs['placeholder'] = 'Enter Student Name'
        self.fields['stud_phone'].widget.attrs['placeholder'] = 'Enter Phone number'
        self.fields['stud_email'].widget.attrs['placeholder'] = 'Enter Student Email'
        self.fields['year_of_admission'].widget.attrs['placeholder'] = 'Enter Admission year'
        self.fields['stud_div'].widget.attrs['placeholder'] = 'Enter Student Division'
        self.fields['branch'].widget.attrs['placeholder'] = 'Select Branch'
        self.fields['finger_id'].widget.attrs['placeholder'] = 'Enter Finger Id'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

