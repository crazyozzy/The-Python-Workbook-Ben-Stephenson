# Упражнение 66. Никаких центов
#
# 4 февраля 2013 года Королевским канадским монетным двором была вы-
# пущена последняя монета номиналом в один цент. После вывода центов
# из обращения все магазины вынуждены были изменить цены на товары
# таким образом, чтобы они стали кратны пяти центам (расчеты по бан-
# ковским картам по-прежнему ведутся с учетом центов). И хотя продавцы
# вольны сами определять политику преобразования цен, большинство из
# них просто округлили цены до ближайших пяти центов.
# Напишите программу, запрашивающую у пользователя цены, пока не
# будет введена пустая строка. На первой строке выведите сумму всех вве-
# денных пользователем сумм, а на второй – сумму, которую покупатель
# должен заплатить наличными. Эта сумма должна быть округлена до бли-
# жайших пяти центов. Вычислить сумму для оплаты наличными можно,
# получив остаток от деления общей суммы в центах на 5. Если он будет
# меньше 2,5, следует округлить сумму вниз, а если больше – вверх.

prices = []

while True:
    user_input = input("Введите цену: ")

    if not user_input:
        print(f"Введенные числа: {prices}")
        sum_prices = int(sum(prices) * 100)
        round_sum = sum_prices % 5
        if sum_prices % 5 < 2.5:
            print(f"Сумма к оплате: {round((sum_prices // 5) * 5 / 100, 2)}")
        else:
            print(f"Сумма к оплате: {round(((sum_prices // 5) * 5 + 5) / 100, 2)}")
        break

    try:
        prices.append(float(user_input))
    except ValueError:
        print("[Ошибка] Введенное число некорректно!")
