from app import app
from flask import jsonify
from configs.backend_settings import START_POINT, FINISH_POINT
from functions.path_functions import pathfinder, list_comp, calc_time


@app.route('/pathfinder')
def index():
    # NEED DOC PAGE
    data = pathfinder(START_POINT, FINISH_POINT)
    ways = list_comp(data)
    dict_final = calc_time(ways)
    return jsonify(dict_final)


@app.route('/pathfinder/api/<start>/<finish>')
def path_jsn(start, finish):
    data = pathfinder(start, finish)
    ways = list_comp(data)
    try:
        dict_final = calc_time(ways)
    except KeyError:
        dict_final = {0: '404'}
    return jsonify(dict_final)