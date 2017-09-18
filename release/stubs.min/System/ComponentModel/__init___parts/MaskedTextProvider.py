class MaskedTextProvider(object,ICloneable):
 """
 Represents a mask-parsing service that can be used by any number of controls that support masking,such as the System.Windows.Forms.MaskedTextBox control.

 

 MaskedTextProvider(mask: str)

 MaskedTextProvider(mask: str,restrictToAscii: bool)

 MaskedTextProvider(mask: str,culture: CultureInfo)

 MaskedTextProvider(mask: str,culture: CultureInfo,restrictToAscii: bool)

 MaskedTextProvider(mask: str,passwordChar: Char,allowPromptAsInput: bool)

 MaskedTextProvider(mask: str,culture: CultureInfo,passwordChar: Char,allowPromptAsInput: bool)

 MaskedTextProvider(mask: str,culture: CultureInfo,allowPromptAsInput: bool,promptChar: Char,passwordChar: Char,restrictToAscii: bool)
 """
 def Add(self,input,testPosition=None,resultHint=None):
  """
  Add(self: MaskedTextProvider,input: str) -> bool

  

   Adds the characters in the specified input string to the end of the formatted string.

  

   input: A System.String containing character values to be appended to the formatted string.

   Returns: true if all the characters from the input string were added successfully; otherwise false to 

    indicate that no characters were added.

  

  Add(self: MaskedTextProvider,input: str) -> (bool,int,MaskedTextResultHint)

  

   Adds the characters in the specified input string to the end of the formatted string,and then 

    outputs position and descriptive information.

  

  

   input: A System.String containing character values to be appended to the formatted string.

   Returns: true if all the characters from the input string were added successfully; otherwise false to 

    indicate that no characters were added.

  

  Add(self: MaskedTextProvider,input: Char) -> bool

  

   Adds the specified input character to the end of the formatted string.

  

   input: A System.Char value to be appended to the formatted string.

   Returns: true if the input character was added successfully; otherwise false.

  Add(self: MaskedTextProvider,input: Char) -> (bool,int,MaskedTextResultHint)

  

   Adds the specified input character to the end of the formatted string,and then outputs position 

    and descriptive information.

  

  

   input: A System.Char value to be appended to the formatted string.

   Returns: true if the input character was added successfully; otherwise false.
  """
  pass
 def Clear(self,resultHint=None):
  """
  Clear(self: MaskedTextProvider) -> MaskedTextResultHint

  

   Clears all the editable input characters from the formatted string,replacing them with prompt 

    characters,and then outputs descriptive information.

  

  Clear(self: MaskedTextProvider)

   Clears all the editable input characters from the formatted string,replacing them with prompt 

    characters.
  """
  pass
 def Clone(self):
  """
  Clone(self: MaskedTextProvider) -> object

  

   Creates a copy of the current System.ComponentModel.MaskedTextProvider.

   Returns: The System.ComponentModel.MaskedTextProvider object this method creates,cast as an object.
  """
  pass
 def FindAssignedEditPositionFrom(self,position,direction):
  """
  FindAssignedEditPositionFrom(self: MaskedTextProvider,position: int,direction: bool) -> int

  

   Returns the position of the first assigned editable position after the specified position using 

    the specified search direction.

  

  

   position: The zero-based position in the formatted string to start the search.

   direction: A System.Boolean indicating the search direction; either true to search forward or false to 

    search backward.

  

   Returns: If successful,an System.Int32 representing the zero-based position of the first assigned 

    editable position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
  """
  pass
 def FindAssignedEditPositionInRange(self,startPosition,endPosition,direction):
  """
  FindAssignedEditPositionInRange(self: MaskedTextProvider,startPosition: int,endPosition: int,direction: bool) -> int

  

   Returns the position of the first assigned editable position between the specified positions 

    using the specified search direction.

  

  

   startPosition: The zero-based position in the formatted string where the search starts.

   endPosition: The zero-based position in the formatted string where the search ends.

   direction: A System.Boolean indicating the search direction; either true to search forward or false to 

    search backward.

  

   Returns: If successful,an System.Int32 representing the zero-based position of the first assigned 

    editable position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
  """
  pass
 def FindEditPositionFrom(self,position,direction):
  """
  FindEditPositionFrom(self: MaskedTextProvider,position: int,direction: bool) -> int

  

   Returns the position of the first editable position after the specified position using the 

    specified search direction.

  

  

   position: The zero-based position in the formatted string to start the search.

   direction: A System.Boolean indicating the search direction; either true to search forward or false to 

    search backward.

  

   Returns: If successful,an System.Int32 representing the zero-based position of the first editable 

    position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
  """
  pass
 def FindEditPositionInRange(self,startPosition,endPosition,direction):
  """
  FindEditPositionInRange(self: MaskedTextProvider,startPosition: int,endPosition: int,direction: bool) -> int

  

   Returns the position of the first editable position between the specified positions using the 

    specified search direction.

  

  

   startPosition: The zero-based position in the formatted string where the search starts.

   endPosition: The zero-based position in the formatted string where the search ends.

   direction: A System.Boolean indicating the search direction; either true to search forward or false to 

    search backward.

  

   Returns: If successful,an System.Int32 representing the zero-based position of the first editable 

    position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
  """
  pass
 def FindNonEditPositionFrom(self,position,direction):
  """
  FindNonEditPositionFrom(self: MaskedTextProvider,position: int,direction: bool) -> int

  

   Returns the position of the first non-editable position after the specified position using the 

    specified search direction.

  

  

   position: The zero-based position in the formatted string to start the search.

   direction: A System.Boolean indicating the search direction; either true to search forward or false to 

    search backward.

  

   Returns: If successful,an System.Int32 representing the zero-based position of the first literal 

    position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
  """
  pass
 def FindNonEditPositionInRange(self,startPosition,endPosition,direction):
  """
  FindNonEditPositionInRange(self: MaskedTextProvider,startPosition: int,endPosition: int,direction: bool) -> int

  

   Returns the position of the first non-editable position between the specified positions using 

    the specified search direction.

  

  

   startPosition: The zero-based position in the formatted string where the search starts.

   endPosition: The zero-based position in the formatted string where the search ends.

   direction: A System.Boolean indicating the search direction; either true to search forward or false to 

    search backward.

  

   Returns: If successful,an System.Int32 representing the zero-based position of the first literal 

    position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
  """
  pass
 def FindUnassignedEditPositionFrom(self,position,direction):
  """
  FindUnassignedEditPositionFrom(self: MaskedTextProvider,position: int,direction: bool) -> int

  

   Returns the position of the first unassigned editable position after the specified position 

    using the specified search direction.

  

  

   position: The zero-based position in the formatted string to start the search.

   direction: A System.Boolean indicating the search direction; either true to search forward or false to 

    search backward.

  

   Returns: If successful,an System.Int32 representing the zero-based position of the first unassigned 

    editable position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
  """
  pass
 def FindUnassignedEditPositionInRange(self,startPosition,endPosition,direction):
  """
  FindUnassignedEditPositionInRange(self: MaskedTextProvider,startPosition: int,endPosition: int,direction: bool) -> int

  

   Returns the position of the first unassigned editable position between the specified positions 

    using the specified search direction.

  

  

   startPosition: The zero-based position in the formatted string where the search starts.

   endPosition: The zero-based position in the formatted string where the search ends.

   direction: A System.Boolean indicating the search direction; either true to search forward or false to 

    search backward.

  

   Returns: If successful,an System.Int32 representing the zero-based position of the first unassigned 

    editable position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
  """
  pass
 @staticmethod
 def GetOperationResultFromHint(hint):
  """
  GetOperationResultFromHint(hint: MaskedTextResultHint) -> bool

  

   Determines whether the specified System.ComponentModel.MaskedTextResultHint denotes success or 

    failure.

  

  

   hint: A System.ComponentModel.MaskedTextResultHint value typically obtained as an output parameter 

    from a previous operation.

  

   Returns: true if the specified System.ComponentModel.MaskedTextResultHint value represents a success; 

    otherwise,false if it represents failure.
  """
  pass
 def InsertAt(self,input,position,testPosition=None,resultHint=None):
  """
  InsertAt(self: MaskedTextProvider,input: str,position: int) -> bool

  

   Inserts the specified string at a specified position within the formatted string.

  

   input: The System.String to be inserted.

   position: The zero-based position in the formatted string to insert the input string.

   Returns: true if the insertion was successful; otherwise,false.

  InsertAt(self: MaskedTextProvider,input: str,position: int) -> (bool,int,MaskedTextResultHint)

  

   Inserts the specified string at a specified position within the formatted string,returning the 

    last insertion position and the status of the operation.

  

  

   input: The System.String to be inserted.

   position: The zero-based position in the formatted string to insert the input string.

   Returns: true if the insertion was successful; otherwise,false.

  InsertAt(self: MaskedTextProvider,input: Char,position: int) -> bool

  

   Inserts the specified character at the specified position within the formatted string.

  

   input: The System.Char to be inserted.

   position: The zero-based position in the formatted string to insert the character.

   Returns: true if the insertion was successful; otherwise,false.

  InsertAt(self: MaskedTextProvider,input: Char,position: int) -> (bool,int,MaskedTextResultHint)

  

   Inserts the specified character at the specified position within the formatted string,returning 

    the last insertion position and the status of the operation.

  

  

   input: The System.Char to be inserted.

   position: The zero-based position in the formatted string to insert the character.

   Returns: true if the insertion was successful; otherwise,false.
  """
  pass
 def IsAvailablePosition(self,position):
  """
  IsAvailablePosition(self: MaskedTextProvider,position: int) -> bool

  

   Determines whether the specified position is available for assignment.

  

   position: The zero-based position in the mask to test.

   Returns: true if the specified position in the formatted string is editable and has not been assigned to 

    yet; otherwise false.
  """
  pass
 def IsEditPosition(self,position):
  """
  IsEditPosition(self: MaskedTextProvider,position: int) -> bool

  

   Determines whether the specified position is editable.

  

   position: The zero-based position in the mask to test.

   Returns: true if the specified position in the formatted string is editable; otherwise false.
  """
  pass
 @staticmethod
 def IsValidInputChar(c):
  """
  IsValidInputChar(c: Char) -> bool

  

   Determines whether the specified character is a valid input character.

  

   c: The System.Char value to test.

   Returns: true if the specified character contains a valid input value; otherwise false.
  """
  pass
 @staticmethod
 def IsValidMaskChar(c):
  """
  IsValidMaskChar(c: Char) -> bool

  

   Determines whether the specified character is a valid mask character.

  

   c: The System.Char value to test.

   Returns: true if the specified character contains a valid mask value; otherwise false.
  """
  pass
 @staticmethod
 def IsValidPasswordChar(c):
  """
  IsValidPasswordChar(c: Char) -> bool

  

   Determines whether the specified character is a valid password character.

  

   c: The System.Char value to test.

   Returns: true if the specified character contains a valid password value; otherwise false.
  """
  pass
 def Remove(self,testPosition=None,resultHint=None):
  """
  Remove(self: MaskedTextProvider) -> (bool,int,MaskedTextResultHint)

  

   Removes the last assigned character from the formatted string,and then outputs the removal 

    position and descriptive information.

  

   Returns: true if the character was successfully removed; otherwise,false.

  Remove(self: MaskedTextProvider) -> bool

  

   Removes the last assigned character from the formatted string.

   Returns: true if the character was successfully removed; otherwise,false.
  """
  pass
 def RemoveAt(self,*__args):
  """
  RemoveAt(self: MaskedTextProvider,startPosition: int,endPosition: int) -> (bool,int,MaskedTextResultHint)

  

   Removes the assigned characters between the specified positions from the formatted string,and 

    then outputs the removal position and descriptive information.

  

  

   startPosition: The zero-based index of the first assigned character to remove.

   endPosition: The zero-based index of the last assigned character to remove.

   Returns: true if the character was successfully removed; otherwise,false.

  RemoveAt(self: MaskedTextProvider,startPosition: int,endPosition: int) -> bool

  

   Removes the assigned characters between the specified positions from the formatted string.

  

   startPosition: The zero-based index of the first assigned character to remove.

   endPosition: The zero-based index of the last assigned character to remove.

   Returns: true if the character was successfully removed; otherwise,false.

  RemoveAt(self: MaskedTextProvider,position: int) -> bool

  

   Removes the assigned character at the specified position from the formatted string.

  

   position: The zero-based position of the assigned character to remove.

   Returns: true if the character was successfully removed; otherwise,false.
  """
  pass
 def Replace(self,input,*__args):
  """
  Replace(self: MaskedTextProvider,input: str,position: int) -> bool

  

   Replaces a range of editable characters starting at the specified position with the specified 

    string.

  

  

   input: The System.String value used to replace the existing editable characters.

   position: The zero-based position to search for the first editable character to replace.

   Returns: true if all the characters were successfully replaced; otherwise,false.

  Replace(self: MaskedTextProvider,input: str,position: int) -> (bool,int,MaskedTextResultHint)

  

   Replaces a range of editable characters starting at the specified position with the specified 

    string,and then outputs the removal position and descriptive information.

  

  

   input: The System.String value used to replace the existing editable characters.

   position: The zero-based position to search for the first editable character to replace.

   Returns: true if all the characters were successfully replaced; otherwise,false.

  Replace(self: MaskedTextProvider,input: str,startPosition: int,endPosition: int) -> (bool,int,MaskedTextResultHint)

  

   Replaces a range of editable characters between the specified starting and ending positions with 

    the specified string,and then outputs the removal position and descriptive information.

  

  

   input: The System.String value used to replace the existing editable characters.

   startPosition: The zero-based position in the formatted string where the replacement starts.

   endPosition: The zero-based position in the formatted string where the replacement ends.

   Returns: true if all the characters were successfully replaced; otherwise,false.

  Replace(self: MaskedTextProvider,input: Char,position: int) -> bool

  

   Replaces a single character at or beyond the specified position with the specified character 

    value.

  

  

   input: The System.Char value that replaces the existing value.

   position: The zero-based position to search for the first editable character to replace.

   Returns: true if the character was successfully replaced; otherwise,false.

  Replace(self: MaskedTextProvider,input: Char,position: int) -> (bool,int,MaskedTextResultHint)

  

   Replaces a single character at or beyond the specified position with the specified character 

    value,and then outputs the removal position and descriptive information.

  

  

   input: The System.Char value that replaces the existing value.

   position: The zero-based position to search for the first editable character to replace.

   Returns: true if the character was successfully replaced; otherwise,false.

  Replace(self: MaskedTextProvider,input: Char,startPosition: int,endPosition: int) -> (bool,int,MaskedTextResultHint)

  

   Replaces a single character between the specified starting and ending positions with the 

    specified character value,and then outputs the removal position and descriptive information.

  

  

   input: The System.Char value that replaces the existing value.

   startPosition: The zero-based position in the formatted string where the replacement starts.

   endPosition: The zero-based position in the formatted string where the replacement ends.

   Returns: true if the character was successfully replaced; otherwise,false.
  """
  pass
 def Set(self,input,testPosition=None,resultHint=None):
  """
  Set(self: MaskedTextProvider,input: str) -> (bool,int,MaskedTextResultHint)

  

   Sets the formatted string to the specified input string,and then outputs the removal position 

    and descriptive information.

  

  

   input: The System.String value used to set the formatted string.

   Returns: true if all the characters were successfully set; otherwise,false.

  Set(self: MaskedTextProvider,input: str) -> bool

  

   Sets the formatted string to the specified input string.

  

   input: The System.String value used to set the formatted string.

   Returns: true if all the characters were successfully set; otherwise,false.
  """
  pass
 def ToDisplayString(self):
  """
  ToDisplayString(self: MaskedTextProvider) -> str

  

   Returns the formatted string in a displayable form.

   Returns: The formatted System.String that includes prompts and mask literals.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(self: MaskedTextProvider,includePrompt: bool,includeLiterals: bool) -> str

  

   Returns the formatted string,optionally including prompt and literal characters.

  

   includePrompt: true to include prompt characters in the return string; otherwise,false.

   includeLiterals: true to include literal characters in the return string; otherwise,false.

   Returns: The formatted System.String that includes all the assigned character values and optionally 

    includes literals and prompts.

  

  ToString(self: MaskedTextProvider,includePrompt: bool,includeLiterals: bool,startPosition: int,length: int) -> str

  

   Returns a substring of the formatted string,optionally including prompt and literal characters.

  

   includePrompt: true to include prompt characters in the return string; otherwise,false.

   includeLiterals: true to include literal characters in the return string; otherwise,false.

   startPosition: The zero-based position in the formatted string where the output begins.

   length: The number of characters to return.

   Returns: If successful,a substring of the formatted System.String,which includes all the assigned 

    character values and optionally includes literals and prompts; otherwise the System.String.Empty 

    string.

  

  ToString(self: MaskedTextProvider,ignorePasswordChar: bool,includePrompt: bool,includeLiterals: bool,startPosition: int,length: int) -> str

  

   Returns a substring of the formatted string,optionally including prompt,literal,and password 

    characters.

  

  

   ignorePasswordChar: true to return the actual editable characters; otherwise,false to indicate that the 

    System.ComponentModel.MaskedTextProvider.PasswordChar property is to be honored.

  

   includePrompt: true to include prompt characters in the return string; otherwise,false.

   includeLiterals: true to return literal characters in the return string; otherwise,false.

   startPosition: The zero-based position in the formatted string where the output begins.

   length: The number of characters to return.

   Returns: If successful,a substring of the formatted System.String,which includes all the assigned 

    character values and optionally includes literals,prompts,and password characters; otherwise 

    the System.String.Empty string.

  

  ToString(self: MaskedTextProvider,ignorePasswordChar: bool,startPosition: int,length: int) -> str

  

   Returns a substring of the formatted string,optionally including password characters.

  

   ignorePasswordChar: true to return the actual editable characters; otherwise,false to indicate that the 

    System.ComponentModel.MaskedTextProvider.PasswordChar property is to be honored.

  

   startPosition: The zero-based position in the formatted string where the output begins.

   length: The number of characters to return.

   Returns: If successful,a substring of the formatted System.String,which includes literals,prompts,and 

    optionally password characters; otherwise the System.String.Empty string.

  

  ToString(self: MaskedTextProvider) -> str

  

   Returns the formatted string that includes all the assigned character values.

   Returns: The formatted System.String that includes all the assigned character values.

  ToString(self: MaskedTextProvider,ignorePasswordChar: bool) -> str

  

   Returns the formatted string,optionally including password characters.

  

   ignorePasswordChar: true to return the actual editable characters; otherwise,false to indicate that the 

    System.ComponentModel.MaskedTextProvider.PasswordChar property is to be honored.

  

   Returns: The formatted System.String that includes literals,prompts,and optionally password characters.

  ToString(self: MaskedTextProvider,startPosition: int,length: int) -> str

  

   Returns a substring of the formatted string.

  

   startPosition: The zero-based position in the formatted string where the output begins.

   length: The number of characters to return.

   Returns: If successful,a substring of the formatted System.String,which includes all the assigned 

    character values; otherwise the System.String.Empty string.
  """
  pass
 def VerifyChar(self,input,position,hint):
  """
  VerifyChar(self: MaskedTextProvider,input: Char,position: int) -> (bool,MaskedTextResultHint)

  

   Tests whether the specified character could be set successfully at the specified position.

  

   input: The System.Char value to test.

   position: The position in the mask to test the input character against.

   Returns: true if the specified character is valid for the specified position; otherwise,false.
  """
  pass
 def VerifyEscapeChar(self,input,position):
  """
  VerifyEscapeChar(self: MaskedTextProvider,input: Char,position: int) -> bool

  

   Tests whether the specified character would be escaped at the specified position.

  

   input: The System.Char value to test.

   position: The position in the mask to test the input character against.

   Returns: true if the specified character would be escaped at the specified position; otherwise,false.
  """
  pass
 def VerifyString(self,input,testPosition=None,resultHint=None):
  """
  VerifyString(self: MaskedTextProvider,input: str) -> (bool,int,MaskedTextResultHint)

  

   Tests whether the specified string could be set successfully,and then outputs position and 

    descriptive information.

  

  

   input: The System.String value to test.

   Returns: true if the specified string represents valid input; otherwise,false.

  VerifyString(self: MaskedTextProvider,input: str) -> bool

  

   Tests whether the specified string could be set successfully.

  

   input: The System.String value to test.

   Returns: true if the specified string represents valid input; otherwise,false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,mask,*__args):
  """
  __new__(cls: type,mask: str)

  __new__(cls: type,mask: str,restrictToAscii: bool)

  __new__(cls: type,mask: str,culture: CultureInfo)

  __new__(cls: type,mask: str,culture: CultureInfo,restrictToAscii: bool)

  __new__(cls: type,mask: str,passwordChar: Char,allowPromptAsInput: bool)

  __new__(cls: type,mask: str,culture: CultureInfo,passwordChar: Char,allowPromptAsInput: bool)

  __new__(cls: type,mask: str,culture: CultureInfo,allowPromptAsInput: bool,promptChar: Char,passwordChar: Char,restrictToAscii: bool)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 AllowPromptAsInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the prompt character should be treated as a valid input character or not.



Get: AllowPromptAsInput(self: MaskedTextProvider) -> bool



"""

 AsciiOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the mask accepts characters outside of the ASCII character set.



Get: AsciiOnly(self: MaskedTextProvider) -> bool



"""

 AssignedEditPositionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of editable character positions that have already been successfully assigned an input value.



Get: AssignedEditPositionCount(self: MaskedTextProvider) -> int



"""

 AvailableEditPositionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of editable character positions in the input mask that have not yet been assigned an input value.



Get: AvailableEditPositionCount(self: MaskedTextProvider) -> int



"""

 Culture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the culture that determines the value of the localizable separators and placeholders in the input mask.



Get: Culture(self: MaskedTextProvider) -> CultureInfo



"""

 EditPositionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of editable positions in the formatted string.



Get: EditPositionCount(self: MaskedTextProvider) -> int



"""

 EditPositions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a newly created enumerator for the editable positions in the formatted string.



Get: EditPositions(self: MaskedTextProvider) -> IEnumerator



"""

 IncludeLiterals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether literal characters in the input mask should be included in the formatted string.



Get: IncludeLiterals(self: MaskedTextProvider) -> bool



Set: IncludeLiterals(self: MaskedTextProvider)=value

"""

 IncludePrompt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether System.Windows.Forms.MaskedTextBox.PromptChar is used to represent the absence of user input when displaying the formatted string.



Get: IncludePrompt(self: MaskedTextProvider) -> bool



Set: IncludePrompt(self: MaskedTextProvider)=value

"""

 IsPassword=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines whether password protection should be applied to the formatted string.



Get: IsPassword(self: MaskedTextProvider) -> bool



Set: IsPassword(self: MaskedTextProvider)=value

"""

 LastAssignedPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index in the mask of the rightmost input character that has been assigned to the mask.



Get: LastAssignedPosition(self: MaskedTextProvider) -> int



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the mask,absent any mask modifier characters.



Get: Length(self: MaskedTextProvider) -> int



"""

 Mask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the input mask.



Get: Mask(self: MaskedTextProvider) -> str



"""

 MaskCompleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether all required inputs have been entered into the formatted string.



Get: MaskCompleted(self: MaskedTextProvider) -> bool



"""

 MaskFull=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether all required and optional inputs have been entered into the formatted string.



Get: MaskFull(self: MaskedTextProvider) -> bool



"""

 PasswordChar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the character to be substituted for the actual input characters.



Get: PasswordChar(self: MaskedTextProvider) -> Char



Set: PasswordChar(self: MaskedTextProvider)=value

"""

 PromptChar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the character used to represent the absence of user input for all available edit positions.



Get: PromptChar(self: MaskedTextProvider) -> Char



Set: PromptChar(self: MaskedTextProvider)=value

"""

 ResetOnPrompt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines how an input character that matches the prompt character should be handled.



Get: ResetOnPrompt(self: MaskedTextProvider) -> bool



Set: ResetOnPrompt(self: MaskedTextProvider)=value

"""

 ResetOnSpace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines how a space input character should be handled.



Get: ResetOnSpace(self: MaskedTextProvider) -> bool



Set: ResetOnSpace(self: MaskedTextProvider)=value

"""

 SkipLiterals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether literal character positions in the mask can be overwritten by their same values.



Get: SkipLiterals(self: MaskedTextProvider) -> bool



Set: SkipLiterals(self: MaskedTextProvider)=value

"""


 DefaultPasswordChar=None
 InvalidIndex=-1

