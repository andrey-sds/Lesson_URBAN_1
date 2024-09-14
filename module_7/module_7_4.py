team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = int(input('Количество участников %s: ' % team1))
print('В команде %(name)s участников: %(count)d' % {'name': team1, 'count': team1_num})
team2_num = int(input('Количество участников %s: ' % team2))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

score_1 = int(input('Мастера кода решила задач:'))
score_2 = int(input('Волшебники данных решила задач:'))
print('Команда {} решила задач: {}!'.format(team2, score_2))
team1_time = float(input(f'Время решения задач {team1}: '))
team2_time = float(input(f'Время решения задач {team2}: '))
print('Волшебники данных решили задачи за {} c!'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg,2)} секунды на задачу!')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f'{challenge_result}')

