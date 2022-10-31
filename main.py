# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line




player_1='Ruud Gullit'
player_2='Marco van Basten'

goal_0=32
goal_1=54




scorers=f'Ruud Gullit {goal_0}, Marco van Basten {goal_1}'

report=f'{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute'


player='Ronald Koeman'
first_name=player[:player.find(' ')]
last_name=player[7:]#kom hier niet uit mbt find/slice


last_name_len=len(last_name)
first_name_len=len(first_name)

name_short=player[:player.find(' ')-5] +f'. {last_name}'

chant='Ronald! '*first_name_len

chant=chant[:-1]



good_chant=chant[-1] != ' '
print(name_short)

""" 

Beste C.Verlaan,
Ik kom er niet uit met de find/slice functie  mbt de last_name!
Hoe kan ik Koeman nu opzoeken zoals ik (dmv jouw hulp) Ronald heb opgezocht?
Hierdoor is last_name_len ook niet conform opdracht!
Thanks voor je feedback..

Gr Jermaine

"""




















        



