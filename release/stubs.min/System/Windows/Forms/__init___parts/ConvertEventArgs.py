class ConvertEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Binding.Format and System.Windows.Forms.Binding.Parse events.

 

 ConvertEventArgs(value: object,desiredType: Type)
 """
 @staticmethod
 def __new__(self,value,desiredType):
  """ __new__(cls: type,value: object,desiredType: Type) """
  pass
 DesiredType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data type of the desired value.



Get: DesiredType(self: ConvertEventArgs) -> Type



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the System.Windows.Forms.ConvertEventArgs.



Get: Value(self: ConvertEventArgs) -> object



Set: Value(self: ConvertEventArgs)=value

"""


