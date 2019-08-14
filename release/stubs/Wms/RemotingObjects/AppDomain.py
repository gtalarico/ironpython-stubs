# encoding: utf-8
# module Wms.RemotingObjects.AppDomain calls itself AppDomain
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AppDomainInformation():
    """
    AppDomainInformation(appDomainName: str, lifetime: TimeSpan)
    AppDomainInformation()
    """
    Instance = AppDomainInformation
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, appDomainName=None, lifetime=None):
        """
        __new__(cls: type, appDomainName: str, lifetime: TimeSpan)
        __new__(cls: type)
        """
        pass

    AppDomainName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AppDomainName(self: AppDomainInformation) -> str

Set: AppDomainName(self: AppDomainInformation) = value
"""

    Lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Lifetime(self: AppDomainInformation) -> TimeSpan

Set: Lifetime(self: AppDomainInformation) = value
"""

    LifetimeString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LifetimeString(self: AppDomainInformation) -> str

"""



