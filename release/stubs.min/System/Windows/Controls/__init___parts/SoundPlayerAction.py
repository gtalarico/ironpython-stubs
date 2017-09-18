class SoundPlayerAction(TriggerAction,IDisposable):
 """
 Represents a lightweight audio playback System.Windows.TriggerAction used to play .wav files.

 

 SoundPlayerAction()
 """
 def Dispose(self):
  """
  Dispose(self: SoundPlayerAction)

   Releases the resources used by the System.Windows.Controls.SoundPlayerAction class.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: DependencyObject,e: DependencyPropertyChangedEventArgs)

   Invoked whenever the effective value of any dependency property on this 

    System.Windows.DependencyObject has been updated. The specific dependency property that changed 

    is reported in the event data.

  

  

   e: Event data that will contain the dependency property identifier of interest,the property 

    metadata for the type,and old and new values.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool

  

   Returns a value that indicates whether serialization processes should serialize the value for 

    the provided dependency property.

  

  

   dp: The identifier for the dependency property that should be serialized.

   Returns: true if the dependency property that is supplied should be value-serialized; otherwise,false.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the audio source location.



Get: Source(self: SoundPlayerAction) -> Uri



Set: Source(self: SoundPlayerAction)=value

"""


 SourceProperty=None

