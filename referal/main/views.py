from functools import wraps

from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response

from .models import ReferralCode
from .serializers import CreateReferralCodeSerializer


class CreateReferralCodeAPIView(CreateAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = CreateReferralCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.validated_data['user'] = request.user
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            error_message = 'У вас уже есть код реферера, удалите свой перед созданием нового!'
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)


class DestroyReferralCodeAPIView(DestroyAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = CreateReferralCodeSerializer
