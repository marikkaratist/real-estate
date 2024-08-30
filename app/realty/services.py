from realty.models import Flat, Floor


def flat_create(**kwargs) -> Flat:
    required_keys = [
        'name', 'price', 'overall_square', 'living_square', 'rooms',
        'view_from_windows', 'lavatory', 'elevator',
        'year_of_sale', 'parking', 'is_complete', 'has_kitchen', 'floor_id'
    ]

    # Проверяем наличие всех обязательных аргументов
    for key in required_keys:
        if key not in kwargs:
            raise ValueError(f'Missing required argument: {key}')

    # Получаем объект Floor по его идентификатору
    floor_id = kwargs['floor_id']
    floor = Floor.objects.get(id=floor_id)

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
        floor=floor  # Передаем объект Floor
    )

    # Проверяем и сохраняем объект Flat
    obj.full_clean()
    obj.save()

    return obj
