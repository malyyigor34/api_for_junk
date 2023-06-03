from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import ReceiveSErializer


class Receive(APIView):
    def post(self, request):
        print(request.FILES.get('photo'))
        with open('rec.jpg', 'wb') as f:
            f.write(request.FILES['photo'].file.read())
        return Response({'status': 'ok'})
