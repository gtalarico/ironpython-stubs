class InputGesture(object):
    """ Abstract class that describes input device gestures. """
    def Matches(self, targetElement, inputEventArgs):
        """
        Matches(self: InputGesture, targetElement: object, inputEventArgs: InputEventArgs) -> bool
        
            When overridden in a derived class, determines whether the specified System.Windows.Input.InputGesture matches the input associated with the specified System.Windows.Input.InputEventArgs object.
        
            targetElement: The target of the command.
            inputEventArgs: The input event data to compare this gesture to.
            Returns: true if the gesture matches the input; otherwise, false.
        """
        pass

