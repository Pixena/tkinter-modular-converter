RU_TO_EN = {
    "килограммы": "kilograms",
    "граммы": "grams",
    "миллиграммы": "milligrams",
    "тонны": "tonnes"
}

EN_TO_RU = {v: k for k, v in RU_TO_EN.items()}

def convert_mass(value, from_unit, to_unit):
    from_unit_en = RU_TO_EN.get(from_unit, from_unit)
    to_unit_en = RU_TO_EN.get(to_unit, to_unit)
    if from_unit_en == to_unit_en:
        return value
    if from_unit_en == "kilograms":
        if to_unit_en == "grams":
            return value * 1000
        if to_unit_en == "milligrams":
            return value * 1000000
        if to_unit_en == "tonnes":
            return value / 1000
    if from_unit_en == "grams":
        if to_unit_en == "kilograms":
            return value / 1000
        if to_unit_en == "milligrams":
            return value * 1000
        if to_unit_en == "tonnes":
            return value / 1000000
    if from_unit_en == "milligrams":
        if to_unit_en == "kilograms":
            return value / 1000000
        if to_unit_en == "grams":
            return value / 1000
        if to_unit_en == "tonnes":
            return value / 1000000000
    if from_unit_en == "tonnes":
        if to_unit_en == "kilograms":
            return value * 1000
        if to_unit_en == "grams":
            return value * 1000000
        if to_unit_en == "milligrams":
            return value * 1000000000
    return value