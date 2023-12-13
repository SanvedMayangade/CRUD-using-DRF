from rest_framework import serializers
from .models import *

class studentserializers(serializers.ModelSerializer):
    
    class  Meta:
        model = Students
        fields = ['name','email','roll_no','adress']

    # def create(self, validate_data):
    #     return Students.objects.create(**validate_data)

