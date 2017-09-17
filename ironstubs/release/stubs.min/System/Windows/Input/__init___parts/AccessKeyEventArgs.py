class AccessKeyEventArgs(EventArgs):
 """ Provides information for access keys events. """
 IsMultiple=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether other elements are invoked by the key.

Get: IsMultiple(self: AccessKeyEventArgs) -> bool

"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access keys that was pressed.

Get: Key(self: AccessKeyEventArgs) -> str

"""


