from rest_framework import serializers

from companies.models import Okved


class OkvedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Okved
        fields = (
            'code',
            'name',
        )
