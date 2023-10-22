salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_spend = 0  # Общая сумма расходов за 10 месяцев
total_salary = 0  # Общая сумма зарплаты за 10 месяцев

for i in range(months):
    total_spend += spend
    total_salary += salary
    spend += spend * increase

money_capital_needed = round(total_spend - total_salary, 2)


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital_needed)