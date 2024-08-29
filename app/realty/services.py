from realty.models import Flat


def flat_create(*, name: str, price: int, overall_square: int, living_square: int, rooms: int, view_from_windows: str,
                lavatory: int, level: int, elevator: int, year_of_sale: int, parking: str, is_complete: bool,
                has_kitchen: bool) -> Flat:

    obj = Flat(name=name, price=price, overall_square=overall_square, living_square=living_square, rooms=rooms,
               view_from_windows=view_from_windows, lavatory=lavatory, level=level, elevator=elevator,
               year_of_sale=year_of_sale, parking=parking, is_complete=is_complete, has_kitchen=has_kitchen)

    obj.full_clean()
    obj.save()

    return obj
