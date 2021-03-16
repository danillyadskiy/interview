from rest_framework import serializers

from companies.models import Company
from companies.serializers.okved import OkvedSerializer


class CompanySerializer(serializers.ModelSerializer):
    region = serializers.ReadOnlyField(source='region.name')
    okopf = serializers.ReadOnlyField(source='okopf.name')
    main_okved_name = serializers.ReadOnlyField(source='main_okved.name')
    okved = OkvedSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = (
            'name',
            'inn',
            'kpp',
            'registration_date',
            'email',
            'link',
            'region',
            'okopf',
            'main_okved',
            'main_okved_name',
            'okved',
        )
