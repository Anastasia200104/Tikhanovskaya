list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
vsego = len(list_players)
polovina = int(vsego / 2)

print(list_players[:polovina])
print(list_players[polovina:])