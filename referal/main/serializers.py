from rest_framework import serializers

from .models import ReferralCode


class CreateReferralCodeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ReferralCode
        fields = ('user_id', 'reference_code', 'referral_due_date',)
