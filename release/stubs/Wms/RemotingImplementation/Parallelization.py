# encoding: utf-8
# module Wms.RemotingImplementation.Parallelization calls itself Parallelization
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Parallel():
    # no doc
    Instance = Parallel
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def ForEach(actions):
        """ ForEach(actions: List[Action]) """
        pass

    __all__ = [
        'ForEach',
    ]


class Sequential():
    # no doc
    Instance = Sequential
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def ForEach(items, action):
        """ ForEach[T](items: IEnumerable[T], action: Action[T]) """
        pass

    __all__ = [
        'ForEach',
    ]


