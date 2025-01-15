from django.core.mail import send_mail
from django.conf import settings
from .models import Subscriber
from .serializers import SubscriberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SubscribeAPIView(APIView):
    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            subscriber = serializer.save()
            # Send a welcome email
            subject = "عضویت در خبرنامه بیزینو"
            message = "پیوستن شما را به خبرنامه بیزینو تبریک میگوییم. ازین پس میتوانید از مقالات و سایر رویداد های بیزینو، در سریع ترین زمان ممکن از طریق ایمیل با خبر شوید. "
            recipient = subscriber.email
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient])
            return Response({"message": "Subscribed successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnsubscribeAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            subscriber = Subscriber.objects.get(email=email)
            subscriber.is_active = False
            subscriber.save()
            return Response({"message": "Unsubscribed successfully!"}, status=status.HTTP_200_OK)
        except Subscriber.DoesNotExist:
            return Response({"error": "Email not found!"}, status=status.HTTP_404_NOT_FOUND)
