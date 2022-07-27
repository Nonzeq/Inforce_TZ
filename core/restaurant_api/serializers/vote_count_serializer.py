from rest_framework import serializers

from ..models.vote import VoteCounts


class VoteCountSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='menu', read_only=True)
    class Meta:
        model = VoteCounts
        fields = "__all__"
        
        

class VoteSerializer(serializers.Serializer):
    total_vote = serializers.CharField()

