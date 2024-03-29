from rest_framework import serializers

from .models import ReferralCode, CustomUser


class CreateReferralCodeSerializer(serializers.ModelSerializer):
    """Сериализатор для создания реферального кода"""

    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ReferralCode
        fields = ('user_id', 'referral_code_title', 'referral_code_due_date',)


class GetReferralCodeSerializer(serializers.ModelSerializer):
    """Серализатор для получения реферального кода и вывода информации о нем"""

    referral_code = serializers.CharField(source='referral_code.referral_code_title')
    referral_code_due_date = serializers.CharField(source='referral_code.referral_code_due_date')

    class Meta:
        model = ReferralCode
        fields = ('referral_code', 'referral_code_due_date')


class GetReferralsListSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки информации о всех пользователях с реферальным кодом"""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',)
