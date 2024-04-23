from rest_framework import serializers


class FlatDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=120)
    price = serializers.IntegerField()
    overall_square = serializers.IntegerField()
    living_square = serializers.IntegerField()
    rooms = serializers.IntegerField()
    view_from_windows = serializers.CharField()
    lavatory = serializers.IntegerField()
    level = serializers.IntegerField()
    elevator = serializers.IntegerField()
    year_of_sale = serializers.IntegerField()
    parking = serializers.CharField()
    is_complete = serializers.BooleanField()
    has_kitchen = serializers.BooleanField()
    floor = serializers.CharField(
        read_only=True,
        source="floor"
    )
