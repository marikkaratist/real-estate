from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count
from django.shortcuts import get_object_or_404

from realty.models import Flat, Floor


class FlatSelector:
    @staticmethod
    def flat_list():
        flats = Flat.objects.all()

        return flats

    @staticmethod
    def get_flat(pk):
        flat = get_object_or_404(Flat.objects.select_related("floor"), pk=pk)

        return flat


class FloorSelector:
    @staticmethod
    def get_floors():
        floors = Floor.objects.annotate(flats_count=Count("flats"))

        return floors

    @staticmethod
    def get_floor_detail(pk):
        try:
            floor = Floor.objects.prefetch_related("flats").get(pk=pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None

        return floor
