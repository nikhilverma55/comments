from rest_framework import serializers
from .. import models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id', 'user', 'orders', 'comment_text', 'active', 'parent']

    def create(self, validated_data):
        """
        Create and return a new `comment` instance, given the validated data.
        """
        return models.Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `comment` instance, given the validated data.
        """
        instance.title = validated_data.get('user_id', instance.user_id)
        instance.code = validated_data.get('comment_text', instance.comment_text)
        instance.linenos = validated_data.get('active', instance.active)
        instance.language = validated_data.get('parent_id', instance.parent_id)
        instance.save()
        return instance