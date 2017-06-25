# encoding: utf-8
# module System.Diagnostics.CodeAnalysis calls itself CodeAnalysis
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ExcludeFromCodeCoverageAttribute(Attribute, _Attribute):
    """
    Specifies that the attributed code should be excluded from code coverage information.
    
    ExcludeFromCodeCoverageAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class SuppressMessageAttribute(Attribute, _Attribute):
    """
    Suppresses reporting of a specific static analysis tool rule violation, allowing multiple suppressions on a single code artifact.
    
    SuppressMessageAttribute(category: str, checkId: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, category, checkId):
        """ __new__(cls: type, category: str, checkId: str) """
        pass

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the category identifying the classification of the attribute.

Get: Category(self: SuppressMessageAttribute) -> str

"""

    CheckId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the identifier of the static analysis tool rule to be suppressed.

Get: CheckId(self: SuppressMessageAttribute) -> str

"""

    Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the justification for suppressing the code analysis message.

Get: Justification(self: SuppressMessageAttribute) -> str

Set: Justification(self: SuppressMessageAttribute) = value
"""

    MessageId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an optional argument expanding on exclusion criteria.

Get: MessageId(self: SuppressMessageAttribute) -> str

Set: MessageId(self: SuppressMessageAttribute) = value
"""

    Scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope of the code that is relevant for the attribute.

Get: Scope(self: SuppressMessageAttribute) -> str

Set: Scope(self: SuppressMessageAttribute) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a fully qualified path that represents the target of the attribute.

Get: Target(self: SuppressMessageAttribute) -> str

Set: Target(self: SuppressMessageAttribute) = value
"""



