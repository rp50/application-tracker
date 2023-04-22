from . import models
from rest_framework import serializers


class JobSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    company = serializers.CharField(max_length=50)
    link = serializers.URLField(max_length=300)
    date_applied = serializers.DateField()
    stage = serializers.CharField(
        max_length=2, choices=models.Job.Stage.choices, default=models.Job.Stage.APPLIED
    )
    stage_completed = serializers.BooleanField()
    stage_deadline = serializers.DateField()
    applicant = serializers.PrimaryKeyRelatedField(many=False)
