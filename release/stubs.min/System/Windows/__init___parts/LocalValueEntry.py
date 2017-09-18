class LocalValueEntry(object):
 """ Represents a property identifier and the property value for a locally set dependency property. """
 def Equals(self,obj):
  """
  Equals(self: LocalValueEntry,obj: object) -> bool
  
   Determines whether two System.Windows.LocalValueEntry instances are equal.
  
   obj: The System.Windows.LocalValueEntry to compare with the current 
    System.Windows.LocalValueEntry.
  
   Returns: This 
    System.Windows.LocalValueEntry.op_Equality(System.Windows.LocalValueEntry,System
    .Windows.LocalValueEntry) implementation compares the values of the 
    System.Windows.LocalValueEntry.Property,and potentially compares the values of 
    System.Windows.LocalValueEntry.Value. The 
    System.Windows.LocalValueEntry.Property component of a 
    System.Windows.LocalValueEntry is a value type,so will always be a bitwise 
    comparison. For the System.Windows.LocalValueEntry.Value component,this 
    implementation employs a bitwise comparison if it is a value type. For locally 
    set properties that have reference types,the behavior is deferred to that 
    type's equality determination mechanisms,because it just uses the == operator 
    on the two values internally. By default,this would be a reference equality of 
    the values and thus the equality of the entire System.Windows.LocalValueEntry 
    would become a reference equality.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: LocalValueEntry) -> int
  
   Returns the hash code for this System.Windows.LocalValueEntry.
   Returns: A signed 32-bit integer value.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 Property=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the identifier for the locally set dependency property that is represented by this entry.

Get: Property(self: LocalValueEntry) -> DependencyProperty

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the locally set dependency property.

Get: Value(self: LocalValueEntry) -> object

"""


