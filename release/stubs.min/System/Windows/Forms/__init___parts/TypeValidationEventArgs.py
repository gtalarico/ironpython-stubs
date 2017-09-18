class TypeValidationEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.MaskedTextBox.TypeValidationCompleted event.

 

 TypeValidationEventArgs(validatingType: Type,isValidInput: bool,returnValue: object,message: str)
 """
 @staticmethod
 def __new__(self,validatingType,isValidInput,returnValue,message):
  """ __new__(cls: type,validatingType: Type,isValidInput: bool,returnValue: object,message: str) """
  pass
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the event should be canceled.



Get: Cancel(self: TypeValidationEventArgs) -> bool



Set: Cancel(self: TypeValidationEventArgs)=value

"""

 IsValidInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the formatted input string was successfully converted to the validating type.



Get: IsValidInput(self: TypeValidationEventArgs) -> bool



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a text message describing the conversion process.



Get: Message(self: TypeValidationEventArgs) -> str



"""

 ReturnValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object that results from the conversion of the formatted input string.



Get: ReturnValue(self: TypeValidationEventArgs) -> object



"""

 ValidatingType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type that the formatted input string is being validated against.



Get: ValidatingType(self: TypeValidationEventArgs) -> Type



"""


