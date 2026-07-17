from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ApplicantSerializer, JobSerializer
from portal.models import Job




class HomeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    


    def post(self, request, *args, **kwargs):
        serializer = ApplicantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Applicant created successfully"}, status=201)
      

    # def post(self, request, *args, **kwargs):
    #     return Response({"name": "Wellcome to my Portal"})




