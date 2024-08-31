from realty.models import Flat

REQUIRED_KEYS = [
    'name', 'price', 'overall_square', 'living_square', 'rooms',
    'view_from_windows', 'lavatory', 'elevator',
    'year_of_sale', 'parking', 'is_complete', 'has_kitchen', 'floor_id'
]


def flat_create(**kwargs) -> Flat:

    # Проверяем наличие всех обязательных аргументов
    for key in REQUIRED_KEYS:
        if key not in kwargs:
            raise ValueError(f'Missing required argument: {key}')

    # Создаем объект Flat
    obj = Flat(
        name=kwargs['name'],
        price=kwargs['price'],
        overall_square=kwargs['overall_square'],
        living_square=kwargs['living_square'],
        rooms=kwargs['rooms'],
        view_from_windows=kwargs['view_from_windows'],
        lavatory=kwargs['lavatory'],
        elevator=kwargs['elevator'],
        year_of_sale=kwargs['year_of_sale'],
        parking=kwargs['parking'],
        is_complete=kwargs['is_complete'],
        has_kitchen=kwargs['has_kitchen'],
        floor_id=kwargs['floor_id']
    )

    # Проверяем и сохраняем объект Flat
    obj.full_clean()
    obj.save()

    return obj
