# importing the libraries
from django import forms            # form is needed for model data input
from .models import PatientData     # get our PatientData model

# Defining the form for value entry
class PatientDataForm(forms.ModelForm):
    class Meta:
        model = PatientData
        fields = ['age', 'mean_hr', 'mean_sys_pr', 'mean_temp',
                  'sepsis', 'any_org_fail', 'cardio_dys', 'resp_dys'
                  ]

    # Defining valid value limits
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 18 or age > 90):
            raise forms.ValidationError("Please enter a valid value for Age")
        return age

    def clean_mean_hr(self):
        mean_hr = self.cleaned_data.get('mean_hr')
        if mean_hr is not None and (mean_hr < 38 or mean_hr > 155):
            raise forms.ValidationError("Please enter a valid value for Mean Heart Rate")
        return mean_hr

    def clean_mean_sys_pr(self):
        mean_sys_pr = self.cleaned_data.get('mean_sys_pr')
        if mean_sys_pr is not None and (mean_sys_pr < 29 or mean_sys_pr > 216):
            raise forms.ValidationError("Please enter a valid value for Mean Systolic Pressure")
        return mean_sys_pr

    def clean_mean_temp(self):
        mean_temp = self.cleaned_data.get('mean_temp')
        if mean_temp is not None and (mean_temp < 30 or mean_temp > 41):
            raise forms.ValidationError("Please enter a valid value for Mean Temperature")
        return mean_temp
