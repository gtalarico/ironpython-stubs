class AddInCommandBinding(object):
 """
 This object represents a binding between a Revit command and one or more handlers which 
 override the behavior of the command in Revit.
 """
 RevitCommandId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Revit command Id.

Get: RevitCommandId(self: AddInCommandBinding) -> RevitCommandId

"""


 BeforeExecuted=None
 CanExecute=None
 Executed=None

