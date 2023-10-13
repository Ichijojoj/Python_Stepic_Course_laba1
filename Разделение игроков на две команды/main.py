list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

total_number_of_players = len(list_players)
half = total_number_of_players // 2
comand1 = list_players[:half]
comand2 = list_players[half:]

print(comand1)
print(comand2)