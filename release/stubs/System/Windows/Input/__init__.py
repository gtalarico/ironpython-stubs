# encoding: utf-8
# module System.Windows.Input calls itself Input
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ICommand:
    # no doc
    def CanExecute(self, parameter):
        """ CanExecute(self: ICommand, parameter: object) -> bool """
        pass

    def Execute(self, parameter):
        """ Execute(self: ICommand, parameter: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanExecuteChanged = None


