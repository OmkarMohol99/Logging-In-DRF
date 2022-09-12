from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User 


class EmployeeSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    eid = serializers.IntegerField()
    name = serializers.CharField(max_length=30)


    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.eid = validated_data.get('eid',instance.eid)
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance


class SignupSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id','username', 'password', 'first_name', 'last_name')
