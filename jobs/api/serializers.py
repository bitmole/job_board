from rest_framework import serializers
from jobs.models import JobOffer

class JobOfferSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField()
    company_email = serializers.EmailField()
    job_title = serializers.CharField()
    job_description = serializers.CharField()
    salary = serializers.IntegerField()
    city = serializers.CharField()
    state = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    available = serializers.BooleanField()

    def create(self, validated_data):
        print(validated_data)
        return JobOffer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.company_email = validated_data.get('company_email', instance.company_email)
        instance.job_title = validated_data.get('job_title', instance.job_title)
        instance.job_description = validated_data.get('job_description', instance.job_description)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance
