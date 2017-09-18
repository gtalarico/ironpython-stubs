class CreateParams(object):
 """
 Encapsulates the information needed when creating a control.

 

 CreateParams()
 """
 def ToString(self):
  """
  ToString(self: CreateParams) -> str

   Returns: A string that represents the current object.
  """
  pass
 Caption=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the control's initial text.



Get: Caption(self: CreateParams) -> str



Set: Caption(self: CreateParams)=value

"""

 ClassName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the Windows class to derive the control from.



Get: ClassName(self: CreateParams) -> str



Set: ClassName(self: CreateParams)=value

"""

 ClassStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a bitwise combination of class style values.



Get: ClassStyle(self: CreateParams) -> int



Set: ClassStyle(self: CreateParams)=value

"""

 ExStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a bitwise combination of extended window style values.



Get: ExStyle(self: CreateParams) -> int



Set: ExStyle(self: CreateParams)=value

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the initial height of the control.



Get: Height(self: CreateParams) -> int



Set: Height(self: CreateParams)=value

"""

 Param=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets additional parameter information needed to create the control.



Get: Param(self: CreateParams) -> object



Set: Param(self: CreateParams)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the control's parent.



Get: Parent(self: CreateParams) -> IntPtr



Set: Parent(self: CreateParams)=value

"""

 Style=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a bitwise combination of window style values.



Get: Style(self: CreateParams) -> int



Set: Style(self: CreateParams)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the initial width of the control.



Get: Width(self: CreateParams) -> int



Set: Width(self: CreateParams)=value

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the initial left position of the control.



Get: X(self: CreateParams) -> int



Set: X(self: CreateParams)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the top position of the initial location of the control.



Get: Y(self: CreateParams) -> int



Set: Y(self: CreateParams)=value

"""


