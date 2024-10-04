import unittest
from fsm import ModThreeTransition, FSM

# Define a test class for the FSM and ModThreeTransition classes
class TestFSM(unittest.TestCase):
    # Set up the test environment before each test
    def setUp(self):
        # Create a ModThreeTransition object
        self.transition = ModThreeTransition()
        # Create an FSM object with the ModThreeTransition object and initial state 'S0'
        self.fsm = FSM(self.transition, 'S0')

    # Test the process_inputs method with various valid inputs
    def test_process_inputs(self):
        # Assert that the final state is 'S1' after processing the input '1101'
        self.assertEqual(self.fsm.process_inputs('1101'), 'S1')
        # Reset the FSM to the initial state
        self.fsm.reset()
        # Assert that the final state is 'S2' after processing the input '1110'
        self.assertEqual(self.fsm.process_inputs('1110'), 'S2')
        # Reset the FSM to the initial state
        self.fsm.reset()
        # Assert that the final state is 'S0' after processing the input '1111'
        self.assertEqual(self.fsm.process_inputs('1111'), 'S0')
        # Reset the FSM to the initial state
        self.fsm.reset()
        # Assert that the final state is 'S0' after processing the input '0000'
        self.assertEqual(self.fsm.process_inputs('0000'), 'S0')
        # Reset the FSM to the initial state
        self.fsm.reset()

    # Test the process_inputs method with various invalid inputs
    def test_process_inputs_unhappy_path(self):
        # Assert that a ValueError is raised when the input contains a non-binary character
        with self.assertRaises(ValueError):
            self.fsm.process_inputs('110a')  # contains a non-binary character
        # Assert that a ValueError is raised when the input is None
        with self.assertRaises(ValueError):
            self.fsm.process_inputs(None)  # None input
        # Assert that a ValueError is raised when the input is an empty string
        with self.assertRaises(ValueError):
            self.fsm.process_inputs('')  # empty string

    # Test the reset method
    def test_reset(self):
        # Process an input
        self.fsm.process_inputs('1101')
        # Reset the FSM to the initial state
        self.fsm.reset()
        # Assert that the state of the FSM is the initial state
        self.assertEqual(self.fsm.state, 'S0')

    # Test all possible transitions of the ModThreeTransition class
    def test_transition(self):
        # Assert that the next state is 'S0' when the current state is 'S0' and the input is '0'
        self.assertEqual(self.transition.transition('S0', '0'), 'S0')
        # Assert that the next state is 'S1' when the current state is 'S0' and the input is '1'
        self.assertEqual(self.transition.transition('S0', '1'), 'S1')
        # Assert that the next state is 'S2' when the current state is 'S1' and the input is '0'
        self.assertEqual(self.transition.transition('S1', '0'), 'S2')
        # Assert that the next state is 'S0' when the current state is 'S1' and the input is '1'
        self.assertEqual(self.transition.transition('S1', '1'), 'S0')
        # Assert that the next state is 'S1' when the current state is 'S2' and the input is '0'
        self.assertEqual(self.transition.transition('S2', '0'), 'S1')
        # Assert that the next state is 'S2' when the current state is 'S2' and the input is '1'
        self.assertEqual(self.transition.transition('S2', '1'), 'S2')

if __name__ == '__main__':
    unittest.main()