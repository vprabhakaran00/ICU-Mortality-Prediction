# Generated by Django 4.2.2 on 2023-08-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PatientData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.IntegerField()),
                ("mean_hr", models.FloatField()),
                ("mean_sys_pr", models.FloatField()),
                ("mean_temp", models.FloatField()),
                ("sepsis", models.BooleanField(default=False)),
                ("any_org_fail", models.BooleanField(default=False)),
                ("cardio_dys", models.BooleanField(default=False)),
                ("resp_dys", models.BooleanField(default=False)),
                ("outcome", models.CharField(blank=True, max_length=4, null=True)),
                (
                    "probability",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
            ],
            options={
                "verbose_name": "Patient Data",
                "verbose_name_plural": "Patient Data",
            },
        ),
    ]
