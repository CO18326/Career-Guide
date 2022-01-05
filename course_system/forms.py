from django import forms
from .models import CourseData

class CourseDataForm(forms.ModelForm):

    course_name = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "placeholder" : "Course Name", 
                "class" : "form-control"
            }
        )
    )

    course_json_file = forms.FileField(
        widget=forms.FileInput(
            attrs = {
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = CourseData
        fields = ('course_name', 'course_json_file', )
        