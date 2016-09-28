from rest_framework import serializers
from models import QBPost, QBUser, QBComment


class QBPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = QBPost
        fields = ('post_id', 'user', 'post_text', 'created_time', 'like_count', 'comment_count')




