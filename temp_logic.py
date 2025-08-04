def convert_temp(value, from_unit, to_unit):
    RU_TO_EN = {
        "Цельсий": "Celsius",
        "Фаренгейт": "Fahrenheit",
        "Кельвин": "Kelvin"
    }
    from_unit_en = RU_TO_EN.get(from_unit, from_unit)
    to_unit_en = RU_TO_EN.get(to_unit, to_unit)

    if from_unit_en == to_unit_en:
        return value
    if from_unit_en == "Celsius":
        if to_unit_en == "Fahrenheit":
            return value * 9/5 + 32
        if to_unit_en == "Kelvin":
            return value + 273.15
    if from_unit_en == "Fahrenheit":
        if to_unit_en == "Celsius":
            return (value - 32) * 5/9
        if to_unit_en == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    if from_unit_en == "Kelvin":
        if to_unit_en == "Celsius":
            return value - 273.15
        if to_unit_en == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return