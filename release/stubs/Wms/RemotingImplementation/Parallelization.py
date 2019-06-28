# encoding: utf-8
# module Wms.RemotingImplementation.Parallelization calls itself Parallelization
# from Wms.RemotingImplementation, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Parallel:
    # no doc
    @staticmethod
    def ForEach(actions):
        """ ForEach(actions: List[Action]) """
        pass

    __all__ = [
        'ForEach',
    ]


class Sequential:
    # no doc
    @staticmethod
    def ForEach(items, action):
        """ ForEach[T](items: IEnumerable[T], action: Action[T]) """
        pass

    __all__ = [
        'ForEach',
    ]


