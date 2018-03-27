import json
from datetime import datetime
start_time = datetime.now()
with open('data/paths.json') as json_data:
    graf = json.load(json_data)

with open('data/way_types.json') as json_data:
    way_types = json.load(json_data)

START_POINT = '12'
FINISH_POINT = '11'


def find_all_pathes(start, finish, path_index, good_pathes, pathes):
    path = list(pathes[path_index])
    path.append(start)
    pathes.append(path)
    for next_point in graf[start]['links']:
        count = 0
        if next_point in path:
            pass
        else:
            if next_point == finish:
                count += 1
                path.append(next_point)
                good_path = path[1:]
                good_pathes.append(good_path)
            else:
                count += 1
                index = pathes.index(path)
                find_all_pathes(next_point, finish, index, good_pathes, pathes)
            if count == 0:
                pathes.remove(path)


def pathfinder(start_point, finish_point):
    gp = []
    p = [[START_POINT], ]
    find_all_pathes(start_point, finish_point, 0, gp, p)
    return gp


def list_minus(inner_data, i1, i2):
    return len(set(inner_data[i1]) - set(inner_data[i2]))


def list_comp(input_path):
    out_path = list(input_path)
    for path1_ind in range(0, len(out_path)):
        for path2_ind in range(0, len(out_path)):
            if list_minus(out_path, path1_ind, path2_ind) == 0 and list_minus(out_path, path2_ind, path1_ind) != 0:
                out_path[path2_ind] = 'not_optimal'
    ihave = True
    while ihave:
        try:
            out_path.remove('not_optimal')
        except ValueError:
            ihave = False
    return out_path


def calc_time(dataset):
    for line in dataset:
        time = 0
        for i in range(0, len(line) - 1):
            time += int(graf[line[i]]['links'][line[i+1]])
            way_type = calc_way_type(line[i], line[i+1])
            # if way_type == 0:

            print('{} from {} to {}, {} minutes'.format(way_types[str(way_type)],
                                                        graf[line[i]]['name'],
                                                        graf[line[i+1]]['name'],
                                                        graf[line[i]]['links'][line[i+1]]))
        print(time, 'min')
        print('========================')


def calc_way_type(point1, point2):
    """
    :param point1:
    :param point2:
    :return:
    0 - subtrain
    1 - subway
    2 - change
    3 - walk
    """
    start_type = graf[point1]['type']
    finish_type = graf[point2]['type']
    if start_type == 'walk' or finish_type == 'walk':
        return 3
    elif start_type == finish_type and start_type == 'subtrain':
        return 0
    elif start_type == finish_type and start_type == 'subway':
        return 1
    return 2


data = pathfinder(START_POINT, FINISH_POINT)
ways = list_comp(data)
calc_time(ways)
print(datetime.now() - start_time)
