from datetime import datetime
from configs.defaults import START_POINT, FINISH_POINT
from functions.path_functions import pathfinder, list_comp, calc_time

start_time = datetime.now()

data = pathfinder(START_POINT, FINISH_POINT)
ways = list_comp(data)
calc_time(ways)
print(datetime.now() - start_time)
