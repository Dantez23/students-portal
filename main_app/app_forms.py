from django import forms

from main_app.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "dob": forms.DateInput(attrs={"min": "1990-01-01", "max": "1999-12-31", "type": "date"}),
            "kcpe_score": forms.NumberInput(attrs={"max": 500, "min": 0})
        }


# how to add radio field django ModelForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
