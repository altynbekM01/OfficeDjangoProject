from rest_framework import serializers


from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee
        fields = ('name','surname', 'middleName', 'position','joined_at','salary', 'chief')

class PositionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee
        fields = ('id', 'position')