import json
import glob
import copy

from avc import Move
from avc import Routine


class AvcParser:
    def __init__(self):
        self.cached_routines = dict()


    def cache_routines(self, folder_path:str):
        routines = self.parse_routines(folder_path)
        self.cached_routines = routines


    def parse_routine(self, json_path:str):
        with open(json_path, 'r') as json_file:
            json_data = json.load(json_file)

        moves = list()
        # parse each move of the routine
        try:
            name = json_data['name']

            for move_data in json_data['moves']:
                len_position = len(move_data['position'])
                use_angle = True if len_position == 6 else False
                move = Move(use_angle, **move_data)
                moves.append(move)
        except:
            raise Exception(f"Wrong json structure in {json_path}")

        routine = Routine(name, moves)
        return routine


    def parse_routines(self, folder_path:str):
        json_paths = glob.glob(f"{folder_path}/*.json")

        routines = dict()
        # parse each routine
        for json_path in json_paths:
            routine = self.parse_routine(json_path)
            name = routine.name
            routines[name] = routine

        return routines


    def parse_choregraphy(self, json_path:str):
        with open(json_path, 'r') as json_file:
            json_data = json.load(json_file)


        routines = list()
        # build the choregraphy from the cached routines
        try:
            name = json_data['name']

            for routine_data in json_data['routines']:
                routine_name = routine_data['name']
                routine = copy.deepcopy(self.cached_routines[routine_name])
                del routine_data['name']
                routine.customize_routine(**routine_data)
                routines.append(routine)
        except:
            raise Exception(f"Wrong json structure in {json_path}")

        return name, routines