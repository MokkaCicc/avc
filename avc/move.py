class Move:
    def __init__(
        self,
        use_angle: bool,
        position: dict,
        start_wait: float,
        transition_time: float,
        end_wait: float
    ):
        self.use_angle = use_angle
        self.position = position
        self.start_wait = start_wait
        self.transition_time = transition_time
        self.end_wait = end_wait


    def __repr__(self):
        if self.use_angle:
            s = "Move to angles : "
            unit = "°"
        else:
            s = "Move to positions : "
            unit = "cm"

        s += "\n{"
        for key, value in self.position.items():
            s += f"\n\t['{key}'] : {value}{unit}"
        s += "\n}"

        s += f"\nWait at start : {self.start_wait}s"
        s += f"\nTransition time : {self.transition_time}s"
        s += f"\nWait at end : {self.end_wait}s"

        return s