from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=63)
    location = models.TextField()
    contact_no = models.CharField(max_length=10)


class Job(models.Model):
    company = models.ForeignKey(Company, 
                                related_name="company", 
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=127)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Applicant(models.Model):
    STATUS = (
        ("Pending", "pending"),
        ("Accepted", "accepted"),
        ("Rejected", "rejected")
    )
    job = models.ForeignKey(Job, related_name="jobs", 
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    email = models.EmailField()
    cv = models.FileField(upload_to="cvs/")
    status = models.CharField(
        choices=STATUS, max_length=63, default="pending" ,null=True, blank=True)
    user = models.ForeignKey(
        User, related_name="applicant", on_delete=models.CASCADE,
        blank=True, null=True
    )
    applied_datetime = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )