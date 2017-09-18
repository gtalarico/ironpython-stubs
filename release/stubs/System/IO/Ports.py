# encoding: utf-8
# module System.IO.Ports calls itself Ports
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Handshake(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the control protocol used in establishing a serial port communication for a System.IO.Ports.SerialPort object.
    
    enum Handshake, values: None (0), RequestToSend (2), RequestToSendXOnXOff (3), XOnXOff (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    RequestToSend = None
    RequestToSendXOnXOff = None
    value__ = None
    XOnXOff = None


class Parity(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the parity bit for a System.IO.Ports.SerialPort object.
    
    enum Parity, values: Even (2), Mark (3), None (0), Odd (1), Space (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Even = None
    Mark = None
    None = None
    Odd = None
    Space = None
    value__ = None


class SerialData(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of character that was received on the serial port of the System.IO.Ports.SerialPort object.
    
    enum SerialData, values: Chars (1), Eof (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Chars = None
    Eof = None
    value__ = None


class SerialDataReceivedEventArgs(EventArgs):
    """ Provides data for the System.IO.Ports.SerialPort.DataReceived event. """
    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event type.

Get: EventType(self: SerialDataReceivedEventArgs) -> SerialData

"""



class SerialDataReceivedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.IO.Ports.SerialPort.DataReceived event of a System.IO.Ports.SerialPort object.
    
    SerialDataReceivedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SerialDataReceivedEventHandler, sender: object, e: SerialDataReceivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SerialDataReceivedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SerialDataReceivedEventHandler, sender: object, e: SerialDataReceivedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SerialError(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies errors that occur on the System.IO.Ports.SerialPort object.
    
    enum SerialError, values: Frame (8), Overrun (2), RXOver (1), RXParity (4), TXFull (256)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Frame = None
    Overrun = None
    RXOver = None
    RXParity = None
    TXFull = None
    value__ = None


class SerialErrorReceivedEventArgs(EventArgs):
    """ Prepares data for the System.IO.Ports.SerialPort.ErrorReceived event. """
    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event type.

Get: EventType(self: SerialErrorReceivedEventArgs) -> SerialError

"""



class SerialErrorReceivedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.IO.Ports.SerialPort.ErrorReceived event of a System.IO.Ports.SerialPort object.
    
    SerialErrorReceivedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SerialErrorReceivedEventHandler, sender: object, e: SerialErrorReceivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SerialErrorReceivedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SerialErrorReceivedEventHandler, sender: object, e: SerialErrorReceivedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SerialPinChange(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of change that occurred on the System.IO.Ports.SerialPort object.
    
    enum SerialPinChange, values: Break (64), CDChanged (32), CtsChanged (8), DsrChanged (16), Ring (256)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Break = None
    CDChanged = None
    CtsChanged = None
    DsrChanged = None
    Ring = None
    value__ = None


class SerialPinChangedEventArgs(EventArgs):
    """ Provides data for the System.IO.Ports.SerialPort.PinChanged event. """
    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event type.

Get: EventType(self: SerialPinChangedEventArgs) -> SerialPinChange

"""



class SerialPinChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.IO.Ports.SerialPort.PinChanged event of a System.IO.Ports.SerialPort object.
    
    SerialPinChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SerialPinChangedEventHandler, sender: object, e: SerialPinChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SerialPinChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SerialPinChangedEventHandler, sender: object, e: SerialPinChangedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SerialPort(Component, IComponent, IDisposable):
    """
    Represents a serial port resource.
    
    SerialPort(container: IContainer)
    SerialPort()
    SerialPort(portName: str)
    SerialPort(portName: str, baudRate: int)
    SerialPort(portName: str, baudRate: int, parity: Parity)
    SerialPort(portName: str, baudRate: int, parity: Parity, dataBits: int)
    SerialPort(portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits)
    """
    def Close(self):
        """
        Close(self: SerialPort)
            Closes the port connection, sets the System.IO.Ports.SerialPort.IsOpen property to false, and 
             disposes of the internal System.IO.Stream object.
        """
        pass

    def DiscardInBuffer(self):
        """
        DiscardInBuffer(self: SerialPort)
            Discards data from the serial driver's receive buffer.
        """
        pass

    def DiscardOutBuffer(self):
        """
        DiscardOutBuffer(self: SerialPort)
            Discards data from the serial driver's transmit buffer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SerialPort, disposing: bool)
            Releases the unmanaged resources used by the System.IO.Ports.SerialPort and optionally releases 
             the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    @staticmethod
    def GetPortNames():
        """
        GetPortNames() -> Array[str]
        
            Gets an array of serial port names for the current computer.
            Returns: An array of serial port names for the current computer.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Open(self):
        """
        Open(self: SerialPort)
            Opens a new serial port connection.
        """
        pass

    def Read(self, buffer, offset, count):
        """
        Read(self: SerialPort, buffer: Array[Char], offset: int, count: int) -> int
        
            Reads a number of characters from the System.IO.Ports.SerialPort input buffer and writes them 
             into an array of characters at a given offset.
        
        
            buffer: The character array to write the input to.
            offset: The offset in the buffer array to begin writing.
            count: The number of characters to read.
            Returns: The number of characters read.
        Read(self: SerialPort, buffer: Array[Byte], offset: int, count: int) -> int
        
            Reads a number of bytes from the System.IO.Ports.SerialPort input buffer and writes those bytes 
             into a byte array at the specified offset.
        
        
            buffer: The byte array to write the input to.
            offset: The offset in the buffer array to begin writing.
            count: The number of bytes to read.
            Returns: The number of bytes read.
        """
        pass

    def ReadByte(self):
        """
        ReadByte(self: SerialPort) -> int
        
            Synchronously reads one byte from the System.IO.Ports.SerialPort input buffer.
            Returns: The byte, cast to an System.Int32, or -1 if the end of the stream has been read.
        """
        pass

    def ReadChar(self):
        """
        ReadChar(self: SerialPort) -> int
        
            Synchronously reads one character from the System.IO.Ports.SerialPort input buffer.
            Returns: The character that was read.
        """
        pass

    def ReadExisting(self):
        """
        ReadExisting(self: SerialPort) -> str
        
            Reads all immediately available bytes, based on the encoding, in both the stream and the input 
             buffer of the System.IO.Ports.SerialPort object.
        
            Returns: The contents of the stream and the input buffer of the System.IO.Ports.SerialPort object.
        """
        pass

    def ReadLine(self):
        """
        ReadLine(self: SerialPort) -> str
        
            Reads up to the System.IO.Ports.SerialPort.NewLine value in the input buffer.
            Returns: The contents of the input buffer up to the first occurrence of a 
             System.IO.Ports.SerialPort.NewLine value.
        """
        pass

    def ReadTo(self, value):
        """
        ReadTo(self: SerialPort, value: str) -> str
        
            Reads a string up to the specified value in the input buffer.
        
            value: A value that indicates where the read operation stops.
            Returns: The contents of the input buffer up to the specified value.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: SerialPort, buffer: Array[Byte], offset: int, count: int)
            Writes a specified number of bytes to the serial port using data from a buffer.
        
            buffer: The byte array that contains the data to write to the port.
            offset: The zero-based byte offset in the buffer parameter at which to begin copying bytes to the port.
            count: The number of bytes to write.
        Write(self: SerialPort, buffer: Array[Char], offset: int, count: int)
            Writes a specified number of characters to the serial port using data from a buffer.
        
            buffer: The character array that contains the data to write to the port.
            offset: The zero-based byte offset in the buffer parameter at which to begin copying bytes to the port.
            count: The number of characters to write.
        Write(self: SerialPort, text: str)
            Writes the specified string to the serial port.
        
            text: The string for output.
        """
        pass

    def WriteLine(self, text):
        """
        WriteLine(self: SerialPort, text: str)
            Writes the specified string and the System.IO.Ports.SerialPort.NewLine value to the output 
             buffer.
        
        
            text: The string to write to the output buffer.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, container: IContainer)
        __new__(cls: type)
        __new__(cls: type, portName: str)
        __new__(cls: type, portName: str, baudRate: int)
        __new__(cls: type, portName: str, baudRate: int, parity: Parity)
        __new__(cls: type, portName: str, baudRate: int, parity: Parity, dataBits: int)
        __new__(cls: type, portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying System.IO.Stream object for a System.IO.Ports.SerialPort object.

Get: BaseStream(self: SerialPort) -> Stream

"""

    BaudRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the serial baud rate.

Get: BaudRate(self: SerialPort) -> int

Set: BaudRate(self: SerialPort) = value
"""

    BreakState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the break signal state.

Get: BreakState(self: SerialPort) -> bool

Set: BreakState(self: SerialPort) = value
"""

    BytesToRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bytes of data in the receive buffer.

Get: BytesToRead(self: SerialPort) -> int

"""

    BytesToWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bytes of data in the send buffer.

Get: BytesToWrite(self: SerialPort) -> int

"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    CDHolding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the Carrier Detect line for the port.

Get: CDHolding(self: SerialPort) -> bool

"""

    CtsHolding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the Clear-to-Send line.

Get: CtsHolding(self: SerialPort) -> bool

"""

    DataBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the standard length of data bits per byte.

Get: DataBits(self: SerialPort) -> int

Set: DataBits(self: SerialPort) = value
"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    DiscardNull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether null bytes are ignored when transmitted between the port and the receive buffer.

Get: DiscardNull(self: SerialPort) -> bool

Set: DiscardNull(self: SerialPort) = value
"""

    DsrHolding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the Data Set Ready (DSR) signal.

Get: DsrHolding(self: SerialPort) -> bool

"""

    DtrEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that enables the Data Terminal Ready (DTR) signal during serial communication.

Get: DtrEnable(self: SerialPort) -> bool

Set: DtrEnable(self: SerialPort) = value
"""

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the byte encoding for pre- and post-transmission conversion of text.

Get: Encoding(self: SerialPort) -> Encoding

Set: Encoding(self: SerialPort) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    Handshake = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the handshaking protocol for serial port transmission of data.

Get: Handshake(self: SerialPort) -> Handshake

Set: Handshake(self: SerialPort) = value
"""

    IsOpen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating the open or closed status of the System.IO.Ports.SerialPort object.

Get: IsOpen(self: SerialPort) -> bool

"""

    NewLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value used to interpret the end of a call to the System.IO.Ports.SerialPort.ReadLine and System.IO.Ports.SerialPort.WriteLine(System.String) methods.

Get: NewLine(self: SerialPort) -> str

Set: NewLine(self: SerialPort) = value
"""

    Parity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the parity-checking protocol.

Get: Parity(self: SerialPort) -> Parity

Set: Parity(self: SerialPort) = value
"""

    ParityReplace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the byte that replaces invalid bytes in a data stream when a parity error occurs.

Get: ParityReplace(self: SerialPort) -> Byte

Set: ParityReplace(self: SerialPort) = value
"""

    PortName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the port for communications, including but not limited to all available COM ports.

Get: PortName(self: SerialPort) -> str

Set: PortName(self: SerialPort) = value
"""

    ReadBufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size of the System.IO.Ports.SerialPort input buffer.

Get: ReadBufferSize(self: SerialPort) -> int

Set: ReadBufferSize(self: SerialPort) = value
"""

    ReadTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of milliseconds before a time-out occurs when a read operation does not finish.

Get: ReadTimeout(self: SerialPort) -> int

Set: ReadTimeout(self: SerialPort) = value
"""

    ReceivedBytesThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of bytes in the internal input buffer before a System.IO.Ports.SerialPort.DataReceived event occurs.

Get: ReceivedBytesThreshold(self: SerialPort) -> int

Set: ReceivedBytesThreshold(self: SerialPort) = value
"""

    RtsEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the Request to Send (RTS) signal is enabled during serial communication.

Get: RtsEnable(self: SerialPort) -> bool

Set: RtsEnable(self: SerialPort) = value
"""

    StopBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the standard number of stopbits per byte.

Get: StopBits(self: SerialPort) -> StopBits

Set: StopBits(self: SerialPort) = value
"""

    WriteBufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size of the serial port output buffer.

Get: WriteBufferSize(self: SerialPort) -> int

Set: WriteBufferSize(self: SerialPort) = value
"""

    WriteTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of milliseconds before a time-out occurs when a write operation does not finish.

Get: WriteTimeout(self: SerialPort) -> int

Set: WriteTimeout(self: SerialPort) = value
"""


    DataReceived = None
    ErrorReceived = None
    InfiniteTimeout = -1
    PinChanged = None


class StopBits(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the number of stop bits used on the System.IO.Ports.SerialPort object.
    
    enum StopBits, values: None (0), One (1), OnePointFive (3), Two (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    One = None
    OnePointFive = None
    Two = None
    value__ = None


