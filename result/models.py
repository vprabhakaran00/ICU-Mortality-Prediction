"""
This file represent the data structure in the application.
Models define the database schema.
Each model class represents a table in the database.
Each attribute of the class represents a column in the table.
"""

# Importing needed libraries
from django.db import models    # for Django's database functionalities
import pandas as pd             # for handling data in dataframe
from joblib import load         # loading a pre-trained machine learning model


# We define the Django model called PatientData here.
# We include a method to predict patient outcome based on the inputs

# define model class: PatientData => a Django model from models.Model
class PatientData(models.Model):
    # Defining 8 input variables and 2 output variables here
    age = models.IntegerField()
    mean_hr = models.FloatField()
    mean_sys_pr = models.FloatField()
    mean_temp = models.FloatField()
    sepsis = models.BooleanField(default=False)
    any_org_fail = models.BooleanField(default=False)
    cardio_dys = models.BooleanField(default=False)
    resp_dys = models.BooleanField(default=False)
    outcome = models.CharField(max_length=4, blank=True, null=True)
    probability = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    # define the 'predict_outcome' function
    def predict_outcome(self):
        # Load the pre-trained XGBoost model
        model = load('./savedModel/XGBmodel.sav')

        # Changing radio button value to integer to match the input format
        sepsis_flag = 1 if self.sepsis == 'Yes' else 0
        any_org_fail_flag = 1 if self.any_org_fail == 'Yes' else 0
        cardio_dys_flag = 1 if self.cardio_dys == 'Yes' else 0
        resp_dys_flag = 1 if self.resp_dys == 'Yes' else 0

        # Converting input features to a dataframe
        input_data = pd.DataFrame({
            'Age': [self.age],
            'Mean Heart Rate': [self.mean_hr],
            'Mean Systolic Pressure': [self.mean_sys_pr],
            'Mean Temperature': [self.mean_temp],
            'Sepsis': [sepsis_flag],
            'Any Organ Failure': [any_org_fail_flag],
            'Cardiovascular Dysfunction': [cardio_dys_flag],
            'Respiratory Dysfunction': [resp_dys_flag]
        })

        # Prediction using input dataframe
        y_pred = model.predict(input_data)
        y_prob = model.predict_proba(input_data)[:,1]

        # Specifying prediction output label
        if y_pred[0] == 0:
            self.outcome = 'live'
            self.probability = (1 - y_prob.item()) * 100
        else:
            self.outcome = 'die'
            self.probability = y_prob.item() * 100

        # Rounding probability to 2 decimal places
        self.probability = round(self.probability, 2)

        # Save the instance with the prediction outcome to the database
        self.save()

        # Return the prediction outcome
        return self.outcome, self.probability

    # The IDs of each entry now follows format of a string - "Patient" + id of PatientData
    def __str__(self):
        return f"Patient {self.id}"

    # defining model's meta data, sets human readable names
    class Meta:
        verbose_name = 'Patient Data'
        verbose_name_plural = 'Patient Data'
