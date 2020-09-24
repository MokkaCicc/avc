from avc import AvcParser


class Choregraphy:
    def __init__(self):
        self.name = None
        self.parser = AvcParser()
        self.routines = list()


    def load_choregraphy(self, routines_folder_path:str, choregraphy_json_path:str):
        if not self.parser.cached_routines:
            self.parser.cache_routines(routines_folder_path)
        name, routines = self.parser.parse_choregraphy(choregraphy_json_path)
        self.name = name
        self.routines = routines


    def __repr__(self):
        if not self.name:
            s = "No choregraphy charged"
        else:
            s = "----------------------------------------"
            s += f"\nChoregraphy '{self.name}'"

            for i in range(len(self.routines)):
                s += "\n\n"
                s += "------------------"
                s += f"\nRoutine n°{i+1}\n"
                s += str(self.routines[i])

        return s