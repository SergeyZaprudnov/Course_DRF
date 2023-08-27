from rest_framework import serializers

from habbit.models import Habbit
from habbit.validators import validate_time_complete, validate_related_habbit, validate_period
from users.models import User


class HabbitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    time_complete = serializers.IntegerField(validators=[validate_time_complete])
    related_habbit = serializers.PrimaryKeyRelatedField(queryset=Habbit.objects.all(), required=False,
                                                        validators=[validate_related_habbit])
    period = serializers.IntegerField(validators=[validate_period])

    class Meta:
        model = Habbit
        fields = '__all__'
