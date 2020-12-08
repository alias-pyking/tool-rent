from abc import ABC

from rest_framework import serializers
from .models import Tool, Picture
from django.core.files.uploadedfile import InMemoryUploadedFile


class ToolSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField(method_name='get_reviews_url')
    images = serializers.SerializerMethodField()
    # ratings = serializers.SerializerMethodField()

    class Meta:
        model = Tool
        fields = '__all__'

    @staticmethod
    def get_user(obj):
        return obj.user.username

    @staticmethod
    def get_reviews_url(obj):
        return obj.get_reviews_url()

    @staticmethod
    def get_images(obj):
        return [img.image.url for img in obj.images.all()]

    @staticmethod
    def get_rating(obj):
        pass

    @staticmethod
    def create_pictures(images):
        pictures = []
        print(images)
        print(type(images[0]))
        for pic in images:
            if type(pic) is not InMemoryUploadedFile:
                raise serializers.ValidationError({'images': 'This field should be an array of images'})
            pictures.append(Picture(image=pic, image_alt_text=pic.name))
        return pictures

    def create(self, validated_data, **kwargs):
        tool = Tool(**validated_data, user=kwargs['user'])
        return tool

    def save(self, user, **kwargs):
        data = self.validated_data
        images = self.custom_validate(**kwargs)
        tool = self.create(data, user=user)
        tool.save()
        pictures = self.create_pictures(images=images)
        Picture.objects.bulk_create(pictures)
        tool.images.add(*pictures)
        return tool

    def update(self, instance, validated_data, **kwargs):
        images = self.custom_validate(update=True, **kwargs)
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

    @staticmethod
    def custom_validate(update=False, **kwargs):
        try:
            images = kwargs['images']
        except KeyError:
            raise AttributeError('Tool serializer requires you to pass images as kwargs in update and save methods')
        if len(images) == 0 and not update:
            raise serializers.ValidationError({
                'images': ['This field is required']
            })
        return images

    def validate(self, data):
        validation_errors = {}

        if data.get('name') is None or data.get('name') == '':
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

