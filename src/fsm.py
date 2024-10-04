# In this code, ModThreeTransition is a class that encapsulates the transition function for the mod-three problem. 
# The FSM class is a generic finite state machine that can be used for any problem that can be modeled as a FSM.
# The process_inputs method of the FSM class processes a sequence of inputs, updating the state of the FSM for each input according to the transition function. 
# The reset method resets the state of the FSM to the initial state.

class FSM:
    # The constructor takes a transition object and an initial state as parameters
    def __init__(self, transition, initial_state):
        # Store the transition object
        self.transition = transition
        # Set the initial state
        self.initial_state = initial_state
        # Set the current state to the initial state
        self.state = initial_state

    # Method to process a sequence of inputs
    def process_inputs(self, inputs):
        if inputs is None:
             raise ValueError("Invalid input: Input cannot be None.")
        if inputs == '':
             raise ValueError("Invalid input: Input cannot be an empty string.")
        for input in inputs:
            if input not in ['0', '1']:
                raise ValueError("Invalid input: Input should be a string of 1s and 0s.")
            self.state = self.transition.transition(self.state, input)
        return self.state

    # Method to reset the state to the initial state
    def reset(self):
        self.state = self.initial_state


# Define a class for the transition function of the mod-three problem
class ModThreeTransition:
    # Method to determine the next state based on the current state and input
    def transition(self, state, input):
        # Convert the input to an integer
        input = int(input)
        # If the current state is 'S0'
        if state == 'S0':
            # Return 'S1' if the input is 1, else return 'S0'
            return 'S1' if input else 'S0'
        # If the current state is 'S1'
        elif state == 'S1':
            # Return 'S0' if the input is 1, else return 'S2'
            return 'S0' if input else 'S2'
        else:  # state == 'S2'
            # Return 'S2' if the input is 1, else return 'S1'
            return 'S2' if input else 'S1'


# Create an instance of the transition function for the mod-three problem
transition = ModThreeTransition()
# Create an instance of FSM with the transition function and initial state 'S0'
fsm = FSM(transition, 'S0')

# Process a sequence of inputs and print the final state
print(fsm.process_inputs('1101'))  # Output: 'S1'
# Reset the FSM to the initial state
fsm.reset()
print(fsm.process_inputs('1110'))  # Output: 'S2'
# Reset the FSM to the initial state
fsm.reset()
print(fsm.process_inputs('1111'))  # Output: 'S0'