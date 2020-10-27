from abc import ABC

from rest_framework import serializers
from .models import Tool, Picture
from .constants import STATUS_CHOICES
from django.forms.widgets import ClearableFileInput


class ListToolSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField(method_name='get_reviews_url')
    images = serializers.SerializerMethodField()
    # ratings = serializers.SerializerMethodField()

    class Meta:
        model = Tool
        fields = ['id', 'user', 'name', 'description', 'quantity', 'cost', 'images', 'status', 'timestamp',
                  'updated_on',
                  'reviews']

    def get_user(self, obj):
        return obj.user.username

    def get_reviews_url(self, obj):
        return obj.get_reviews_url()

    def get_images(self, obj):
        return [img.image.url for img in obj.images.all()]

    def get_rating(self, obj):
        pass


class CreateUpdateToolSerializer(serializers.Serializer):
    name = serializers.CharField(label='Name', required=True)
    description = serializers.CharField(label='Description', required=True)
    status = serializers.ChoiceField(label='Status', choices=STATUS_CHOICES, required=True)
    quantity = serializers.IntegerField(label='Quantity', required=True)
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data, **kwargs):
        tool = Tool(**validated_data, user=kwargs['user'])
        return tool

    @staticmethod
    def create_pictures(images):
        pictures = []
        for pic in images:
            pictures.append(Picture(image=pic, image_alt_text=pic.name))
        return pictures

    def save(self, user, images=None):
        data = self.validated_data
        tool = self.create(data, user=user)
        tool.save()
        pictures = self.create_pictures(images=images)
        Picture.objects.bulk_create(pictures)
        tool.images.add(*pictures)

        return tool

    def update(self, instance, validated_data, images=None):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        if images:
            pictures = self.create_pictures(images=images)
            Picture.objects.bulk_create(pictures)
            instance.images.add(*pictures)
        return instance

    def validate(self, data):
        validation_errors = {}

        if data.get('name') is None or data.get('name') == 'sks':
            validation_errors.update({
                'name': 'This field is required'
            })
        if data.get('description') is None or data.get('description') == '':
            validation_errors.update({
                'description': 'Description field is required'
            })

        if data.get('quantity') is None or data.get('quantity') == '':
            validation_errors.update({
                'quantity': 'This field is required',
            })

        if data.get('cost') is None or data.get('cost') == '':
            validation_errors.update({
                'cost': 'This field is required'
            })
        if validation_errors:
            raise serializers.ValidationError(validation_errors)
        return data


class EditToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['name', 'description', 'quantity', 'cost', 'timestamp', 'updated_on']
