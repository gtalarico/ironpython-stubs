# encoding: utf-8
# module Wms.RemotingImplementation.StateMachine calls itself StateMachine
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class State():
    # no doc
    def Next(self):
        """ Next(self: State) -> State """
        pass

    def Run(self, args):
        """ Run(self: State, *args: Array[object]) -> Array[object] """
        pass

    Instance = State()
    """hardcoded/returns an instance of the class"""

class StateMachine():
    """
    StateMachine(initialState: State, *args: Array[object])
    StateMachine(uniqueId: str, initialState: State, mapper: Func[str, State], *args: Array[object])
    """
    def Run(self):
        """ Run(self: StateMachine)Run[TResult](self: StateMachine) -> TResult """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, initialState: State, *args: Array[object])
        __new__(cls: type, uniqueId: str, initialState: State, mapper: Func[str, State], *args: Array[object])
        """
        pass

    Instance = StateMachine()
    """hardcoded/returns an instance of the class"""

# variables with complex values

