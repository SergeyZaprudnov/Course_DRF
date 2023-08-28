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

    def validate(self, data):
        related_habbit = data.get('related_habbit')
        reward = data.get('reward')
        useful = data.get('useful')
        if related_habbit and reward:
            raise serializers.ValidationError('Привычка и награда не могут указываться одновременно')
        elif useful and (reward is not None or related_habbit is not None):
            raise serializers.ValidationError('Приятная привычка не вознаграждается и не имеет связанной привычки')
        return data

