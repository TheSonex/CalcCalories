def calculate_bmr(weight, height, age, gender):
    """
    Розрахунок базального метаболізму (BMR) за формулою Міффліна-Сан Жеора
    """
    if gender == 1:
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 2:
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Стать має бути 1 (чоловік) або 2 (жінка)")


def calculate_tdee(bmr, activity_level):
    """
    Розрахунок добової норми калорій (TDEE) на основі рівня активності
    """
    activity_multipliers = {
        1: 1.2,  # сидячий
        2: 1.375,  # малорухливий
        3: 1.55,  # помірний
        4: 1.725,  # активний
        5: 1.9  # дуже активний
    }

    if activity_level not in activity_multipliers:
        raise ValueError("Некоректний рівень активності")

    return bmr * activity_multipliers[activity_level]


def main():
    try:
        weight = float(input("Введіть вашу вагу (кг): "))
        height = float(input("Введіть ваш зріст (см): "))
        age = int(input("Введіть ваш вік: "))

        print("Оберіть вашу стать: 1 - Чоловік, 2 - Жінка")
        gender = int(input("Введіть 1 або 2: "))

        print("Оберіть рівень активності:")
        print("1 - Сидячий спосіб життя")
        print("2 - Малорухливий (легкі тренування 1-3 рази на тиждень)")
        print("3 - Помірний (помірні тренування 3-5 разів на тиждень)")
        print("4 - Активний (інтенсивні тренування 6-7 разів на тиждень)")
        print("5 - Дуже активний (важкі фізичні навантаження, спорт)")
        activity_level = int(input("Введіть число від 1 до 5: "))

        bmr = calculate_bmr(weight, height, age, gender)
        tdee = calculate_tdee(bmr, activity_level)

        print(f"Ваша добова норма калорій (TDEE): {tdee:.2f} ккал")
    except ValueError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
