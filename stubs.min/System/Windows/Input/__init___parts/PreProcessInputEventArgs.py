class PreProcessInputEventArgs(ProcessInputEventArgs):
    """ Provides data for preprocess input events. """
    def Cancel(self):
        """
        Cancel(self: PreProcessInputEventArgs)
            Cancels the processing of the input event.
        """
        pass

    Canceled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether processing of the input event was canceled.

Get: Canceled(self: PreProcessInputEventArgs) -> bool

"""


