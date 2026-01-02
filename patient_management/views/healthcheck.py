from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (HTTP_503_SERVICE_UNAVAILABLE, HTTP_200_OK)
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    health_status = {
        'status': 'healthy',
        'database': 'unknown',
    }
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        health_status['database'] = 'operational'
    except Exception as e:
        health_status['status'] = 'unhealthy'
        health_status['database'] = f'error: {str(e)}'
        return Response(health_status, status=HTTP_503_SERVICE_UNAVAILABLE)

    return Response(health_status, status=HTTP_200_OK)
