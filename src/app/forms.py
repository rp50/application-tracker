from django import forms
from . import models

class AddApplication(forms.ModelForm):
    class Meta:
        model = models.Job
        fields = ["title", "company", "link", "date_applied", "stage", "stage_completed", "stage_deadline"]
