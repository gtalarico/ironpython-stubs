class Binding(object):
 """
 Represents the simple binding between the property value of an object and the property value of a control.

 

 Binding(propertyName: str,dataSource: object,dataMember: str)

 Binding(propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool)

 Binding(propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,dataSourceUpdateMode: DataSourceUpdateMode)

 Binding(propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,dataSourceUpdateMode: DataSourceUpdateMode,nullValue: object)

 Binding(propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,dataSourceUpdateMode: DataSourceUpdateMode,nullValue: object,formatString: str)

 Binding(propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,dataSourceUpdateMode: DataSourceUpdateMode,nullValue: object,formatString: str,formatInfo: IFormatProvider)
 """
 def OnBindingComplete(self,*args):
  """
  OnBindingComplete(self: Binding,e: BindingCompleteEventArgs)

   Raises the System.Windows.Forms.Binding.BindingComplete event.

  

   e: A System.Windows.Forms.BindingCompleteEventArgs  that contains the event data.
  """
  pass
 def OnFormat(self,*args):
  """
  OnFormat(self: Binding,cevent: ConvertEventArgs)

   Raises the System.Windows.Forms.Binding.Format event.

  

   cevent: A System.Windows.Forms.ConvertEventArgs that contains the event data.
  """
  pass
 def OnParse(self,*args):
  """
  OnParse(self: Binding,cevent: ConvertEventArgs)

   Raises the System.Windows.Forms.Binding.Parse event.

  

   cevent: A System.Windows.Forms.ConvertEventArgs that contains the event data.
  """
  pass
 def ReadValue(self):
  """
  ReadValue(self: Binding)

   Sets the control property to the value read from the data source.
  """
  pass
 def WriteValue(self):
  """
  WriteValue(self: Binding)

   Reads the current value from the control property and writes it to the data source.
  """
  pass
 @staticmethod
 def __new__(self,propertyName,dataSource,dataMember,formattingEnabled=None,dataSourceUpdateMode=None,nullValue=None,formatString=None,formatInfo=None):
  """
  __new__(cls: type,propertyName: str,dataSource: object,dataMember: str)

  __new__(cls: type,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool)

  __new__(cls: type,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,dataSourceUpdateMode: DataSourceUpdateMode)

  __new__(cls: type,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,dataSourceUpdateMode: DataSourceUpdateMode,nullValue: object)

  __new__(cls: type,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,dataSourceUpdateMode: DataSourceUpdateMode,nullValue: object,formatString: str)

  __new__(cls: type,propertyName: str,dataSource: object,dataMember: str,formattingEnabled: bool,dataSourceUpdateMode: DataSourceUpdateMode,nullValue: object,formatString: str,formatInfo: IFormatProvider)
  """
  pass
 BindableComponent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control the System.Windows.Forms.Binding is associated with.



Get: BindableComponent(self: Binding) -> IBindableComponent



"""

 BindingManagerBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.BindingManagerBase for this System.Windows.Forms.Binding.



Get: BindingManagerBase(self: Binding) -> BindingManagerBase



"""

 BindingMemberInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that contains information about this binding based on the dataMember parameter in the erload:System.Windows.Forms.Binding.#ctor constructor.



Get: BindingMemberInfo(self: Binding) -> BindingMemberInfo



"""

 Control=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control that the binding belongs to.



Get: Control(self: Binding) -> Control



"""

 ControlUpdateMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets when changes to the data source are propagated to the bound control property.



Get: ControlUpdateMode(self: Binding) -> ControlUpdateMode



Set: ControlUpdateMode(self: Binding)=value

"""

 DataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data source for this binding.



Get: DataSource(self: Binding) -> object



"""

 DataSourceNullValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value to be stored in the data source if the control value is null or empty.



Get: DataSourceNullValue(self: Binding) -> object



Set: DataSourceNullValue(self: Binding)=value

"""

 DataSourceUpdateMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates when changes to the bound control property are propagated to the data source.



Get: DataSourceUpdateMode(self: Binding) -> DataSourceUpdateMode



Set: DataSourceUpdateMode(self: Binding)=value

"""

 FormatInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.IFormatProvider that provides custom formatting behavior.



Get: FormatInfo(self: Binding) -> IFormatProvider



Set: FormatInfo(self: Binding)=value

"""

 FormatString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the format specifier characters that indicate how a value is to be displayed.



Get: FormatString(self: Binding) -> str



Set: FormatString(self: Binding)=value

"""

 FormattingEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether type conversion and formatting is applied to the control property data.



Get: FormattingEnabled(self: Binding) -> bool



Set: FormattingEnabled(self: Binding)=value

"""

 IsBinding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the binding is active.



Get: IsBinding(self: Binding) -> bool



"""

 NullValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Object to be set as the control property when the data source contains a System.DBNull value.



Get: NullValue(self: Binding) -> object



Set: NullValue(self: Binding)=value

"""

 PropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the control's data-bound property.



Get: PropertyName(self: Binding) -> str



"""


 BindingComplete=None
 Format=None
 Parse=None

