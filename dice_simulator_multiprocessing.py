# Author: Vincent Gustafsson - 2020-11-25
# Uträkning (facepalm) 6 x 3 x 5 / 216
from multiprocessing import Pool, cpu_count
from collections import Counter
from datetime import datetime
import random, sys


def simulate(times):
	occurence = 0
	for i in range(times):
		random_numbers = [random.randint(1, 6) for _ in range(3)]
		occurence += 1 if 2 in Counter(random_numbers).values() else 0
	return occurence


if __name__ == '__main__':
	num_of_passes = int(sys.argv[1])
	startTime = datetime.now()
	result = 0
	
	with Pool(processes=cpu_count()) as pool:
		result = pool.map(simulate, [num_of_passes])[0]
		

	print(f'''
	Rolls (simulations): {num_of_passes:,}		Pairs: {result}		Time: {datetime.now() - startTime}
	No Pairs (%): {(num_of_passes - result) / num_of_passes:.2%} 			Pairs (%): {result / num_of_passes:.2%}
	   ''')
