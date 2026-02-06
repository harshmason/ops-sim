import random

class Asset:

    def __init__(self, name, failure_rate, repair_time, base_capacity):
        # config
        self.name = name
        self.failure_rate = failure_rate
        self.repair_time = repair_time
        self.base_capacity = base_capacity #tons an hour?

        # state
        self.status = "RUNNING"
        self.last_event = None
        self.repair_remaining = 0


    def step(self, dt): #dt is minutes
        if self.status == "DOWN":
            self.repair_remaining -= dt
            if self.repair_remaining <= 0:
                self.repair()
            return
        
        p = self.failure_rate * (dt / 60.0)
        if random.random() < p:
            self.fail()
        """TODO: check logic. """


    def fail(self):
        self.status = "DOWN"
        self.repair_remaining = self.repair_time
        self.last_event = f"{self.name} failed"


    def repair(self):
        self.status = "RUNNING"
        self.repair_remaining = 0
        self.last_event = f"{self.name} repaired"


    def get_output(self):
        if self.status == "DOWN":
            return 0
        else:
            return self.base_capacity
        """TODO: 0 if down.. Base output for ?"""

class Crusher(Asset):
    pass
    """TODO: Add stuff speicific to crusher.. Atts + methods"""


class Conveyor(Asset):
    pass
    """TODO: Add specifics"""

class Truck(Asset):
    pass
    """TODO: Add specifics"""




