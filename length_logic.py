RU_TO_EN = {
    "метры": "meters",
    "сантиметры": "centimeters",
    "миллиметры": "millimeters",
    "километры": "kilometers"
}

EN_TO_RU = {v: k for k, v in RU_TO_EN.items()}

def convert_length(value, from_unit, to_unit):
    from_unit_en = RU_TO_EN.get(from_unit, from_unit)
    to_unit_en = RU_TO_EN.get(to_unit, to_unit)
    if from_unit_en == to_unit_en:
        return value
    if from_unit_en == "meters":
        if to_unit_en == "centimeters":
            return value * 100
        if to_unit_en == "millimeters":
            return value * 1000
        if to_unit_en == "kilometers":
            return value / 1000
    if from_unit_en == "centimeters":
        if to_unit_en == "meters":
            return value / 100
        if to_unit_en == "millimeters":
            return value * 10
        if to_unit_en == "kilometers":
            return value / 100000
    if from_unit_en == "millimeters":
        if to_unit_en == "meters":
            return value / 1000
        if to_unit_en == "centimeters":
            return value / 10
        if to_unit_en == "kilometers":
            return value / 1000000
    if from_unit_en == "kilometers":
        if to_unit_en == "meters":
            return value * 1000
        if to_unit_en == "centimeters":
            return value * 100000
        if to_unit_en == "millimeters":
            return value * 1000000
    return value