# Реализовать функцию которая принимает словарь вида:
new_dict = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            69.2578125,
                            30.031055426540206
                        ],
                        [
                            72.2900390625,
                            30.031055426540206
                        ],
                        [
                            72.2900390625,
                            31.50362930577303
                        ],
                        [
                            69.2578125,
                            31.50362930577303
                        ],
                        [
                            69.2578125,
                            30.031055426540206
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            73.037109375,
                            31.16580958786196
                        ],
                        [
                            74.3994140625,
                            31.16580958786196
                        ],
                        [
                            74.3994140625,
                            31.87755764334002
                        ],
                        [
                            73.037109375,
                            31.87755764334002
                        ],
                        [
                            73.037109375,
                            31.16580958786196
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Point",
                "coordinates": [
                    73.4326171875,
                    30.600093873550072
                ]
            }
        }
    ]
}

# Функция должна вернуть все координаты в виде списка т.е [[73.037109375, 31.16580958786196], [74.3994140625, 31.87755764334002]...].
# Так же функция должна валидировать входной словарь и если что-то введено неправильно - вернуть сообщение об этом.


# Без повідомлень про помилку
def get_coordinates(complex_dict):
    coordinates = []
    for feat in complex_dict.get("features"):
        coordinates.append(feat.get('geometry').get('coordinates', None))
    return coordinates


# З повідомленням про помилку 1
def get_coordinates_v1(complex_dict):
    coordinates = []
    if 'features' in complex_dict.keys():
        if not isinstance(complex_dict['features'], list):
            print('"features": key should contain a list value')
            return
        for feature_item in range(len(complex_dict['features'])):
            if 'geometry' in complex_dict['features'][feature_item]:
                if 'coordinates' in complex_dict['features'][feature_item]['geometry']:
                    coordinates.append(complex_dict['features'][feature_item]['geometry']['coordinates'])
                else:
                    coordinates.append(None)
            else:
                print(f'"features"/item_{feature_item}/"geometry": key does not exist')
                return
    else:
        print(f'"features": key does not exist')
        return
    return coordinates


# З повідомленням про помилку 2
def get_coordinates_v2(complex_dict):
    coordinates = []
    features = complex_dict.get('features', False)
    if not features or not isinstance(features, list):
        print('"features": key does not exist or it does not contain a list value')
        return
    for feature_item in range(len(features)):
        geometry = features[feature_item].get('geometry', False)
        if not geometry or not isinstance(geometry, dict):
            print(f'"features"/item_{feature_item}/"geometry": key does not exist '
                  f'or it does not contain a dict value')
            return
        coordinates.append(geometry.get('coordinates', None))
    return coordinates


a = get_coordinates_v2(complex_dict=new_dict)
print(a)
