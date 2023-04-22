from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Job(models.Model):
    class Stage(models.TextChoices):
        APPLIED = "AP", _("Applied")
        ONLINE_ASSESSMENT = "OA", _("Online Assessment")
        PHONE_SCREEN = "PS", _("Phone Screen")
        INTERVIEW = "IN", _("Interview")
        OFFER = "OF", _("Offer")
        GHOSTED = "GH", _("Ghosted")
        REJECTED = "RJ", _("Rejected")

    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    link = models.URLField(max_length=300)
    date_applied = models.DateField()
    stage = models.CharField(max_length=2, choices=Stage.choices, default=Stage.APPLIED)
    stage_completed = models.BooleanField()
    stage_deadline = models.DateField()
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
