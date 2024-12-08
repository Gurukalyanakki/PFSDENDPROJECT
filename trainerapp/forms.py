from django import forms
from .models import Course, CourseAssignment


class CourseForm(forms.ModelForm):
    employee_id = forms.CharField(max_length=20, label="Employee ID")

    class Meta:
        model = Course
        fields = ['name', 'description']

    def clean_employee_id(self):
        employee_id = self.cleaned_data['employee_id']
        if not Employee.objects.filter(id_number=employee_id).exists():
            raise forms.ValidationError("Employee ID does not exist.")
        return employee_id
