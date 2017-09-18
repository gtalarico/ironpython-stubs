# encoding: utf-8
# module System.Net.Mail calls itself Mail
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AttachmentBase(object, IDisposable):
    """ Base class that represents an email attachment. Classes System.Net.Mail.Attachment, System.Net.Mail.AlternateView, and System.Net.Mail.LinkedResource derive from this class. """
    def Dispose(self):
        """
        Dispose(self: AttachmentBase)
            Releases the resources used by the System.Net.Mail.AttachmentBase.
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, mediaType: str)
        __new__(cls: type, fileName: str, contentType: ContentType)
        __new__(cls: type, contentStream: Stream)
        __new__(cls: type, contentStream: Stream, mediaType: str)
        __new__(cls: type, contentStream: Stream, contentType: ContentType)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ContentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the MIME content ID for this attachment.

Get: ContentId(self: AttachmentBase) -> str

Set: ContentId(self: AttachmentBase) = value
"""

    ContentStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the content stream of this attachment.

Get: ContentStream(self: AttachmentBase) -> Stream

"""

    ContentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the content type of this attachment.

Get: ContentType(self: AttachmentBase) -> ContentType

Set: ContentType(self: AttachmentBase) = value
"""

    TransferEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the encoding of this attachment.

Get: TransferEncoding(self: AttachmentBase) -> TransferEncoding

Set: TransferEncoding(self: AttachmentBase) = value
"""



class AlternateView(AttachmentBase, IDisposable):
    """
    Represents the format to view an email message.
    
    AlternateView(fileName: str)
    AlternateView(fileName: str, mediaType: str)
    AlternateView(fileName: str, contentType: ContentType)
    AlternateView(contentStream: Stream)
    AlternateView(contentStream: Stream, mediaType: str)
    AlternateView(contentStream: Stream, contentType: ContentType)
    """
    @staticmethod
    def CreateAlternateViewFromString(content, *__args):
        """
        CreateAlternateViewFromString(content: str, contentType: ContentType) -> AlternateView
        
            Creates an System.Net.Mail.AlternateView of an email message using the content specified in a 
             System.String and the specified MIME media type of the content.
        
        
            content: A System.String that contains the content for this attachment.
            contentType: A System.Net.Mime.ContentType that describes the data in string.
            Returns: An System.Net.Mail.AlternateView object that represents an alternate view of an email message.
        CreateAlternateViewFromString(content: str, contentEncoding: Encoding, mediaType: str) -> AlternateView
        
            Creates an System.Net.Mail.AlternateView of an email message using the content specified in a 
             System.String, the specified text encoding, and MIME media type of the content.
        
        
            content: A System.String that contains the content for this attachment.
            contentEncoding: An System.Text.Encoding. This value can be null.
            mediaType: The MIME media type of the content.
            Returns: An System.Net.Mail.AlternateView object that represents an alternate view of an email message.
        CreateAlternateViewFromString(content: str) -> AlternateView
        
            Creates a System.Net.Mail.AlternateView of an email message using the content specified in a 
             System.String.
        
        
            content: The System.String that contains the content of the email message.
            Returns: An System.Net.Mail.AlternateView object that represents an alternate view of an email message.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: AlternateView, disposing: bool)
            Releases the unmanaged resources used by the System.Net.Mail.AlternateView and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, mediaType: str)
        __new__(cls: type, fileName: str, contentType: ContentType)
        __new__(cls: type, contentStream: Stream)
        __new__(cls: type, contentStream: Stream, mediaType: str)
        __new__(cls: type, contentStream: Stream, contentType: ContentType)
        """
        pass

    BaseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Base URI to use for resolving relative URIs in the System.Net.Mail.AlternateView.

Get: BaseUri(self: AlternateView) -> Uri

Set: BaseUri(self: AlternateView) = value
"""

    LinkedResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of embedded resources referred to by this attachment.

Get: LinkedResources(self: AlternateView) -> LinkedResourceCollection

"""



class AlternateViewCollection(Collection[AlternateView], IList[AlternateView], ICollection[AlternateView], IEnumerable[AlternateView], IEnumerable, IList, ICollection, IReadOnlyList[AlternateView], IReadOnlyCollection[AlternateView], IDisposable):
    """ Represents a collection of System.Net.Mail.AlternateView objects. """
    def ClearItems(self, *args): #cannot find CLR method
        """ ClearItems(self: AlternateViewCollection) """
        pass

    def Dispose(self):
        """
        Dispose(self: AlternateViewCollection)
            Releases all resources used by the System.Net.Mail.AlternateViewCollection.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: AlternateViewCollection, index: int, item: AlternateView) """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: AlternateViewCollection, index: int) """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: AlternateViewCollection, index: int, item: AlternateView) """
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

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""



class Attachment(AttachmentBase, IDisposable):
    """
    Represents an attachment to an e-mail.
    
    Attachment(fileName: str)
    Attachment(fileName: str, mediaType: str)
    Attachment(fileName: str, contentType: ContentType)
    Attachment(contentStream: Stream, name: str)
    Attachment(contentStream: Stream, name: str, mediaType: str)
    Attachment(contentStream: Stream, contentType: ContentType)
    """
    @staticmethod
    def CreateAttachmentFromString(content, *__args):
        """
        CreateAttachmentFromString(content: str, contentType: ContentType) -> Attachment
        
            Creates a mail attachment using the content from the specified string, and the specified 
             System.Net.Mime.ContentType.
        
        
            content: A System.String that contains the content for this attachment.
            contentType: A System.Net.Mime.ContentType object that represents the Multipurpose Internet Mail Exchange 
             (MIME) protocol Content-Type header to be used.
        
            Returns: An object of type System.Net.Mail.Attachment.
        CreateAttachmentFromString(content: str, name: str, contentEncoding: Encoding, mediaType: str) -> Attachment
        
            Creates a mail attachment using the content from the specified string, the specified MIME 
             content type name, character encoding, and MIME header information for the attachment.
        
        
            content: A System.String that contains the content for this attachment.
            name: The MIME content type name value in the content type associated with this attachment.
            contentEncoding: An System.Text.Encoding. This value can be null.
            mediaType: A System.String that contains the MIME Content-Header information for this attachment. This 
             value can be null.
        
            Returns: An object of type System.Net.Mail.Attachment.
        CreateAttachmentFromString(content: str, name: str) -> Attachment
        
            Creates a mail attachment using the content from the specified string, and the specified MIME 
             content type name.
        
        
            content: A System.String that contains the content for this attachment.
            name: The MIME content type name value in the content type associated with this attachment.
            Returns: An object of type System.Net.Mail.Attachment.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: AttachmentBase, disposing: bool)
            Releases the unmanaged resources used by the System.Net.Mail.AttachmentBase and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, mediaType: str)
        __new__(cls: type, fileName: str, contentType: ContentType)
        __new__(cls: type, contentStream: Stream, name: str)
        __new__(cls: type, contentStream: Stream, name: str, mediaType: str)
        __new__(cls: type, contentStream: Stream, contentType: ContentType)
        """
        pass

    ContentDisposition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the MIME content disposition for this attachment.

Get: ContentDisposition(self: Attachment) -> ContentDisposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the MIME content type name value in the content type associated with this attachment.

Get: Name(self: Attachment) -> str

Set: Name(self: Attachment) = value
"""

    NameEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the encoding for the System.Net.Mail.AttachmentSystem.Net.Mail.Attachment.Name.

Get: NameEncoding(self: Attachment) -> Encoding

Set: NameEncoding(self: Attachment) = value
"""



class AttachmentCollection(Collection[Attachment], IList[Attachment], ICollection[Attachment], IEnumerable[Attachment], IEnumerable, IList, ICollection, IReadOnlyList[Attachment], IReadOnlyCollection[Attachment], IDisposable):
    """ Stores attachments to be sent as part of an e-mail message. """
    def ClearItems(self, *args): #cannot find CLR method
        """ ClearItems(self: AttachmentCollection) """
        pass

    def Dispose(self):
        """
        Dispose(self: AttachmentCollection)
            Releases all resources used by the System.Net.Mail.AttachmentCollection.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: AttachmentCollection, index: int, item: Attachment) """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: AttachmentCollection, index: int) """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: AttachmentCollection, index: int, item: Attachment) """
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

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""



class DeliveryNotificationOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the delivery notification options for e-mail.
    
    enum (flags) DeliveryNotificationOptions, values: Delay (4), Never (134217728), None (0), OnFailure (2), OnSuccess (1)
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

    Delay = None
    Never = None
    None = None
    OnFailure = None
    OnSuccess = None
    value__ = None


class LinkedResource(AttachmentBase, IDisposable):
    """
    Represents an embedded external resource in an email attachment, such as an image in an HTML attachment.
    
    LinkedResource(fileName: str)
    LinkedResource(fileName: str, mediaType: str)
    LinkedResource(fileName: str, contentType: ContentType)
    LinkedResource(contentStream: Stream)
    LinkedResource(contentStream: Stream, mediaType: str)
    LinkedResource(contentStream: Stream, contentType: ContentType)
    """
    @staticmethod
    def CreateLinkedResourceFromString(content, *__args):
        """
        CreateLinkedResourceFromString(content: str, contentType: ContentType) -> LinkedResource
        
            Creates a System.Net.Mail.LinkedResource object from a string to be included in an email 
             attachment as an embedded resource, with the specified content type, and media type as plain 
             text.
        
        
            content: A string that contains the embedded resource to be included in the email attachment.
            contentType: The type of the content.
            Returns: A System.Net.Mail.LinkedResource object that contains the embedded resource to be included in 
             the email attachment.
        
        CreateLinkedResourceFromString(content: str, contentEncoding: Encoding, mediaType: str) -> LinkedResource
        
            Creates a System.Net.Mail.LinkedResource object from a string to be included in an email 
             attachment as an embedded resource, with the specified content type, and media type.
        
        
            content: A string that contains the embedded resource to be included in the email attachment.
            contentEncoding: The type of the content.
            mediaType: The MIME media type of the content.
            Returns: A System.Net.Mail.LinkedResource object that contains the embedded resource to be included in 
             the email attachment.
        
        CreateLinkedResourceFromString(content: str) -> LinkedResource
        
            Creates a System.Net.Mail.LinkedResource object from a string to be included in an email 
             attachment as an embedded resource. The default media type is plain text, and the default 
             content type is ASCII.
        
        
            content: A string that contains the embedded resource to be included in the email attachment.
            Returns: A System.Net.Mail.LinkedResource object that contains the embedded resource to be included in 
             the email attachment.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: AttachmentBase, disposing: bool)
            Releases the unmanaged resources used by the System.Net.Mail.AttachmentBase and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, mediaType: str)
        __new__(cls: type, fileName: str, contentType: ContentType)
        __new__(cls: type, contentStream: Stream)
        __new__(cls: type, contentStream: Stream, mediaType: str)
        __new__(cls: type, contentStream: Stream, contentType: ContentType)
        """
        pass

    ContentLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a URI that the resource must match.

Get: ContentLink(self: LinkedResource) -> Uri

Set: ContentLink(self: LinkedResource) = value
"""



class LinkedResourceCollection(Collection[LinkedResource], IList[LinkedResource], ICollection[LinkedResource], IEnumerable[LinkedResource], IEnumerable, IList, ICollection, IReadOnlyList[LinkedResource], IReadOnlyCollection[LinkedResource], IDisposable):
    """ Stores linked resources to be sent as part of an e-mail message. """
    def ClearItems(self, *args): #cannot find CLR method
        """ ClearItems(self: LinkedResourceCollection) """
        pass

    def Dispose(self):
        """
        Dispose(self: LinkedResourceCollection)
            Releases all resources used by the System.Net.Mail.LinkedResourceCollection.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: LinkedResourceCollection, index: int, item: LinkedResource) """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: LinkedResourceCollection, index: int) """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: LinkedResourceCollection, index: int, item: LinkedResource) """
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

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""



class MailAddress(object):
    """
    Represents the address of an electronic mail sender or recipient.
    
    MailAddress(address: str)
    MailAddress(address: str, displayName: str)
    MailAddress(address: str, displayName: str, displayNameEncoding: Encoding)
    """
    def Equals(self, value):
        """
        Equals(self: MailAddress, value: object) -> bool
        
            Compares two mail addresses.
        
            value: A System.Net.Mail.MailAddress instance to compare to the current instance.
            Returns: true if the two mail addresses are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: MailAddress) -> int
        
            Returns a hash value for a mail address.
            Returns: An integer hash value.
        """
        pass

    def ToString(self):
        """
        ToString(self: MailAddress) -> str
        
            Returns a string representation of this instance.
            Returns: A System.String that contains the contents of this System.Net.Mail.MailAddress.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, address, displayName=None, displayNameEncoding=None):
        """
        __new__(cls: type, address: str)
        __new__(cls: type, address: str, displayName: str)
        __new__(cls: type, address: str, displayName: str, displayNameEncoding: Encoding)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the e-mail address specified when this instance was created.

Get: Address(self: MailAddress) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display name composed from the display name and address information specified when this instance was created.

Get: DisplayName(self: MailAddress) -> str

"""

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the host portion of the address specified when this instance was created.

Get: Host(self: MailAddress) -> str

"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user information from the address specified when this instance was created.

Get: User(self: MailAddress) -> str

"""



class MailAddressCollection(Collection[MailAddress], IList[MailAddress], ICollection[MailAddress], IEnumerable[MailAddress], IEnumerable, IList, ICollection, IReadOnlyList[MailAddress], IReadOnlyCollection[MailAddress]):
    """
    Store e-mail addresses that are associated with an e-mail message.
    
    MailAddressCollection()
    """
    def Add(self, *__args):
        """
        Add(self: MailAddressCollection, addresses: str)
            Add a list of e-mail addresses to the collection.
        
            addresses: The e-mail addresses to add to the System.Net.Mail.MailAddressCollection. Multiple e-mail 
             addresses must be separated with a comma character (",").
        """
        pass

    def ClearItems(self, *args): #cannot find CLR method
        """
        ClearItems(self: Collection[MailAddress])
            Removes all elements from the System.Collections.ObjectModel.Collection.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """
        InsertItem(self: MailAddressCollection, index: int, item: MailAddress)
            Inserts an e-mail address into the System.Net.Mail.MailAddressCollection, at the specified 
             location.
        
        
            index: The location at which to insert the e-mail address that is specified by item.
            item: The e-mail address to be inserted into the collection.
        """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """
        RemoveItem(self: Collection[MailAddress], index: int)
            Removes the element at the specified index of the System.Collections.ObjectModel.Collection.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """
        SetItem(self: MailAddressCollection, index: int, item: MailAddress)
            Replaces the element at the specified index.
        
            index: The index of the e-mail address element to be replaced.
            item: An e-mail address that will replace the element in the collection.
        """
        pass

    def ToString(self):
        """
        ToString(self: MailAddressCollection) -> str
        
            Returns a string representation of the e-mail addresses in this 
             System.Net.Mail.MailAddressCollection object.
        
            Returns: A System.String containing the e-mail addresses in this collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""



class MailMessage(object, IDisposable):
    """
    Represents an e-mail message that can be sent using the System.Net.Mail.SmtpClient class.
    
    MailMessage()
    MailMessage(from: str, to: str)
    MailMessage(from: str, to: str, subject: str, body: str)
    MailMessage(from: MailAddress, to: MailAddress)
    """
    def Dispose(self):
        """
        Dispose(self: MailMessage)
            Releases all resources used by the System.Net.Mail.MailMessage.
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
    def __new__(self, from=None, to=None, subject=None, body=None):
        """
        __new__(cls: type)
        __new__(cls: type, from: str, to: str)
        __new__(cls: type, from: str, to: str, subject: str, body: str)
        __new__(cls: type, from: MailAddress, to: MailAddress)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AlternateViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the attachment collection used to store alternate forms of the message body.

Get: AlternateViews(self: MailMessage) -> AlternateViewCollection

"""

    Attachments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the attachment collection used to store data attached to this e-mail message.

Get: Attachments(self: MailMessage) -> AttachmentCollection

"""

    Bcc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the address collection that contains the blind carbon copy (BCC) recipients for this e-mail message.

Get: Bcc(self: MailMessage) -> MailAddressCollection

"""

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the message body.

Get: Body(self: MailMessage) -> str

Set: Body(self: MailMessage) = value
"""

    BodyEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the encoding used to encode the message body.

Get: BodyEncoding(self: MailMessage) -> Encoding

Set: BodyEncoding(self: MailMessage) = value
"""

    BodyTransferEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BodyTransferEncoding(self: MailMessage) -> TransferEncoding

Set: BodyTransferEncoding(self: MailMessage) = value
"""

    CC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the address collection that contains the carbon copy (CC) recipients for this e-mail message.

Get: CC(self: MailMessage) -> MailAddressCollection

"""

    DeliveryNotificationOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the delivery notifications for this e-mail message.

Get: DeliveryNotificationOptions(self: MailMessage) -> DeliveryNotificationOptions

Set: DeliveryNotificationOptions(self: MailMessage) = value
"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the from address for this e-mail message.

Get: From(self: MailMessage) -> MailAddress

Set: From(self: MailMessage) = value
"""

    Headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the e-mail headers that are transmitted with this e-mail message.

Get: Headers(self: MailMessage) -> NameValueCollection

"""

    HeadersEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the encoding used for the user-defined custom headers for this e-mail message.

Get: HeadersEncoding(self: MailMessage) -> Encoding

Set: HeadersEncoding(self: MailMessage) = value
"""

    IsBodyHtml = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the mail message body is in Html.

Get: IsBodyHtml(self: MailMessage) -> bool

Set: IsBodyHtml(self: MailMessage) = value
"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the priority of this e-mail message.

Get: Priority(self: MailMessage) -> MailPriority

Set: Priority(self: MailMessage) = value
"""

    ReplyTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ReplyTo address for the mail message.

Get: ReplyTo(self: MailMessage) -> MailAddress

Set: ReplyTo(self: MailMessage) = value
"""

    ReplyToList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the list of addresses to reply to for the mail message.

Get: ReplyToList(self: MailMessage) -> MailAddressCollection

"""

    Sender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sender's address for this e-mail message.

Get: Sender(self: MailMessage) -> MailAddress

Set: Sender(self: MailMessage) = value
"""

    Subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the subject line for this e-mail message.

Get: Subject(self: MailMessage) -> str

Set: Subject(self: MailMessage) = value
"""

    SubjectEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the encoding used for the subject content for this e-mail message.

Get: SubjectEncoding(self: MailMessage) -> Encoding

Set: SubjectEncoding(self: MailMessage) = value
"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the address collection that contains the recipients of this e-mail message.

Get: To(self: MailMessage) -> MailAddressCollection

"""



class MailPriority(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the priority of a System.Net.Mail.MailMessage.
    
    enum MailPriority, values: High (2), Low (1), Normal (0)
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

    High = None
    Low = None
    Normal = None
    value__ = None


class SendCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Net.Mail.SmtpClient.SendCompleted event.
    
    SendCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SendCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: SendCompletedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SendCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs) """
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


class SmtpAccess(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the level of access allowed to a Simple Mail Transport Protocol (SMTP) server.
    
    enum SmtpAccess, values: Connect (1), ConnectToUnrestrictedPort (2), None (0)
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

    Connect = None
    ConnectToUnrestrictedPort = None
    None = None
    value__ = None


class SmtpClient(object, IDisposable):
    """
    Allows applications to send e-mail by using the Simple Mail Transfer Protocol (SMTP).
    
    SmtpClient()
    SmtpClient(host: str)
    SmtpClient(host: str, port: int)
    """
    def Dispose(self):
        """
        Dispose(self: SmtpClient)
            Sends a QUIT message to the SMTP server, gracefully ends the TCP connection, and releases all 
             resources used by the current instance of the System.Net.Mail.SmtpClient class.
        """
        pass

    def OnSendCompleted(self, *args): #cannot find CLR method
        """
        OnSendCompleted(self: SmtpClient, e: AsyncCompletedEventArgs)
            Raises the System.Net.Mail.SmtpClient.SendCompleted event.
        
            e: An System.ComponentModel.AsyncCompletedEventArgs that contains event data.
        """
        pass

    def Send(self, *__args):
        """
        Send(self: SmtpClient, message: MailMessage)
            Sends the specified message to an SMTP server for delivery.
        
            message: A System.Net.Mail.MailMessage that contains the message to send.
        Send(self: SmtpClient, from: str, recipients: str, subject: str, body: str)
            Sends the specified e-mail message to an SMTP server for delivery. The message sender, 
             recipients, subject, and message body are specified using System.String objects.
        
        
            from: A System.String that contains the address information of the message sender.
            recipients: A System.String that contains the addresses that the message is sent to.
            subject: A System.String that contains the subject line for the message.
            body: A System.String that contains the message body.
        """
        pass

    def SendAsync(self, *__args):
        """
        SendAsync(self: SmtpClient, message: MailMessage, userToken: object)
            Sends the specified e-mail message to an SMTP server for delivery. This method does not block 
             the calling thread and allows the caller to pass an object to the method that is invoked when 
             the operation completes.
        
        
            message: A System.Net.Mail.MailMessage that contains the message to send.
            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 
             completes.
        
        SendAsync(self: SmtpClient, from: str, recipients: str, subject: str, body: str, userToken: object)
            Sends an e-mail message to an SMTP server for delivery. The message sender, recipients, subject, 
             and message body are specified using System.String objects. This method does not block the 
             calling thread and allows the caller to pass an object to the method that is invoked when the 
             operation completes.
        
        
            from: A System.String that contains the address information of the message sender.
            recipients: A System.String that contains the address that the message is sent to.
            subject: A System.String that contains the subject line for the message.
            body: A System.String that contains the message body.
            userToken: A user-defined object that is passed to the method invoked when the asynchronous operation 
             completes.
        """
        pass

    def SendAsyncCancel(self):
        """
        SendAsyncCancel(self: SmtpClient)
            Cancels an asynchronous operation to send an e-mail message.
        """
        pass

    def SendMailAsync(self, *__args):
        """
        SendMailAsync(self: SmtpClient, message: MailMessage) -> Task
        SendMailAsync(self: SmtpClient, from: str, recipients: str, subject: str, body: str) -> Task
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
    def __new__(self, host=None, port=None):
        """
        __new__(cls: type)
        __new__(cls: type, host: str)
        __new__(cls: type, host: str, port: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ClientCertificates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specify which certificates should be used to establish the Secure Sockets Layer (SSL) connection.

Get: ClientCertificates(self: SmtpClient) -> X509CertificateCollection

"""

    Credentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the credentials used to authenticate the sender.

Get: Credentials(self: SmtpClient) -> ICredentialsByHost

Set: Credentials(self: SmtpClient) = value
"""

    DeliveryFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryFormat(self: SmtpClient) -> SmtpDeliveryFormat

Set: DeliveryFormat(self: SmtpClient) = value
"""

    DeliveryMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies how outgoing email messages will be handled.

Get: DeliveryMethod(self: SmtpClient) -> SmtpDeliveryMethod

Set: DeliveryMethod(self: SmtpClient) = value
"""

    EnableSsl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specify whether the System.Net.Mail.SmtpClient uses Secure Sockets Layer (SSL) to encrypt the connection.

Get: EnableSsl(self: SmtpClient) -> bool

Set: EnableSsl(self: SmtpClient) = value
"""

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name or IP address of the host used for SMTP transactions.

Get: Host(self: SmtpClient) -> str

Set: Host(self: SmtpClient) = value
"""

    PickupDirectoryLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the folder where applications save mail messages to be processed by the local SMTP server.

Get: PickupDirectoryLocation(self: SmtpClient) -> str

Set: PickupDirectoryLocation(self: SmtpClient) = value
"""

    Port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the port used for SMTP transactions.

Get: Port(self: SmtpClient) -> int

Set: Port(self: SmtpClient) = value
"""

    ServicePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the network connection used to transmit the e-mail message.

Get: ServicePoint(self: SmtpClient) -> ServicePoint

"""

    TargetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Service Provider Name (SPN) to use for authentication when using extended protection.

Get: TargetName(self: SmtpClient) -> str

Set: TargetName(self: SmtpClient) = value
"""

    Timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the amount of time after which a synchronous erload:System.Net.Mail.SmtpClient.Send call times out.

Get: Timeout(self: SmtpClient) -> int

Set: Timeout(self: SmtpClient) = value
"""

    UseDefaultCredentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that controls whether the System.Net.CredentialCache.DefaultCredentials are sent with requests.

Get: UseDefaultCredentials(self: SmtpClient) -> bool

Set: UseDefaultCredentials(self: SmtpClient) = value
"""


    SendCompleted = None


class SmtpDeliveryFormat(Enum, IComparable, IFormattable, IConvertible):
    """ enum SmtpDeliveryFormat, values: International (1), SevenBit (0) """
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

    International = None
    SevenBit = None
    value__ = None


class SmtpDeliveryMethod(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how email messages are delivered.
    
    enum SmtpDeliveryMethod, values: Network (0), PickupDirectoryFromIis (2), SpecifiedPickupDirectory (1)
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

    Network = None
    PickupDirectoryFromIis = None
    SpecifiedPickupDirectory = None
    value__ = None


class SmtpException(Exception, ISerializable, _Exception):
    """
    Represents the exception that is thrown when the System.Net.Mail.SmtpClient is not able to complete a erload:System.Net.Mail.SmtpClient.Send or erload:System.Net.Mail.SmtpClient.SendAsync operation.
    
    SmtpException(statusCode: SmtpStatusCode)
    SmtpException(statusCode: SmtpStatusCode, message: str)
    SmtpException()
    SmtpException(message: str)
    SmtpException(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, serializationInfo, streamingContext):
        """
        GetObjectData(self: SmtpException, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
            Populates a System.Runtime.Serialization.SerializationInfo instance with the data needed to 
             serialize the System.Net.Mail.SmtpException.
        
        
            serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.
            streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 
             serialization.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, statusCode: SmtpStatusCode)
        __new__(cls: type, statusCode: SmtpStatusCode, message: str)
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    StatusCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the status code returned by an SMTP server when an e-mail message is transmitted.

Get: StatusCode(self: SmtpException) -> SmtpStatusCode

Set: StatusCode(self: SmtpException) = value
"""



class SmtpFailedRecipientException(SmtpException, ISerializable, _Exception):
    """
    Represents the exception that is thrown when the System.Net.Mail.SmtpClient is not able to complete a erload:System.Net.Mail.SmtpClient.Send or erload:System.Net.Mail.SmtpClient.SendAsync operation to a particular recipient.
    
    SmtpFailedRecipientException()
    SmtpFailedRecipientException(message: str)
    SmtpFailedRecipientException(message: str, innerException: Exception)
    SmtpFailedRecipientException(statusCode: SmtpStatusCode, failedRecipient: str)
    SmtpFailedRecipientException(statusCode: SmtpStatusCode, failedRecipient: str, serverResponse: str)
    SmtpFailedRecipientException(message: str, failedRecipient: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, serializationInfo, streamingContext):
        """
        GetObjectData(self: SmtpFailedRecipientException, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
            Populates a System.Runtime.Serialization.SerializationInfo instance with the data that is needed 
             to serialize the System.Net.Mail.SmtpFailedRecipientException.
        
        
            serializationInfo: The System.Runtime.Serialization.SerializationInfo to populate with data.
            streamingContext: A System.Runtime.Serialization.StreamingContext that specifies the destination for this 
             serialization.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, statusCode: SmtpStatusCode, failedRecipient: str)
        __new__(cls: type, statusCode: SmtpStatusCode, failedRecipient: str, serverResponse: str)
        __new__(cls: type, message: str, failedRecipient: str, innerException: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FailedRecipient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the e-mail address with delivery difficulties.

Get: FailedRecipient(self: SmtpFailedRecipientException) -> str

"""



class SmtpFailedRecipientsException(SmtpFailedRecipientException, ISerializable, _Exception):
    """
    The exception that is thrown when e-mail is sent using an System.Net.Mail.SmtpClient and cannot be delivered to all recipients.
    
    SmtpFailedRecipientsException()
    SmtpFailedRecipientsException(message: str)
    SmtpFailedRecipientsException(message: str, innerException: Exception)
    SmtpFailedRecipientsException(message: str, innerExceptions: Array[SmtpFailedRecipientException])
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, serializationInfo, streamingContext):
        """
        GetObjectData(self: SmtpFailedRecipientsException, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
            Populates a System.Runtime.Serialization.SerializationInfo instance with the data that is needed 
             to serialize the System.Net.Mail.SmtpFailedRecipientsException.
        
        
            serializationInfo: The System.Runtime.Serialization.SerializationInfo to be used.
            streamingContext: The System.Runtime.Serialization.StreamingContext to be used.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, message: str, innerExceptions: Array[SmtpFailedRecipientException])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InnerExceptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets one or more System.Net.Mail.SmtpFailedRecipientExceptions that indicate the e-mail recipients with SMTP delivery errors.

Get: InnerExceptions(self: SmtpFailedRecipientsException) -> Array[SmtpFailedRecipientException]

"""



class SmtpPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """
    Controls access to Simple Mail Transport Protocol (SMTP) servers.
    
    SmtpPermission(state: PermissionState)
    SmtpPermission(unrestricted: bool)
    SmtpPermission(access: SmtpAccess)
    """
    def AddPermission(self, access):
        """
        AddPermission(self: SmtpPermission, access: SmtpAccess)
            Adds the specified access level value to the permission.
        
            access: One of the System.Net.Mail.SmtpAccess values.
        """
        pass

    def Copy(self):
        """
        Copy(self: SmtpPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission.
            Returns: An System.Net.Mail.SmtpPermission that is identical to the current permission.
        """
        pass

    def FromXml(self, securityElement):
        """
        FromXml(self: SmtpPermission, securityElement: SecurityElement)
            Sets the state of the permission using the specified XML encoding.
        
            securityElement: The XML encoding to use to set the state of the current permission.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: SmtpPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: An System.Security.IPermission to intersect with the current permission. It must be of the same 
             type as the current permission.
        
            Returns: An System.Net.Mail.SmtpPermission that represents the intersection of the current permission and 
             the specified permission. Returns null if the intersection is empty or target is null.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: SmtpPermission, target: IPermission) -> bool
        
            Returns a value indicating whether the current permission is a subset of the specified 
             permission.
        
        
            target: An System.Security.IPermission that is to be tested for the subset relationship. This permission 
             must be of the same type as the current permission.
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: SmtpPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: SmtpPermission) -> SecurityElement
        
            Creates an XML encoding of the state of the permission.
            Returns: A System.Security.SecurityElement that contains an XML encoding of the current permission.
        """
        pass

    def Union(self, target):
        """
        Union(self: SmtpPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of the current permission and the specified permission.
        
            target: An System.Security.IPermission to combine with the current permission.
            Returns: A new System.Net.Mail.SmtpPermission permission that represents the union of the current 
             permission and the specified permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, unrestricted: bool)
        __new__(cls: type, access: SmtpAccess)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the level of access to SMTP servers controlled by the permission.

Get: Access(self: SmtpPermission) -> SmtpAccess

"""



class SmtpPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Controls access to Simple Mail Transport Protocol (SMTP) servers.
    
    SmtpPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: SmtpPermissionAttribute) -> IPermission
        
            Creates a permission object that can be stored with the 
             System.Security.Permissions.SecurityAction in an assembly's metadata.
        
            Returns: An System.Net.Mail.SmtpPermission instance.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, action):
        """ __new__(cls: type, action: SecurityAction) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the level of access to SMTP servers controlled by the attribute.

Get: Access(self: SmtpPermissionAttribute) -> str

Set: Access(self: SmtpPermissionAttribute) = value
"""



class SmtpStatusCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the outcome of sending e-mail by using the System.Net.Mail.SmtpClient class.
    
    enum SmtpStatusCode, values: BadCommandSequence (503), CannotVerifyUserWillAttemptDelivery (252), ClientNotPermitted (454), CommandNotImplemented (502), CommandParameterNotImplemented (504), CommandUnrecognized (500), ExceededStorageAllocation (552), GeneralFailure (-1), HelpMessage (214), InsufficientStorage (452), LocalErrorInProcessing (451), MailboxBusy (450), MailboxNameNotAllowed (553), MailboxUnavailable (550), MustIssueStartTlsFirst (530), Ok (250), ServiceClosingTransmissionChannel (221), ServiceNotAvailable (421), ServiceReady (220), StartMailInput (354), SyntaxError (501), SystemStatus (211), TransactionFailed (554), UserNotLocalTryAlternatePath (551), UserNotLocalWillForward (251)
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

    BadCommandSequence = None
    CannotVerifyUserWillAttemptDelivery = None
    ClientNotPermitted = None
    CommandNotImplemented = None
    CommandParameterNotImplemented = None
    CommandUnrecognized = None
    ExceededStorageAllocation = None
    GeneralFailure = None
    HelpMessage = None
    InsufficientStorage = None
    LocalErrorInProcessing = None
    MailboxBusy = None
    MailboxNameNotAllowed = None
    MailboxUnavailable = None
    MustIssueStartTlsFirst = None
    Ok = None
    ServiceClosingTransmissionChannel = None
    ServiceNotAvailable = None
    ServiceReady = None
    StartMailInput = None
    SyntaxError = None
    SystemStatus = None
    TransactionFailed = None
    UserNotLocalTryAlternatePath = None
    UserNotLocalWillForward = None
    value__ = None


