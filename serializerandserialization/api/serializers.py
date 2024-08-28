from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()  # id=serializers.AutoField()  # auto field ko bhanney  # id=serializers.IntegerField(read_only=True)  # id ko read only mode ko bhanney
    name=serializers.CharField(max_length=100)
    rolls=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

