class ICommandSource:
 """ Defines an object that knows how to invoke a command. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Command=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the command that will be executed when the command source is invoked.

Get: Command(self: ICommandSource) -> ICommand

"""

 CommandParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Represents a user defined data value that can be passed to the command when it is executed.

Get: CommandParameter(self: ICommandSource) -> object

"""

 CommandTarget=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The object that the command is being executed on.

Get: CommandTarget(self: ICommandSource) -> IInputElement

"""


