from rest_framework import serializers
from portal.models import Applicant, Job
from portal.models import Applicant


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "description",
            "start_date",
            "end_date",
        ]


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = [
            "name",
            "email",
            "job"
        ]