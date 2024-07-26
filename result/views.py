from django.shortcuts import render, redirect

from .models import PatientData
# import the 'PatientData' class from models.py

from .forms import PatientDataForm

def predictor(request):
    form = PatientDataForm()
    return render(request,'home.html', {'form': form})

# Define result view function here
def result(request):
    prediction_outcome = None
    prediction_prob = None
    # # post method, user submitting data
    if request.method == 'POST':
        form = PatientDataForm(request.POST) # creates instance called PatientDataForm upon submission
        if form.is_valid():
            new_patient_data = form.save(commit=False)
            prediction_outcome, prediction_prob = new_patient_data.predict_outcome()
            new_patient_data.save()
        else:
            return render(request, 'home.html', {'form': form})

    # Retrieve all patient data from the database
    all_patients = PatientData.objects.all()

# Outcome Calculations
    # Calculate the number of alive and dead patients
    total_patients = all_patients.count()
    alive_patients = all_patients.filter(outcome='live').count()
    dead_patients = all_patients.filter(outcome='die').count()
    # Calculate the percentages
    alive_percentage = (alive_patients / total_patients) * 100
    dead_percentage = (dead_patients / total_patients) * 100

# other binary variables
    sepsis_percentage = (all_patients.filter(sepsis = True).count() / total_patients) * 100
    any_org_fail_percentage = (all_patients.filter(any_org_fail = True).count() / all_patients.count()) * 100
    cardio_dys_percentage = (all_patients.filter(cardio_dys = True).count() / all_patients.count()) * 100
    resp_dys_percentage = (all_patients.filter(resp_dys = True).count() / all_patients.count()) * 100

# other numeric variables
    age_dp = [patient.age for patient in all_patients]
    hr_dp = [patient.mean_hr for patient in all_patients]

    # displays the results page
    return render(request, 'result.html', {
        'result': prediction_outcome,
        'result_prob': prediction_prob,
        'alive_percentage': alive_percentage,
        'dead_percentage': dead_percentage,
        'sepsis_percentage' : sepsis_percentage,
        'any_org_fail_percentage' : any_org_fail_percentage,
        'cardio_dys_percentage' : cardio_dys_percentage,
        'resp_dys_percentage' : resp_dys_percentage,
        'age_dp' :  age_dp,
        'hr_dp' : hr_dp
    })
