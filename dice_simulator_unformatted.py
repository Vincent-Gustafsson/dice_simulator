from datetime import datetime
from progressbar import progressbar
from collections import Counter
import random
import sys

startTime = datetime.now()
num_of_passes = int(sys.argv[1])


def numbers_generator():
    num_list = []
    for i in range(3):
        random_number = random.randint(1, 6)
        num_list.append(random_number)
    return num_list


def check_occurence(num_list):
	if 2 in Counter(num_list).values():
		return 1
	else:
		return 0
	

def simulator(times):
	occurence = 0
	for i in progressbar(range(times)):
		occurence += check_occurence(numbers_generator())
	return occurence


pairs = simulator(num_of_passes)

print(f'''
Rolls (simulations): {num_of_passes:,}		Pairs: {simulation}		Time: {datetime.now() - startTime}
No Pairs (%): {(num_of_passes - simulation) / num_of_passes:.2%} 			Pairs (%): {simulation / num_of_passes:.2%}
	   ''')