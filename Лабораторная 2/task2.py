money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
months = 0
current_budget = money_capital

while True:
    current_budget += salary
    if current_budget < spend:
        break
    current_budget -= spend
    spend += spend * increase
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)