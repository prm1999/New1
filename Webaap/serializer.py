from rest_framework import serializers

from .models import student, More_Info, upadte_info


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        # field=('first_name','last_name')
        fields = '__all__'


class More_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = More_Info
        fields = '__all__'


class upadteinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = upadte_info
        fields = '__all__'
