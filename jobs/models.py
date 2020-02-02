from django.db import models

# Create your models here.

class JobOffer(models.Model):

    """JobOffer model"""

    company_name = models.CharField(max_length=60)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=60)
    job_description = models.TextField(blank=True)
    salary = models.IntegerField()
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{ self.job_title } at { self.company_name }'
