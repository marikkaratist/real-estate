from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.paginator import Paginator
from django.db.models import Count

from config import settings
from realty.models import Flat, Floor


class FlatSelector:
    @staticmethod
    def flat_list():
        flats = Flat.objects.all()

        return flats

    @staticmethod
    def get_flat(pk):
        flat = Flat.objects.select_related("floor").get_object_or_404(pk)

        return flat


class FloorSelector:
    @staticmethod
    def get_floors():
        floors = Floor.objects.annotate(flats=Count("flat"))

        return floors

    @staticmethod
    def get_floor_detail(pk):
        pass
