from rest_framework import serializers
from .models import Student


def starts_with_r(value):
    if value[0].lower() !='r':
        raise serializers.ValidationError("Name should start with 'R'")
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[starts_with_r])
    rolls=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.rolls=validated_data.get('rolls',instance.rolls)
        instance.city=validated_data.get('city',instance.city)
        instance.save()#we have to save the instance
        return instance
    
    #field level validation
    def validate_rolls(self,value):
        if value>=200:
            raise serializers.ValidationError("Roll number should not be greater than 200 or it is seat full")
        return value
    # object level validation  
    def validate(self,data):
        nm=data.get('name')
        ci=data.get('city')
        if len(nm)>5 or ci!=ci.lower():
            raise serializers.ValidationError("Name and city should be of length small than 5 and city shoulde in lower")
        return data
    # 
    