from rest_framework import serializers
from api.models import Profile
from api.models import UserConcert
from api.models import UserConcertMedia



class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """translates Profiles to json"""

    class Meta:
        """like a form -- point at a model and tell it what fields you want to use"""
        model = Profile
        fields = ('id', 'url','profile_photo', 'quote_lyrics', 'favorite_artist')


class UserConcertSerializer(serializers.HyperlinkedModelSerializer):
    """translates UserConcerts to json"""

    user = ProfileSerializer(many=True, read_only=True)
    class Meta:
        model = UserConcert
        fields = ('id', 'url', 'concert_id', 'notes', 'rating')


class UserConcertMediaSerializer(serializers.HyperlinkedModelSerializer):
    """translates UserConcertMedia to json"""

    concert = UserConcertSerializer(many=True, read_only=True)
    class Meta:
        model = UserConcertMedia
        fields = ('id', 'url', 'concert_id', 'description', 'is_private')