from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..serializers.encounter import EncounterSerializer
from ..models.encounter import Encounter


class EncounterViews(viewsets.ModelViewSet):
    serializer_class = EncounterSerializer
    permission_classes = [AllowAny]
    required_permission = 'view_encounter'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patient', 'doctor']

    def get_queryset(self):
        queryset = Encounter.objects.select_related(
            'patient', 'doctor', 'created_by', 'updated_by'
        ).all()

        from_date = self.request.query_params.get('from', None)
        to_date = self.request.query_params.get('to', None)

        if from_date:
            queryset = queryset.filter(visit_datetime__gte=from_date)
        if to_date:
            queryset = queryset.filter(visit_datetime__lte=to_date)

        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
