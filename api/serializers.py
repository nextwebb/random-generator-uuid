from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegistrationSerializers(serializers.ModelSerializer):
    # User registration  api data formatter.
    class Meta:  # pylint: disable=too-few-public-methods
        # Return default User options fields.
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }
