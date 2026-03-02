from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

class JobStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.filter(user=request.user)

        data = {
            "total_jobs": jobs.count(),
            "applied": jobs.filter(status="Applied").count(),
            "interview": jobs.filter(status="Interview").count(),
            "rejected": jobs.filter(status="Rejected").count(),
            "offer": jobs.filter(status="Offer").count(),
        }

        return Response(data)

class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status']
    search_fields = ['company_name', 'role']

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.filter(user=request.user)

        total = jobs.count()
        interviews = jobs.filter(status="Interview").count()
        offers = jobs.filter(status="Offer").count()

        conversion_rate = (interviews / total * 100) if total > 0 else 0
        offer_ratio = (offers / interviews * 100) if interviews > 0 else 0

        return Response({
            "total_applications": total,
            "interviews": interviews,
            "offers": offers,
            "application_to_interview_rate": round(conversion_rate, 2),
            "interview_to_offer_ratio": round(offer_ratio, 2)
        })