from django import forms
from .models import CourseData

class CourseDataForm(forms.ModelForm):
    class Meta:
        model = CourseData
        fields = ('course_name', 'course_json_file', )