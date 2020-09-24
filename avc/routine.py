from avc import Move


class Routine:
    def __init__(self, name:str, moves:list):
        self.name = name
        self.moves = moves
        self.is_customized = False
        self.start_wait = None
        self.transition_time = None
        self.end_wait = None


    def customize_routine(
        self,
        start_wait:float,
        transition_time:float,
        end_wait:float
    ):
        self.is_customized = True
        self.start_wait = start_wait
        self.transition_time = transition_time
        self.end_wait = end_wait


    def __repr__(self):
        s = f"Routine '{self.name}'"
        if self.is_customized:
            s += f"\nWait at start : {self.start_wait}s"
            s += f"\nTransition time : {self.transition_time}s"
            s += f"\nWait at end : {self.end_wait}s"
        else:
            s += f"\nThe routine is not customized"

        for i in range(len(self.moves)):
            s += "\n\n"
            s += f"Move n°{i+1}\n"
            s += str(self.moves[i])

        return s
