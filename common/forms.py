from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UpcomingExams,ClassRoutine,Assignments,Announcements
from users.models import User, Student


class CommonRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["role",'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
    
        if not email:
            raise forms.ValidationError("Please provide either email or full ID.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['role'].label = 'Choose your role'

        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].label = 'Email'

        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].label = 'Password'

        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].label = 'Confirm Password'



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ['account']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'is_class_cr':                
                self.fields[field].widget.attrs.update({'class': 'mt-2 pe-2 '})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

            

class ClassRoutineForm(forms.ModelForm):
    class Meta:
        model = ClassRoutine
        fields = "__all__"
        exclude = ['intake','department','section']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

            

class AssignmentsForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ["types","course_code","course_title","date","assignment_title","detail",]
        exclude = ['intake','department','section']
        widgets = {
                    'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
                }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

            


class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = '__all__'
        exclude = ['intake','department','section', 'who_posted']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

            


class UpcomingExamsForm(forms.ModelForm):
    class Meta:
        model = UpcomingExams
        fields = "__all__"
        exclude = ['intake', 'department', 'section']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["exam_name"].widget.attrs.update({
            'class': 'form-control',
            
            'placeholder': self.fields["exam_name"].label if self.fields["exam_name"].label else '',
            })
        self.fields["course_name"].widget.attrs.update({
            'class': 'form-control',
            
            'placeholder': self.fields["course_name"].label if self.fields["course_name"].label else '',
            })
        self.fields["course_code"].widget.attrs.update({
            'class': 'form-control',
            
            'placeholder': self.fields["course_code"].label if self.fields["course_code"].label else '',
            })
        self.fields["date"].widget.attrs.update({
            'class': 'form-control datepicker',
            'id':"birthday",
            "placeholder":"dd mm yyyy",
            'placeholder': self.fields["date"].label if self.fields["date"].label else '',
            })
        self.fields["topic"].widget.attrs.update({
            'class': 'form-control',
            
            'placeholder': self.fields["topic"].label if self.fields["topic"].label else '',
            })
        self.fields["detail"].widget.attrs.update({
            'class': 'form-control',
            "id":"addResss",
            'placeholder': self.fields["detail"].label if self.fields["detail"].label else '',
            })