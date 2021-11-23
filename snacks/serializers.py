from rest_framework import serializers

from .models import Snack

class SnackSerlizer(serializers.ModelSerializer):
    class Meta :
        model = Snack
        fields = ('id', 'purchaser' ,'title', 'created_at', 'description')
        