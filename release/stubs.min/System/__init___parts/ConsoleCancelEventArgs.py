class ConsoleCancelEventArgs(EventArgs):
 """ Provides data for the System.Console.CancelKeyPress event. This class cannot be inherited. """
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether simultaneously pressing the System.ConsoleModifiers.Control modifier key and System.ConsoleKey.C console key (CTRL+C) terminates the current process.



Get: Cancel(self: ConsoleCancelEventArgs) -> bool



Set: Cancel(self: ConsoleCancelEventArgs)=value

"""

 SpecialKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the combination of modifier and console keys that interrupted the current process.



Get: SpecialKey(self: ConsoleCancelEventArgs) -> ConsoleSpecialKey



"""


