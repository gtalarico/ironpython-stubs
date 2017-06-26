class CollectionChangeEventArgs(EventArgs):
    """
    Provides data for the System.Data.DataColumnCollection.CollectionChanged event.
    
    CollectionChangeEventArgs(action: CollectionChangeAction, element: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, action, element):
        """ __new__(cls: type, action: CollectionChangeAction, element: object) """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an action that specifies how the collection changed.

Get: Action(self: CollectionChangeEventArgs) -> CollectionChangeAction

"""

    Element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the instance of the collection with the change.

Get: Element(self: CollectionChangeEventArgs) -> object

"""


