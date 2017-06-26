class DragEventArgs(RoutedEventArgs):
    """ Contains arguments relevant to all drag-and-drop events (System.Windows.DragDrop.DragEnter, System.Windows.DragDrop.DragLeave, System.Windows.DragDrop.DragOver, and System.Windows.DragDrop.Drop). """
    def GetPosition(self, relativeTo):
        """
        GetPosition(self: DragEventArgs, relativeTo: IInputElement) -> Point
        
            Returns a drop point that is relative to a specified System.Windows.IInputElement.
        
            relativeTo: An System.Windows.IInputElement object for which to get a relative drop point.
            Returns: A drop point that is relative to the element specified in relativeTo.
        """
        pass

    AllowedEffects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a member of the System.Windows.DragDropEffects enumeration that specifies which operations are allowed by the originator of the drag event.

Get: AllowedEffects(self: DragEventArgs) -> DragDropEffects

"""

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a data object that contains the data associated with the corresponding drag event.

Get: Data(self: DragEventArgs) -> IDataObject

"""

    Effects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target drag-and-drop operation.

Get: Effects(self: DragEventArgs) -> DragDropEffects

Set: Effects(self: DragEventArgs) = value
"""

    KeyStates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag enumeration indicating the current state of the SHIFT, CTRL, and ALT keys, as well as the state of the mouse buttons.

Get: KeyStates(self: DragEventArgs) -> DragDropKeyStates

"""


