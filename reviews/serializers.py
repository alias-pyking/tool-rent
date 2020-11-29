from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for listing Reviews of a Tool/Product
    or getting a Review
    """
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        exclude = ['tool']

    def get_user(self, obj):
        return obj.user.username


class CreateReviewSerializer(serializers.Serializer):
    """
    Serializer for Creating a Review
    """
    title = serializers.CharField(label='Review Title', required=True)
    text = serializers.CharField(label='Review Description', required=True)
    stars = serializers.IntegerField(label='Review Stars', required=True)

    def create(self, validated_data, **kwargs):
        review = Review(user=kwargs['user'], tool=kwargs['tool'], **validated_data)
        return review

    def save(self, user, tool):
        review = self.create(validated_data=self.validated_data, user=user, tool=tool)
        review.save()
        return review

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        """
        Object level validation for CreateSerializer(obviously)
        """
        validation_errors = {}
        if data.get('stars') is None or data.get('stars') == '':
            validation_errors.update({
                'stars': 'This field is required',
            })
        elif int(data.get('stars')) > 5:
            validation_errors.update({
                'stars': 'Stars cannot have a value greater than 5'
            })
        if validation_errors:
            raise serializers.ValidationError(validation_errors)
        return data
