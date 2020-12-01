# Author: Vincent Gustafsson - 2020-11-25
# Uträkning (facepalm) 6 x 3 x 5 / 216
from datetime import datetime
from progressbar import progressbar
from collections import Counter
import random, sys

startTime = datetime.now()
num_of_passes = int(sys.argv[1])


def simulate(times):
	occurence = 0
	for i in progressbar(range(times)):
		random_numbers = [random.randint(1, 6) for _ in range(3)]
		occurence += 1 if 2 in Counter(random_numbers).values() else 0
	return occurence

simulation = simulate(num_of_passes)

print(f'''
Rolls (simulations): {num_of_passes:,}		Pairs: {simulation}		Time: {datetime.now() - startTime}
No Pairs (%): {(num_of_passes - simulation) / num_of_passes:.2%} 			Pairs (%): {simulation / num_of_passes:.2%}
	   ''')
