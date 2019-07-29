from .. import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CommentList(APIView):
    """
    List all comments, or create a new comment.
    """
    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None, version=None):
        comments = models.Comment.objects.all()
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None, version=None):
        serializer = serializers.CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
