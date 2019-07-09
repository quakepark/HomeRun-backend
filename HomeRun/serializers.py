from rest_framework import serializers
from HomeRun.models import Registration


class RegSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = ('id', 'First_Name', 'Last_Name', 'Address',
                  'Email_Address', 'created_at', 'Phone_Number')
