class State(object):
    def __init__(self, name, inputs, output):
        self.name = name
        self.inputs = inputs
        self.output = output

    def return_name(self):
        return self.name

    def return_input(self):
        return self.inputs

    def return_output(self):
        return self.output

class Moore(object):
    def __init__(self, name):
        self.name = name
        self.states = []

    def add_state(self, name, input1, input2, output ): # function to create some states for Moore Machine
        states = self.states
        name = State(str(name), {0: str(input1), 1: str(input2)}, output) #Input when is 0 or 1
        states.append(name)
        return states

machine = Moore('Line')
machine.add_state('s1', 's2', 's1', 1)
machine.add_state('s2', 's3', 's1', 0)
machine.add_state('s3', 's4', 's1', 1)
machine.add_state('s4', 's4', 's1', 0)
