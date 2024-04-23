from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from realty.selectors import FlatSelector, FloorSelector
from serializers import FlatDetailSerializer


class FlatListApi(APIView):
    class FlatListSerializer(serializers.Serializer):
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

    def get(self, request):
        flats = FlatSelector.flat_list()

        data = self.FlatListSerializer(flats, many=True).data

        return Response(data)


class FlatDetailApi(APIView):
    def get(self, request, pk):
        flat = FlatSelector.get_flat(pk=pk)

        data = FlatDetailSerializer(flat).data

        return Response(data)


class FloorListApi(APIView):
    class FloorListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        flats_count = serializers.IntegerField()

    def get(self, request):
        floors = FloorSelector.get_floors()

        data = self.FloorListSerializer(floors, many=True).data

        return Response(data)


class FloorDetailApi(APIView):
    class FloorDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        number = serializers.IntegerField()
        flats = FlatDetailSerializer(many=True)

    def get(self, request, pk):
        floor = FloorSelector.get_floor_detail(pk)

        data = self.FloorDetailSerializer(floor).data

        return data
