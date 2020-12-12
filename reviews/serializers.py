from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    stars = serializers.IntegerField(required=True)

    class Meta:
        model = Review
        exclude = ('tool', )

    @staticmethod
    def get_user(obj):
        return obj.user.username

    def create(self, validated_data, **kwargs):
        tool = kwargs['tool']
        total_users_rated = int(tool.total_users_rated) + 1
        tool.total_stars = float(tool.total_stars + int(validated_data['stars']))
        tool.total_users_rated = total_users_rated
        tool.rating = float(tool.total_stars/total_users_rated)
        tool.save()
        review = Review(user=kwargs['user'], tool=tool, **validated_data)
        return review

    def save(self, user, tool):
        review = self.create(validated_data=self.validated_data, user=user, tool=tool)
        review.save()
        return review

    def update(self, instance, validated_data):
        raise NotImplemented('Please come and implement this method first before calling it.')

    def validate(self, data):
        """
        Object level validation for ReviewSerializer(obviously)
        """
        validation_errors = {}
        if int(data.get('stars')) > 5:
            validation_errors.update({
                'stars': 'Stars cannot have a value greater than 5'
            })
        if validation_errors:
            raise serializers.ValidationError(validation_errors)
        return data
