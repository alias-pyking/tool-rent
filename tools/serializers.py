from rest_framework import serializers
from .models import Tool


class ListToolSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField(method_name='get_reviews_url')
    class Meta:
        model = Tool
        fields = ['id', 'user', 'name', 'description', 'quantity', 'cost', 'timestamp', 'updated_on', 'reviews']
    
    def get_user(self, obj):
        return obj.user.username
    
    def get_reviews_url(self, obj):
        return obj.get_reviews_url()


class CreateUpdateToolSerializer(serializers.Serializer):
    name = serializers.CharField(label='Name', required=True)
    description = serializers.CharField(label='Description', required=True)
    quantity = serializers.IntegerField(label='Quantity',required=True)
    cost = serializers.DecimalField(max_digits=10,decimal_places=2)

    def save(self, user):
        data = self.validated_data
        tool = Tool.objects.create(**data, user=user)
        tool.save()
        return tool
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.save()
        return instance

    
    def validate(self, data):
        validation_errors = {}
        
        if data.get('name') is None or data.get('name') == 'sks':
            validation_errors.update({
                'name':'This field is required'
            })
        if data.get('description') is None or data.get('description') == '':
            validation_errors.update({
                'description':'Description field is required'
            })
        
        if data.get('quantity') is None or data.get('quantity') == '':
            validation_errors.update({
                'quantity':'This field is required',
            })
        
        if data.get('cost') is None or data.get('cost') == '':
            validation_errors.update({
                'cost':'This Fied is required'
            })
        if validation_errors:
            raise serializers.ValidationError(validation_errors)
        return data


class EditToolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tool
        fields = ['name', 'description', 'quantity', 'cost', 'timestamp', 'updated_on']
