from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer

@api_view(['GET', 'POST'])
def job_list_create_api_view(request):
    if request.method == 'GET':
        jobs = JobOffer.objects.filter(available=True)
        ser = JobOfferSerializer(jobs, many=True)
        return Response(ser.data)
    elif request.method == 'POST':
        ser = JobOfferSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def job_detail_api_view(request, pk):
    try:
        job = JobOffer.objects.get(pk=pk)
    except JobOffer.DoesNotExist:
        return Response({'error': {'code': 404, 'message': 'Job not found.'}},
                status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = JobOfferSerializer(job)
        return Response(ser.data)
    elif request.method == 'PUT':
        ser = JobOfferSerializer(job, data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        ser.save()
        return Response(ser.data)
    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
