from datetime import datetime
from configs.backend_settings import START_POINT, FINISH_POINT
from functions.path_functions import pathfinder, list_comp, calc_time
##  FOR DEBUG RUNNER
start_time = datetime.now()

data = pathfinder(START_POINT, FINISH_POINT)
ways = list_comp(data)
dict_final = calc_time(ways)
print(dict_final)
for i in dict_final:
    print(i, dict_final[i])
print(datetime.now() - start_time)
