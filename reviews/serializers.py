from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for listing Reviews of a Tool/Product
    or getting a Review
    """
    class Meta:
        model = Review
        exclude = ['tool']


class CreateReviewSerializer(serializers.Serializer):
    """
    Serilizer for Creating a Review
    """
    title = serializers.CharField(label='Review Title', required=True)
    text = serializers.CharField(label='Reivew Description', required=True)
    stars = serializers.IntegerField(label='Review Stars', required=True)

    def save(self, user, tool):
        data = self.validated_data
        review = Review(user=user, tool=tool, title=data.get('title'), text=data.get('text'), stars=data.get('stars'))
        review.save()
        return review

    def validate(self, data):
        """
        Object level validation for CreateSerializer(obviously)
        """
        validation_errors = {}
        if data.get('stars') is None or data.get('stars') == '':
            validation_errors.update({
                'stars':'This field is required',
            })
        elif int(data.get('stars')) > 5:
            validation_errors.update({
                'stars':'Stars cannot have a value greater than 5'
            })
        if validation_errors:
            raise serializers.ValidationError(validation_errors)
        return data