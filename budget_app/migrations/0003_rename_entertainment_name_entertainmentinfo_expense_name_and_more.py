# Generated by Django 4.0.5 on 2022-06-14 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0002_rename_savings_name_savingsinfo_saving_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entertainmentinfo',
            old_name='entertainment_name',
            new_name='expense_name',
        ),
        migrations.RenameField(
            model_name='savingsinfo',
            old_name='saving_name',
            new_name='expense_name',
        ),
        migrations.RenameField(
            model_name='studyinfo',
            old_name='study_name',
            new_name='expense_name',
        ),
        migrations.RenameField(
            model_name='travelsinfo',
            old_name='travel_name',
            new_name='expense_name',
        ),
    ]
