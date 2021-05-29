from .models import Random_UUID
from rest_framework import serializers


class UUIDSerializers(serializers.ModelSerializer):
    # User registration  api data formatter.
    class Meta:  # pylint: disable=too-few-public-methods
        # Return default User options fields.
        # Return optional model loan record
        model = Random_UUID
        fields = '__all__'
