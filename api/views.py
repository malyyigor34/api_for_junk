from rest_framework.views import APIView
from rest_framework.response import Response
from api.vision import markImage
from api.ChatRequestGenerator import ChatRequestGenerator
import openai


class RecognizePhoto(APIView):
    def post(self, request):
        photo = request.FILES['photo'].file.read()
        with open('rec.jpg', 'wb') as f:
            f.write(photo)

        res = markImage(photo)
        print(f"Vision return {res}")
        return Response({'object': res})


class RecognizeAndAnswer(APIView):
    def post(self, request):
        openai.api_key = "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"

        photo = request.FILES['photo'].file.read()
        with open('rec.jpg', 'wb') as f:
            f.write(photo)

        res = markImage(photo)
        print(f"Vision return {res}")
        chat = ChatRequestGenerator(res)
        return Response({'object': chat.make_request()})
