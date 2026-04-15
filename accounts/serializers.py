from .models import Users
from rest_framework import serializers

class RegisterUser(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['username','password']
        extra_kwargs={
            'password':{'write_only': True}
        }
    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)

        
    