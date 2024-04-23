from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

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
        floors = Floor.objects.annotate(flats_count=Count("flat"))

        return floors

    @staticmethod
    def get_floor_detail(pk):
        try:
            floor = Floor.object.prefetch_related("flat_set").get(id=pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None

        flats = list(floor.flat_set.all())

        data = {
            "number": floor.number,
            "flats": flats
        }

        return data
