# encoding: utf-8
# module Wms.RemotingImplementation.StateMachine calls itself StateMachine
# from Wms.RemotingImplementation, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class State:
    # no doc
    def Next(self):
        """ Next(self: State) -> State """
        pass

    def Run(self, args):
        """ Run(self: State, *args: Array[object]) -> Array[object] """
        pass


class StateMachine:
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


# variables with complex values

