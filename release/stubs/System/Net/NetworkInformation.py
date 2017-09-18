# encoding: utf-8
# module System.Net.NetworkInformation calls itself NetworkInformation
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class DuplicateAddressDetectionState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the current state of an IP address.
    
    enum DuplicateAddressDetectionState, values: Deprecated (3), Duplicate (2), Invalid (0), Preferred (4), Tentative (1)
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

    Deprecated = None
    Duplicate = None
    Invalid = None
    Preferred = None
    Tentative = None
    value__ = None


class GatewayIPAddressInformation(object):
    """ Represents the IP address of the network gateway. This class cannot be instantiated. """
    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the IP address of the gateway.

Get: Address(self: GatewayIPAddressInformation) -> IPAddress

"""



class GatewayIPAddressInformationCollection(object, ICollection[GatewayIPAddressInformation], IEnumerable[GatewayIPAddressInformation], IEnumerable):
    """ Stores a set of System.Net.NetworkInformation.GatewayIPAddressInformation types. """
    def Add(self, address):
        """
        Add(self: GatewayIPAddressInformationCollection, address: GatewayIPAddressInformation)
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        
        
            address: The object to be added to the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: GatewayIPAddressInformationCollection)
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        """
        pass

    def Contains(self, address):
        """
        Contains(self: GatewayIPAddressInformationCollection, address: GatewayIPAddressInformation) -> bool
        
            Checks whether the collection contains the specified 
             System.Net.NetworkInformation.GatewayIPAddressInformation object.
        
        
            address: The System.Net.NetworkInformation.GatewayIPAddressInformation object to be searched in the 
             collection.
        
            Returns: true if the System.Net.NetworkInformation.GatewayIPAddressInformation object exists in the 
             collection; otherwise false.
        """
        pass

    def CopyTo(self, array, offset):
        """
        CopyTo(self: GatewayIPAddressInformationCollection, array: Array[GatewayIPAddressInformation], offset: int)
            Copies the elements in this collection to a one-dimensional array of type 
             System.Net.NetworkInformation.GatewayIPAddressInformation.
        
        
            array: A one-dimensional array that receives a copy of the collection.
            offset: The zero-based index in array at which the copy begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: GatewayIPAddressInformationCollection) -> IEnumerator[GatewayIPAddressInformation]
        
            Returns an object that can be used to iterate through this collection.
            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to 
             the System.Net.NetworkInformation.UnicastIPAddressInformation types in this collection.
        """
        pass

    def Remove(self, address):
        """
        Remove(self: GatewayIPAddressInformationCollection, address: GatewayIPAddressInformation) -> bool
        
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        
        
            address: The object to be removed.
            Returns: Always throws a System.NotSupportedException.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[GatewayIPAddressInformation], item: GatewayIPAddressInformation) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Net.NetworkInformation.GatewayIPAddressInformation types in this collection.

Get: Count(self: GatewayIPAddressInformationCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to this collection is read-only.

Get: IsReadOnly(self: GatewayIPAddressInformationCollection) -> bool

"""



class IcmpV4Statistics(object):
    """ Provides Internet Control Message Protocol for IPv4 (ICMPv4) statistical data for the local computer. """
    AddressMaskRepliesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Address Mask Reply messages that were received.

Get: AddressMaskRepliesReceived(self: IcmpV4Statistics) -> Int64

"""

    AddressMaskRepliesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Address Mask Reply messages that were sent.

Get: AddressMaskRepliesSent(self: IcmpV4Statistics) -> Int64

"""

    AddressMaskRequestsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Address Mask Request messages that were received.

Get: AddressMaskRequestsReceived(self: IcmpV4Statistics) -> Int64

"""

    AddressMaskRequestsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Address Mask Request messages that were sent.

Get: AddressMaskRequestsSent(self: IcmpV4Statistics) -> Int64

"""

    DestinationUnreachableMessagesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) messages that were received because of a packet having an unreachable address in its destination.

Get: DestinationUnreachableMessagesReceived(self: IcmpV4Statistics) -> Int64

"""

    DestinationUnreachableMessagesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) messages that were sent because of a packet having an unreachable address in its destination.

Get: DestinationUnreachableMessagesSent(self: IcmpV4Statistics) -> Int64

"""

    EchoRepliesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Echo Reply messages that were received.

Get: EchoRepliesReceived(self: IcmpV4Statistics) -> Int64

"""

    EchoRepliesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Echo Reply messages that were sent.

Get: EchoRepliesSent(self: IcmpV4Statistics) -> Int64

"""

    EchoRequestsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Echo Request messages that were received.

Get: EchoRequestsReceived(self: IcmpV4Statistics) -> Int64

"""

    EchoRequestsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Echo Request messages that were sent.

Get: EchoRequestsSent(self: IcmpV4Statistics) -> Int64

"""

    ErrorsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) error messages that were received.

Get: ErrorsReceived(self: IcmpV4Statistics) -> Int64

"""

    ErrorsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) error messages that were sent.

Get: ErrorsSent(self: IcmpV4Statistics) -> Int64

"""

    MessagesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol messages that were received.

Get: MessagesReceived(self: IcmpV4Statistics) -> Int64

"""

    MessagesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) messages that were sent.

Get: MessagesSent(self: IcmpV4Statistics) -> Int64

"""

    ParameterProblemsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Parameter Problem messages that were received.

Get: ParameterProblemsReceived(self: IcmpV4Statistics) -> Int64

"""

    ParameterProblemsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Parameter Problem messages that were sent.

Get: ParameterProblemsSent(self: IcmpV4Statistics) -> Int64

"""

    RedirectsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Redirect messages that were received.

Get: RedirectsReceived(self: IcmpV4Statistics) -> Int64

"""

    RedirectsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Redirect messages that were sent.

Get: RedirectsSent(self: IcmpV4Statistics) -> Int64

"""

    SourceQuenchesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Source Quench messages that were received.

Get: SourceQuenchesReceived(self: IcmpV4Statistics) -> Int64

"""

    SourceQuenchesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Source Quench messages that were sent.

Get: SourceQuenchesSent(self: IcmpV4Statistics) -> Int64

"""

    TimeExceededMessagesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Time Exceeded messages that were received.

Get: TimeExceededMessagesReceived(self: IcmpV4Statistics) -> Int64

"""

    TimeExceededMessagesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Time Exceeded messages that were sent.

Get: TimeExceededMessagesSent(self: IcmpV4Statistics) -> Int64

"""

    TimestampRepliesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Timestamp Reply messages that were received.

Get: TimestampRepliesReceived(self: IcmpV4Statistics) -> Int64

"""

    TimestampRepliesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Timestamp Reply messages that were sent.

Get: TimestampRepliesSent(self: IcmpV4Statistics) -> Int64

"""

    TimestampRequestsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Timestamp Request messages that were received.

Get: TimestampRequestsReceived(self: IcmpV4Statistics) -> Int64

"""

    TimestampRequestsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 4 (ICMPv4) Timestamp Request messages that were sent.

Get: TimestampRequestsSent(self: IcmpV4Statistics) -> Int64

"""



class IcmpV6Statistics(object):
    """ Provides Internet Control Message Protocol for Internet Protocol version 6 (ICMPv6) statistical data for the local computer. """
    DestinationUnreachableMessagesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) messages received because of a packet having an unreachable address in its destination.

Get: DestinationUnreachableMessagesReceived(self: IcmpV6Statistics) -> Int64

"""

    DestinationUnreachableMessagesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) messages sent because of a packet having an unreachable address in its destination.

Get: DestinationUnreachableMessagesSent(self: IcmpV6Statistics) -> Int64

"""

    EchoRepliesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Echo Reply messages received.

Get: EchoRepliesReceived(self: IcmpV6Statistics) -> Int64

"""

    EchoRepliesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Echo Reply messages sent.

Get: EchoRepliesSent(self: IcmpV6Statistics) -> Int64

"""

    EchoRequestsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Echo Request messages received.

Get: EchoRequestsReceived(self: IcmpV6Statistics) -> Int64

"""

    EchoRequestsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Echo Request messages sent.

Get: EchoRequestsSent(self: IcmpV6Statistics) -> Int64

"""

    ErrorsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) error messages received.

Get: ErrorsReceived(self: IcmpV6Statistics) -> Int64

"""

    ErrorsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) error messages sent.

Get: ErrorsSent(self: IcmpV6Statistics) -> Int64

"""

    MembershipQueriesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Group management Protocol (IGMP) Group Membership Query messages received.

Get: MembershipQueriesReceived(self: IcmpV6Statistics) -> Int64

"""

    MembershipQueriesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Group management Protocol (IGMP) Group Membership Query messages sent.

Get: MembershipQueriesSent(self: IcmpV6Statistics) -> Int64

"""

    MembershipReductionsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Group Management Protocol (IGMP) Group Membership Reduction messages received.

Get: MembershipReductionsReceived(self: IcmpV6Statistics) -> Int64

"""

    MembershipReductionsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Group Management Protocol (IGMP) Group Membership Reduction messages sent.

Get: MembershipReductionsSent(self: IcmpV6Statistics) -> Int64

"""

    MembershipReportsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Group Management Protocol (IGMP) Group Membership Report messages received.

Get: MembershipReportsReceived(self: IcmpV6Statistics) -> Int64

"""

    MembershipReportsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Group Management Protocol (IGMP) Group Membership Report messages sent.

Get: MembershipReportsSent(self: IcmpV6Statistics) -> Int64

"""

    MessagesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) messages received.

Get: MessagesReceived(self: IcmpV6Statistics) -> Int64

"""

    MessagesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) messages sent.

Get: MessagesSent(self: IcmpV6Statistics) -> Int64

"""

    NeighborAdvertisementsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Neighbor Advertisement messages received.

Get: NeighborAdvertisementsReceived(self: IcmpV6Statistics) -> Int64

"""

    NeighborAdvertisementsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Neighbor Advertisement messages sent.

Get: NeighborAdvertisementsSent(self: IcmpV6Statistics) -> Int64

"""

    NeighborSolicitsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Neighbor Solicitation messages received.

Get: NeighborSolicitsReceived(self: IcmpV6Statistics) -> Int64

"""

    NeighborSolicitsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Neighbor Solicitation messages sent.

Get: NeighborSolicitsSent(self: IcmpV6Statistics) -> Int64

"""

    PacketTooBigMessagesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Packet Too Big messages received.

Get: PacketTooBigMessagesReceived(self: IcmpV6Statistics) -> Int64

"""

    PacketTooBigMessagesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Packet Too Big messages sent.

Get: PacketTooBigMessagesSent(self: IcmpV6Statistics) -> Int64

"""

    ParameterProblemsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Parameter Problem messages received.

Get: ParameterProblemsReceived(self: IcmpV6Statistics) -> Int64

"""

    ParameterProblemsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Parameter Problem messages sent.

Get: ParameterProblemsSent(self: IcmpV6Statistics) -> Int64

"""

    RedirectsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Redirect messages received.

Get: RedirectsReceived(self: IcmpV6Statistics) -> Int64

"""

    RedirectsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Redirect messages sent.

Get: RedirectsSent(self: IcmpV6Statistics) -> Int64

"""

    RouterAdvertisementsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Router Advertisement messages received.

Get: RouterAdvertisementsReceived(self: IcmpV6Statistics) -> Int64

"""

    RouterAdvertisementsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Router Advertisement messages sent.

Get: RouterAdvertisementsSent(self: IcmpV6Statistics) -> Int64

"""

    RouterSolicitsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Router Solicitation messages received.

Get: RouterSolicitsReceived(self: IcmpV6Statistics) -> Int64

"""

    RouterSolicitsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Router Solicitation messages sent.

Get: RouterSolicitsSent(self: IcmpV6Statistics) -> Int64

"""

    TimeExceededMessagesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Time Exceeded messages received.

Get: TimeExceededMessagesReceived(self: IcmpV6Statistics) -> Int64

"""

    TimeExceededMessagesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Control Message Protocol version 6 (ICMPv6) Time Exceeded messages sent.

Get: TimeExceededMessagesSent(self: IcmpV6Statistics) -> Int64

"""



class IPAddressCollection(object, ICollection[IPAddress], IEnumerable[IPAddress], IEnumerable):
    """ Stores a set of System.Net.IPAddress types. """
    def Add(self, address):
        """
        Add(self: IPAddressCollection, address: IPAddress)
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        
        
            address: The object to be added to the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: IPAddressCollection)
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        """
        pass

    def Contains(self, address):
        """
        Contains(self: IPAddressCollection, address: IPAddress) -> bool
        
            Checks whether the collection contains the specified System.Net.IPAddress object.
        
            address: The System.Net.IPAddress object to be searched in the collection.
            Returns: true if the System.Net.IPAddress object exists in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, offset):
        """
        CopyTo(self: IPAddressCollection, array: Array[IPAddress], offset: int)
            Copies the elements in this collection to a one-dimensional array of type System.Net.IPAddress.
        
            array: A one-dimensional array that receives a copy of the collection.
            offset: The zero-based index in array at which the copy begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: IPAddressCollection) -> IEnumerator[IPAddress]
        
            Returns an object that can be used to iterate through this collection.
            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to 
             the System.Net.NetworkInformation.IPAddressCollection types in this collection.
        """
        pass

    def Remove(self, address):
        """
        Remove(self: IPAddressCollection, address: IPAddress) -> bool
        
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        
        
            address: The object to be removed.
            Returns: Always throws a System.NotSupportedException.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[IPAddress], item: IPAddress) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Net.IPAddress types in this collection.

Get: Count(self: IPAddressCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to this collection is read-only.

Get: IsReadOnly(self: IPAddressCollection) -> bool

"""



class IPAddressInformation(object):
    """ Provides information about a network interface address. """
    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Internet Protocol (IP) address.

Get: Address(self: IPAddressInformation) -> IPAddress

"""

    IsDnsEligible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the Internet Protocol (IP) address is valid to appear in a Domain Name System (DNS) server database.

Get: IsDnsEligible(self: IPAddressInformation) -> bool

"""

    IsTransient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the Internet Protocol (IP) address is transient (a cluster address).

Get: IsTransient(self: IPAddressInformation) -> bool

"""



class IPAddressInformationCollection(object, ICollection[IPAddressInformation], IEnumerable[IPAddressInformation], IEnumerable):
    """ Stores a set of System.Net.NetworkInformation.IPAddressInformation types. """
    def Add(self, address):
        """
        Add(self: IPAddressInformationCollection, address: IPAddressInformation)
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        
        
            address: The object to be added to the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: IPAddressInformationCollection)
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        """
        pass

    def Contains(self, address):
        """
        Contains(self: IPAddressInformationCollection, address: IPAddressInformation) -> bool
        
            Checks whether the collection contains the specified 
             System.Net.NetworkInformation.IPAddressInformation object.
        
        
            address: The System.Net.NetworkInformation.IPAddressInformation object to be searched in the collection.
            Returns: true if the System.Net.NetworkInformation.IPAddressInformation object exists in the collection; 
             otherwise. false.
        """
        pass

    def CopyTo(self, array, offset):
        """
        CopyTo(self: IPAddressInformationCollection, array: Array[IPAddressInformation], offset: int)
            Copies the collection to the specified array.
        
            array: A one-dimensional array that receives a copy of the collection.
            offset: The zero-based index in array at which the copy begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: IPAddressInformationCollection) -> IEnumerator[IPAddressInformation]
        
            Returns an object that can be used to iterate through this collection.
            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to 
             the System.Net.NetworkInformation.IPAddressInformation types in this collection.
        """
        pass

    def Remove(self, address):
        """
        Remove(self: IPAddressInformationCollection, address: IPAddressInformation) -> bool
        
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        
        
            address: The object to be removed.
            Returns: Always throws a System.NotSupportedException.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[IPAddressInformation], item: IPAddressInformation) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Net.NetworkInformation.IPAddressInformation types in this collection.

Get: Count(self: IPAddressInformationCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to this collection is read-only.

Get: IsReadOnly(self: IPAddressInformationCollection) -> bool

"""



class IPGlobalProperties(object):
    """ Provides information about the network connectivity of the local computer. """
    def BeginGetUnicastAddresses(self, callback, state):
        """
        BeginGetUnicastAddresses(self: IPGlobalProperties, callback: AsyncCallback, state: object) -> IAsyncResult
        
            Begins an asynchronous request to retrieve the stable unicast IP address table on the local 
             computer.
        
        
            callback: The System.AsyncCallback delegate.
            state: An object that contains state information for this request.
            Returns: An System.IAsyncResult that references the asynchronous request.
        """
        pass

    def EndGetUnicastAddresses(self, asyncResult):
        """
        EndGetUnicastAddresses(self: IPGlobalProperties, asyncResult: IAsyncResult) -> UnicastIPAddressInformationCollection
        
            Ends a pending asynchronous request to retrieve the stable unicast IP address table on the local 
             computer.
        
        
            asyncResult: An System.IAsyncResult that references the asynchronous request.
            Returns: An System.IAsyncResult that stores state information and any user defined data for this 
             asynchronous operation.
        """
        pass

    def GetActiveTcpConnections(self):
        """
        GetActiveTcpConnections(self: IPGlobalProperties) -> Array[TcpConnectionInformation]
        
            Returns information about the Internet Protocol version 4 (IPv4) and IPv6 Transmission Control 
             Protocol (TCP) connections on the local computer.
        
            Returns: A System.Net.NetworkInformation.TcpConnectionInformation array that contains objects that 
             describe the active TCP connections, or an empty array if no active TCP connections are 
             detected.
        """
        pass

    def GetActiveTcpListeners(self):
        """
        GetActiveTcpListeners(self: IPGlobalProperties) -> Array[IPEndPoint]
        
            Returns endpoint information about the Internet Protocol version 4 (IPv4) and IPv6 Transmission 
             Control Protocol (TCP) listeners on the local computer.
        
            Returns: A System.Net.IPEndPoint array that contains objects that describe the active TCP listeners, or 
             an empty array, if no active TCP listeners are detected.
        """
        pass

    def GetActiveUdpListeners(self):
        """
        GetActiveUdpListeners(self: IPGlobalProperties) -> Array[IPEndPoint]
        
            Returns information about the Internet Protocol version 4 (IPv4) and IPv6 User Datagram Protocol 
             (UDP) listeners on the local computer.
        
            Returns: An System.Net.IPEndPoint array that contains objects that describe the UDP listeners, or an 
             empty array if no UDP listeners are detected.
        """
        pass

    def GetIcmpV4Statistics(self):
        """
        GetIcmpV4Statistics(self: IPGlobalProperties) -> IcmpV4Statistics
        
            Provides Internet Control Message Protocol (ICMP) version 4 statistical data for the local 
             computer.
        
            Returns: An System.Net.NetworkInformation.IcmpV4Statistics object that provides ICMP version 4 traffic 
             statistics for the local computer.
        """
        pass

    def GetIcmpV6Statistics(self):
        """
        GetIcmpV6Statistics(self: IPGlobalProperties) -> IcmpV6Statistics
        
            Provides Internet Control Message Protocol (ICMP) version 6 statistical data for the local 
             computer.
        
            Returns: An System.Net.NetworkInformation.IcmpV6Statistics object that provides ICMP version 6 traffic 
             statistics for the local computer.
        """
        pass

    @staticmethod
    def GetIPGlobalProperties():
        """
        GetIPGlobalProperties() -> IPGlobalProperties
        
            Gets an object that provides information about the local computer's network connectivity and 
             traffic statistics.
        
            Returns: A System.Net.NetworkInformation.IPGlobalProperties object that contains information about the 
             local computer.
        """
        pass

    def GetIPv4GlobalStatistics(self):
        """
        GetIPv4GlobalStatistics(self: IPGlobalProperties) -> IPGlobalStatistics
        
            Provides Internet Protocol version 4 (IPv4) statistical data for the local computer.
            Returns: An System.Net.NetworkInformation.IPGlobalStatistics object that provides IPv4 traffic statistics 
             for the local computer.
        """
        pass

    def GetIPv6GlobalStatistics(self):
        """
        GetIPv6GlobalStatistics(self: IPGlobalProperties) -> IPGlobalStatistics
        
            Provides Internet Protocol version 6 (IPv6) statistical data for the local computer.
            Returns: An System.Net.NetworkInformation.IPGlobalStatistics object that provides IPv6 traffic statistics 
             for the local computer.
        """
        pass

    def GetTcpIPv4Statistics(self):
        """
        GetTcpIPv4Statistics(self: IPGlobalProperties) -> TcpStatistics
        
            Provides Transmission Control Protocol/Internet Protocol version 4 (TCP/IPv4) statistical data 
             for the local computer.
        
            Returns: A System.Net.NetworkInformation.TcpStatistics object that provides TCP/IPv4 traffic statistics 
             for the local computer.
        """
        pass

    def GetTcpIPv6Statistics(self):
        """
        GetTcpIPv6Statistics(self: IPGlobalProperties) -> TcpStatistics
        
            Provides Transmission Control Protocol/Internet Protocol version 6 (TCP/IPv6) statistical data 
             for the local computer.
        
            Returns: A System.Net.NetworkInformation.TcpStatistics object that provides TCP/IPv6 traffic statistics 
             for the local computer.
        """
        pass

    def GetUdpIPv4Statistics(self):
        """
        GetUdpIPv4Statistics(self: IPGlobalProperties) -> UdpStatistics
        
            Provides User Datagram Protocol/Internet Protocol version 4 (UDP/IPv4) statistical data for the 
             local computer.
        
            Returns: A System.Net.NetworkInformation.UdpStatistics object that provides UDP/IPv4 traffic statistics 
             for the local computer.
        """
        pass

    def GetUdpIPv6Statistics(self):
        """
        GetUdpIPv6Statistics(self: IPGlobalProperties) -> UdpStatistics
        
            Provides User Datagram Protocol/Internet Protocol version 6 (UDP/IPv6) statistical data for the 
             local computer.
        
            Returns: A System.Net.NetworkInformation.UdpStatistics object that provides UDP/IPv6 traffic statistics 
             for the local computer.
        """
        pass

    def GetUnicastAddresses(self):
        """
        GetUnicastAddresses(self: IPGlobalProperties) -> UnicastIPAddressInformationCollection
        
            Retrieves the stable unicast IP address table on the local computer.
            Returns: A System.Net.NetworkInformation.UnicastIPAddressInformationCollection that contains a list of 
             stable unicast IP addresses on the local computer.
        """
        pass

    def GetUnicastAddressesAsync(self):
        """ GetUnicastAddressesAsync(self: IPGlobalProperties) -> Task[UnicastIPAddressInformationCollection] """
        pass

    DhcpScopeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Dynamic Host Configuration Protocol (DHCP) scope name.

Get: DhcpScopeName(self: IPGlobalProperties) -> str

"""

    DomainName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the domain in which the local computer is registered.

Get: DomainName(self: IPGlobalProperties) -> str

"""

    HostName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the host name for the local computer.

Get: HostName(self: IPGlobalProperties) -> str

"""

    IsWinsProxy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that specifies whether the local computer is acting as a Windows Internet Name Service (WINS) proxy.

Get: IsWinsProxy(self: IPGlobalProperties) -> bool

"""

    NodeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Network Basic Input/Output System (NetBIOS) node type of the local computer.

Get: NodeType(self: IPGlobalProperties) -> NetBiosNodeType

"""



class IPGlobalStatistics(object):
    """ Provides Internet Protocol (IP) statistical data. """
    DefaultTtl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default time-to-live (TTL) value for Internet Protocol (IP) packets.

Get: DefaultTtl(self: IPGlobalStatistics) -> int

"""

    ForwardingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that specifies whether Internet Protocol (IP) packet forwarding is enabled.

Get: ForwardingEnabled(self: IPGlobalStatistics) -> bool

"""

    NumberOfInterfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of network interfaces.

Get: NumberOfInterfaces(self: IPGlobalStatistics) -> int

"""

    NumberOfIPAddresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) addresses assigned to the local computer.

Get: NumberOfIPAddresses(self: IPGlobalStatistics) -> int

"""

    NumberOfRoutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of routes in the Internet Protocol (IP) routing table.

Get: NumberOfRoutes(self: IPGlobalStatistics) -> int

"""

    OutputPacketRequests = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of outbound Internet Protocol (IP) packets.

Get: OutputPacketRequests(self: IPGlobalStatistics) -> Int64

"""

    OutputPacketRoutingDiscards = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of routes that have been discarded from the routing table.

Get: OutputPacketRoutingDiscards(self: IPGlobalStatistics) -> Int64

"""

    OutputPacketsDiscarded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of transmitted Internet Protocol (IP) packets that have been discarded.

Get: OutputPacketsDiscarded(self: IPGlobalStatistics) -> Int64

"""

    OutputPacketsWithNoRoute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets for which the local computer could not determine a route to the destination address.

Get: OutputPacketsWithNoRoute(self: IPGlobalStatistics) -> Int64

"""

    PacketFragmentFailures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets that could not be fragmented.

Get: PacketFragmentFailures(self: IPGlobalStatistics) -> Int64

"""

    PacketReassembliesRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets that required reassembly.

Get: PacketReassembliesRequired(self: IPGlobalStatistics) -> Int64

"""

    PacketReassemblyFailures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets that were not successfully reassembled.

Get: PacketReassemblyFailures(self: IPGlobalStatistics) -> Int64

"""

    PacketReassemblyTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum amount of time within which all fragments of an Internet Protocol (IP) packet must arrive.

Get: PacketReassemblyTimeout(self: IPGlobalStatistics) -> Int64

"""

    PacketsFragmented = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets fragmented.

Get: PacketsFragmented(self: IPGlobalStatistics) -> Int64

"""

    PacketsReassembled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets reassembled.

Get: PacketsReassembled(self: IPGlobalStatistics) -> Int64

"""

    ReceivedPackets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets received.

Get: ReceivedPackets(self: IPGlobalStatistics) -> Int64

"""

    ReceivedPacketsDelivered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets delivered.

Get: ReceivedPacketsDelivered(self: IPGlobalStatistics) -> Int64

"""

    ReceivedPacketsDiscarded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets that have been received and discarded.

Get: ReceivedPacketsDiscarded(self: IPGlobalStatistics) -> Int64

"""

    ReceivedPacketsForwarded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets forwarded.

Get: ReceivedPacketsForwarded(self: IPGlobalStatistics) -> Int64

"""

    ReceivedPacketsWithAddressErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets with address errors that were received.

Get: ReceivedPacketsWithAddressErrors(self: IPGlobalStatistics) -> Int64

"""

    ReceivedPacketsWithHeadersErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets with header errors that were received.

Get: ReceivedPacketsWithHeadersErrors(self: IPGlobalStatistics) -> Int64

"""

    ReceivedPacketsWithUnknownProtocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Internet Protocol (IP) packets received on the local machine with an unknown protocol in the header.

Get: ReceivedPacketsWithUnknownProtocol(self: IPGlobalStatistics) -> Int64

"""



class IPInterfaceProperties(object):
    """ Provides information about network interfaces that support Internet Protocol version 4 (IPv4) or Internet Protocol version 6 (IPv6). """
    def GetIPv4Properties(self):
        """
        GetIPv4Properties(self: IPInterfaceProperties) -> IPv4InterfaceProperties
        
            Provides Internet Protocol version 4 (IPv4) configuration data for this network interface.
            Returns: An System.Net.NetworkInformation.IPv4InterfaceProperties object that contains IPv4 configuration 
             data, or null if no data is available for the interface.
        """
        pass

    def GetIPv6Properties(self):
        """
        GetIPv6Properties(self: IPInterfaceProperties) -> IPv6InterfaceProperties
        
            Provides Internet Protocol version 6 (IPv6) configuration data for this network interface.
            Returns: An System.Net.NetworkInformation.IPv6InterfaceProperties object that contains IPv6 configuration 
             data.
        """
        pass

    AnycastAddresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the anycast IP addresses assigned to this interface.

Get: AnycastAddresses(self: IPInterfaceProperties) -> IPAddressInformationCollection

"""

    DhcpServerAddresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the addresses of Dynamic Host Configuration Protocol (DHCP) servers for this interface.

Get: DhcpServerAddresses(self: IPInterfaceProperties) -> IPAddressCollection

"""

    DnsAddresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the addresses of Domain Name System (DNS) servers for this interface.

Get: DnsAddresses(self: IPInterfaceProperties) -> IPAddressCollection

"""

    DnsSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Domain Name System (DNS) suffix associated with this interface.

Get: DnsSuffix(self: IPInterfaceProperties) -> str

"""

    GatewayAddresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the IPv4 network gateway addresses for this interface.

Get: GatewayAddresses(self: IPInterfaceProperties) -> GatewayIPAddressInformationCollection

"""

    IsDnsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether NetBt is configured to use DNS name resolution on this interface.

Get: IsDnsEnabled(self: IPInterfaceProperties) -> bool

"""

    IsDynamicDnsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether this interface is configured to automatically register its IP address information with the Domain Name System (DNS).

Get: IsDynamicDnsEnabled(self: IPInterfaceProperties) -> bool

"""

    MulticastAddresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the multicast addresses assigned to this interface.

Get: MulticastAddresses(self: IPInterfaceProperties) -> MulticastIPAddressInformationCollection

"""

    UnicastAddresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unicast addresses assigned to this interface.

Get: UnicastAddresses(self: IPInterfaceProperties) -> UnicastIPAddressInformationCollection

"""

    WinsServersAddresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the addresses of Windows Internet Name Service (WINS) servers.

Get: WinsServersAddresses(self: IPInterfaceProperties) -> IPAddressCollection

"""



class IPInterfaceStatistics(object):
    # no doc
    BytesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BytesReceived(self: IPInterfaceStatistics) -> Int64

"""

    BytesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BytesSent(self: IPInterfaceStatistics) -> Int64

"""

    IncomingPacketsDiscarded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncomingPacketsDiscarded(self: IPInterfaceStatistics) -> Int64

"""

    IncomingPacketsWithErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncomingPacketsWithErrors(self: IPInterfaceStatistics) -> Int64

"""

    IncomingUnknownProtocolPackets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncomingUnknownProtocolPackets(self: IPInterfaceStatistics) -> Int64

"""

    NonUnicastPacketsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NonUnicastPacketsReceived(self: IPInterfaceStatistics) -> Int64

"""

    NonUnicastPacketsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NonUnicastPacketsSent(self: IPInterfaceStatistics) -> Int64

"""

    OutgoingPacketsDiscarded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutgoingPacketsDiscarded(self: IPInterfaceStatistics) -> Int64

"""

    OutgoingPacketsWithErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutgoingPacketsWithErrors(self: IPInterfaceStatistics) -> Int64

"""

    OutputQueueLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputQueueLength(self: IPInterfaceStatistics) -> Int64

"""

    UnicastPacketsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnicastPacketsReceived(self: IPInterfaceStatistics) -> Int64

"""

    UnicastPacketsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnicastPacketsSent(self: IPInterfaceStatistics) -> Int64

"""



class IPStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Reports the status of sending an Internet Control Message Protocol (ICMP) echo message to a computer.
    
    enum IPStatus, values: BadDestination (11018), BadHeader (11042), BadOption (11007), BadRoute (11012), DestinationHostUnreachable (11003), DestinationNetworkUnreachable (11002), DestinationPortUnreachable (11005), DestinationProhibited (11004), DestinationProtocolUnreachable (11004), DestinationScopeMismatch (11045), DestinationUnreachable (11040), HardwareError (11008), IcmpError (11044), NoResources (11006), PacketTooBig (11009), ParameterProblem (11015), SourceQuench (11016), Success (0), TimedOut (11010), TimeExceeded (11041), TtlExpired (11013), TtlReassemblyTimeExceeded (11014), Unknown (-1), UnrecognizedNextHeader (11043)
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

    BadDestination = None
    BadHeader = None
    BadOption = None
    BadRoute = None
    DestinationHostUnreachable = None
    DestinationNetworkUnreachable = None
    DestinationPortUnreachable = None
    DestinationProhibited = None
    DestinationProtocolUnreachable = None
    DestinationScopeMismatch = None
    DestinationUnreachable = None
    HardwareError = None
    IcmpError = None
    NoResources = None
    PacketTooBig = None
    ParameterProblem = None
    SourceQuench = None
    Success = None
    TimedOut = None
    TimeExceeded = None
    TtlExpired = None
    TtlReassemblyTimeExceeded = None
    Unknown = None
    UnrecognizedNextHeader = None
    value__ = None


class IPv4InterfaceProperties(object):
    """ Provides information about network interfaces that support Internet Protocol version 4 (IPv4). """
    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of the network interface associated with the Internet Protocol version 4 (IPv4) address.

Get: Index(self: IPv4InterfaceProperties) -> int

"""

    IsAutomaticPrivateAddressingActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether this interface has an automatic private IP addressing (APIPA) address.

Get: IsAutomaticPrivateAddressingActive(self: IPv4InterfaceProperties) -> bool

"""

    IsAutomaticPrivateAddressingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether this interface has automatic private IP addressing (APIPA) enabled.

Get: IsAutomaticPrivateAddressingEnabled(self: IPv4InterfaceProperties) -> bool

"""

    IsDhcpEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the interface is configured to use a Dynamic Host Configuration Protocol (DHCP) server to obtain an IP address.

Get: IsDhcpEnabled(self: IPv4InterfaceProperties) -> bool

"""

    IsForwardingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether this interface can forward (route) packets.

Get: IsForwardingEnabled(self: IPv4InterfaceProperties) -> bool

"""

    Mtu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum transmission unit (MTU) for this network interface.

Get: Mtu(self: IPv4InterfaceProperties) -> int

"""

    UsesWins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether an interface uses Windows Internet Name Service (WINS).

Get: UsesWins(self: IPv4InterfaceProperties) -> bool

"""



class IPv4InterfaceStatistics(object):
    """ Provides statistical data for a network interface on the local computer. """
    BytesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bytes that were received on the interface.

Get: BytesReceived(self: IPv4InterfaceStatistics) -> Int64

"""

    BytesSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bytes that were sent on the interface.

Get: BytesSent(self: IPv4InterfaceStatistics) -> Int64

"""

    IncomingPacketsDiscarded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of incoming packets that were discarded.

Get: IncomingPacketsDiscarded(self: IPv4InterfaceStatistics) -> Int64

"""

    IncomingPacketsWithErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of incoming packets with errors.

Get: IncomingPacketsWithErrors(self: IPv4InterfaceStatistics) -> Int64

"""

    IncomingUnknownProtocolPackets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of incoming packets with an unknown protocol.

Get: IncomingUnknownProtocolPackets(self: IPv4InterfaceStatistics) -> Int64

"""

    NonUnicastPacketsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of non-unicast packets that were received on the interface.

Get: NonUnicastPacketsReceived(self: IPv4InterfaceStatistics) -> Int64

"""

    NonUnicastPacketsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of non-unicast packets that were sent on the interface.

Get: NonUnicastPacketsSent(self: IPv4InterfaceStatistics) -> Int64

"""

    OutgoingPacketsDiscarded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of outgoing packets that were discarded.

Get: OutgoingPacketsDiscarded(self: IPv4InterfaceStatistics) -> Int64

"""

    OutgoingPacketsWithErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of outgoing packets with errors.

Get: OutgoingPacketsWithErrors(self: IPv4InterfaceStatistics) -> Int64

"""

    OutputQueueLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the output queue.

Get: OutputQueueLength(self: IPv4InterfaceStatistics) -> Int64

"""

    UnicastPacketsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of unicast packets that were received on the interface.

Get: UnicastPacketsReceived(self: IPv4InterfaceStatistics) -> Int64

"""

    UnicastPacketsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of unicast packets that were sent on the interface.

Get: UnicastPacketsSent(self: IPv4InterfaceStatistics) -> Int64

"""



class IPv6InterfaceProperties(object):
    """ Provides information about network interfaces that support Internet Protocol version 6 (IPv6). """
    def GetScopeId(self, scopeLevel):
        """ GetScopeId(self: IPv6InterfaceProperties, scopeLevel: ScopeLevel) -> Int64 """
        pass

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of the network interface associated with an Internet Protocol version 6 (IPv6) address.

Get: Index(self: IPv6InterfaceProperties) -> int

"""

    Mtu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum transmission unit (MTU) for this network interface.

Get: Mtu(self: IPv6InterfaceProperties) -> int

"""



class MulticastIPAddressInformation(IPAddressInformation):
    """ Provides information about a network interface's multicast address. """
    AddressPreferredLifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of seconds remaining during which this address is the preferred address.

Get: AddressPreferredLifetime(self: MulticastIPAddressInformation) -> Int64

"""

    AddressValidLifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of seconds remaining during which this address is valid.

Get: AddressValidLifetime(self: MulticastIPAddressInformation) -> Int64

"""

    DhcpLeaseLifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the amount of time remaining on the Dynamic Host Configuration Protocol (DHCP) lease for this IP address.

Get: DhcpLeaseLifetime(self: MulticastIPAddressInformation) -> Int64

"""

    DuplicateAddressDetectionState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the state of the duplicate address detection algorithm.

Get: DuplicateAddressDetectionState(self: MulticastIPAddressInformation) -> DuplicateAddressDetectionState

"""

    PrefixOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the source of a Multicast Internet Protocol (IP) address prefix.

Get: PrefixOrigin(self: MulticastIPAddressInformation) -> PrefixOrigin

"""

    SuffixOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the source of a Multicast Internet Protocol (IP) address suffix.

Get: SuffixOrigin(self: MulticastIPAddressInformation) -> SuffixOrigin

"""



class MulticastIPAddressInformationCollection(object, ICollection[MulticastIPAddressInformation], IEnumerable[MulticastIPAddressInformation], IEnumerable):
    """ Stores a set of System.Net.NetworkInformation.MulticastIPAddressInformation types. """
    def Add(self, address):
        """
        Add(self: MulticastIPAddressInformationCollection, address: MulticastIPAddressInformation)
            Throws a System.NotSupportedException because the collection is read-only and elements cannot be 
             added to the collection.
        
        
            address: The object to be added to the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: MulticastIPAddressInformationCollection)
            Throws a System.NotSupportedException because the collection is read-only and elements cannot be 
             removed.
        """
        pass

    def Contains(self, address):
        """
        Contains(self: MulticastIPAddressInformationCollection, address: MulticastIPAddressInformation) -> bool
        
            Checks whether the collection contains the specified 
             System.Net.NetworkInformation.MulticastIPAddressInformation object.
        
        
            address: The System.Net.NetworkInformation.MulticastIPAddressInformation object to be searched in the 
             collection.
        
            Returns: true if the System.Net.NetworkInformation.MulticastIPAddressInformation object exists in the 
             collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, offset):
        """
        CopyTo(self: MulticastIPAddressInformationCollection, array: Array[MulticastIPAddressInformation], offset: int)
            Copies the elements in this collection to a one-dimensional array of type 
             System.Net.NetworkInformation.MulticastIPAddressInformation.
        
        
            array: A one-dimensional array that receives a copy of the collection.
            offset: The zero-based index in array at which the copy begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MulticastIPAddressInformationCollection) -> IEnumerator[MulticastIPAddressInformation]
        
            Returns an object that can be used to iterate through this collection.
            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to 
             the System.Net.NetworkInformation.UnicastIPAddressInformation types in this collection.
        """
        pass

    def Remove(self, address):
        """
        Remove(self: MulticastIPAddressInformationCollection, address: MulticastIPAddressInformation) -> bool
        
            Throws a System.NotSupportedException because the collection is read-only and elements cannot be 
             removed.
        
        
            address: The object to be removed.
            Returns: Always throws a System.NotSupportedException.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MulticastIPAddressInformation], item: MulticastIPAddressInformation) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Net.NetworkInformation.MulticastIPAddressInformation types in this collection.

Get: Count(self: MulticastIPAddressInformationCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to this collection is read-only.

Get: IsReadOnly(self: MulticastIPAddressInformationCollection) -> bool

"""



class NetBiosNodeType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the Network Basic Input/Output System (NetBIOS) node type.
    
    enum NetBiosNodeType, values: Broadcast (1), Hybrid (8), Mixed (4), Peer2Peer (2), Unknown (0)
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

    Broadcast = None
    Hybrid = None
    Mixed = None
    Peer2Peer = None
    Unknown = None
    value__ = None


class NetworkAddressChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    References one or more methods to be called when the address of a network interface changes.
    
    NetworkAddressChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: NetworkAddressChangedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: NetworkAddressChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: NetworkAddressChangedEventHandler, sender: object, e: EventArgs) """
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


class NetworkAvailabilityChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    References one or more methods to be called when the availability of the network changes.
    
    NetworkAvailabilityChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: NetworkAvailabilityChangedEventHandler, sender: object, e: NetworkAvailabilityEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: NetworkAvailabilityChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: NetworkAvailabilityChangedEventHandler, sender: object, e: NetworkAvailabilityEventArgs) """
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


class NetworkAvailabilityEventArgs(EventArgs):
    """ Provides data for the System.Net.NetworkInformation.NetworkChange.NetworkAvailabilityChanged event. """
    IsAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current status of the network connection.

Get: IsAvailable(self: NetworkAvailabilityEventArgs) -> bool

"""



class NetworkChange(object):
    """
    Allows applications to receive notification when the Internet Protocol (IP) address of a network interface, also called a network card or adapter, changes.
    
    NetworkChange()
    """
    @staticmethod
    def RegisterNetworkChange(nc):
        """ RegisterNetworkChange(nc: NetworkChange) """
        pass

    NetworkAddressChanged = None
    NetworkAvailabilityChanged = None


class NetworkInformationAccess(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies permission to access information about network interfaces and traffic statistics.
    
    enum (flags) NetworkInformationAccess, values: None (0), Ping (4), Read (1)
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
    Ping = None
    Read = None
    value__ = None


class NetworkInformationException(Win32Exception, ISerializable, _Exception):
    """
    The exception that is thrown when an error occurs while retrieving network information.
    
    NetworkInformationException()
    NetworkInformationException(errorCode: int)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, errorCode=None):
        """
        __new__(cls: type)
        __new__(cls: type, errorCode: int)
        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Win32 error code for this exception.

Get: ErrorCode(self: NetworkInformationException) -> int

"""



class NetworkInformationPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """
    Controls access to network information and traffic statistics for the local computer. This class cannot be inherited.
    
    NetworkInformationPermission(state: PermissionState)
    NetworkInformationPermission(access: NetworkInformationAccess)
    """
    def AddPermission(self, access):
        """
        AddPermission(self: NetworkInformationPermission, access: NetworkInformationAccess)
            Adds the specified value to this permission.
        
            access: One of the System.Net.NetworkInformation.NetworkInformationAccess values.
        """
        pass

    def Copy(self):
        """
        Copy(self: NetworkInformationPermission) -> IPermission
        
            Creates and returns an identical copy of this permission.
            Returns: A System.Net.NetworkInformation.NetworkInformationPermission that is identical to the current 
             permission
        """
        pass

    def FromXml(self, securityElement):
        """
        FromXml(self: NetworkInformationPermission, securityElement: SecurityElement)
            Sets the state of this permission using the specified XML encoding.
        
            securityElement: A System.Security.SecurityElement that contains the XML encoding to use to set the state of the 
             current permission
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: NetworkInformationPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission and the 
             specified permission.
        
        
            target: An System.Security.IPermission to intersect with the current permission. It must be of the same 
             type as the current permission.
        
            Returns: A System.Net.NetworkInformation.NetworkInformationPermission that represents the intersection of 
             the current permission and the specified permission. This new permission is null if the 
             intersection is empty or target is null.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: NetworkInformationPermission, target: IPermission) -> bool
        
            Determines whether the current permission is a subset of the specified permission.
        
            target: An System.Security.IPermission that is to be tested for the subset relationship. This permission 
             must be of the same type as the current permission
        
            Returns: true if the current permission is a subset of the specified permission; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: NetworkInformationPermission) -> bool
        
            Returns a value indicating whether the current permission is unrestricted.
            Returns: true if the current permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: NetworkInformationPermission) -> SecurityElement
        
            Creates an XML encoding of the state of this permission.
            Returns: A System.Security.SecurityElement that contains the XML encoding of the current permission.
        """
        pass

    def Union(self, target):
        """
        Union(self: NetworkInformationPermission, target: IPermission) -> IPermission
        
            Creates a permission that is the union of this permission and the specified permission.
        
            target: A System.Net.NetworkInformation.NetworkInformationPermission  permission to combine with the 
             current permission.
        
            Returns: A new permission that represents the union of the current permission and the specified 
             permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, access: NetworkInformationAccess)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the level of access to network information controlled by this permission.

Get: Access(self: NetworkInformationPermission) -> NetworkInformationAccess

"""



class NetworkInformationPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows security actions for System.Net.NetworkInformation.NetworkInformationPermission to be applied to code using declarative security.
    
    NetworkInformationPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: NetworkInformationPermissionAttribute) -> IPermission
        
            Creates and returns a new System.Net.NetworkInformation.NetworkInformationPermission object.
            Returns: A System.Net.NetworkInformation.NetworkInformationPermission that corresponds to this attribute.
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
    """Gets or sets the network information access level.

Get: Access(self: NetworkInformationPermissionAttribute) -> str

Set: Access(self: NetworkInformationPermissionAttribute) = value
"""



class NetworkInterface(object):
    """ Provides configuration and statistical information for a network interface. """
    @staticmethod
    def GetAllNetworkInterfaces():
        """
        GetAllNetworkInterfaces() -> Array[NetworkInterface]
        
            Returns objects that describe the network interfaces on the local computer.
            Returns: A System.Net.NetworkInformation.NetworkInterface array that contains objects that describe the 
             available network interfaces, or an empty array if no interfaces are detected.
        """
        pass

    def GetIPProperties(self):
        """
        GetIPProperties(self: NetworkInterface) -> IPInterfaceProperties
        
            Returns an object that describes the configuration of this network interface.
            Returns: An System.Net.NetworkInformation.IPInterfaceProperties object that describes this network 
             interface.
        """
        pass

    def GetIPStatistics(self):
        """ GetIPStatistics(self: NetworkInterface) -> IPInterfaceStatistics """
        pass

    def GetIPv4Statistics(self):
        """
        GetIPv4Statistics(self: NetworkInterface) -> IPv4InterfaceStatistics
        
            Gets the IPv4 statistics.
            Returns: An System.Net.NetworkInformation.IPv4InterfaceStatistics object.
        """
        pass

    @staticmethod
    def GetIsNetworkAvailable():
        """
        GetIsNetworkAvailable() -> bool
        
            Indicates whether any network connection is available.
            Returns: true if a network connection is available; otherwise, false.
        """
        pass

    def GetPhysicalAddress(self):
        """
        GetPhysicalAddress(self: NetworkInterface) -> PhysicalAddress
        
            Returns the Media Access Control (MAC) or physical address for this adapter.
            Returns: A System.Net.NetworkInformation.PhysicalAddress object that contains the physical address.
        """
        pass

    def Supports(self, networkInterfaceComponent):
        """
        Supports(self: NetworkInterface, networkInterfaceComponent: NetworkInterfaceComponent) -> bool
        
            Gets a System.Boolean value that indicates whether the interface supports the specified protocol.
        
            networkInterfaceComponent: A System.Net.NetworkInformation.NetworkInterfaceComponent value.
            Returns: true if the specified protocol is supported; otherwise, false.
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the description of the interface.

Get: Description(self: NetworkInterface) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the identifier of the network adapter.

Get: Id(self: NetworkInterface) -> str

"""

    IsReceiveOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the network interface is set to only receive data packets.

Get: IsReceiveOnly(self: NetworkInterface) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the network adapter.

Get: Name(self: NetworkInterface) -> str

"""

    NetworkInterfaceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the interface type.

Get: NetworkInterfaceType(self: NetworkInterface) -> NetworkInterfaceType

"""

    OperationalStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current operational state of the network connection.

Get: OperationalStatus(self: NetworkInterface) -> OperationalStatus

"""

    Speed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the speed of the network interface.

Get: Speed(self: NetworkInterface) -> Int64

"""

    SupportsMulticast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Boolean value that indicates whether the network interface is enabled to receive multicast packets.

Get: SupportsMulticast(self: NetworkInterface) -> bool

"""


    IPv6LoopbackInterfaceIndex = 1
    LoopbackInterfaceIndex = 1


class NetworkInterfaceComponent(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the Internet Protocol versions that are supported by a network interface.
    
    enum NetworkInterfaceComponent, values: IPv4 (0), IPv6 (1)
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

    IPv4 = None
    IPv6 = None
    value__ = None


class NetworkInterfaceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies types of network interfaces.
    
    enum NetworkInterfaceType, values: AsymmetricDsl (94), Atm (37), BasicIsdn (20), Ethernet (6), Ethernet3Megabit (26), FastEthernetFx (69), FastEthernetT (62), Fddi (15), GenericModem (48), GigabitEthernet (117), HighPerformanceSerialBus (144), IPOverAtm (114), Isdn (63), Loopback (24), MultiRateSymmetricDsl (143), Ppp (23), PrimaryIsdn (21), RateAdaptDsl (95), Slip (28), SymmetricDsl (96), TokenRing (9), Tunnel (131), Unknown (1), VeryHighSpeedDsl (97), Wireless80211 (71), Wman (237), Wwanpp (243), Wwanpp2 (244)
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

    AsymmetricDsl = None
    Atm = None
    BasicIsdn = None
    Ethernet = None
    Ethernet3Megabit = None
    FastEthernetFx = None
    FastEthernetT = None
    Fddi = None
    GenericModem = None
    GigabitEthernet = None
    HighPerformanceSerialBus = None
    IPOverAtm = None
    Isdn = None
    Loopback = None
    MultiRateSymmetricDsl = None
    Ppp = None
    PrimaryIsdn = None
    RateAdaptDsl = None
    Slip = None
    SymmetricDsl = None
    TokenRing = None
    Tunnel = None
    Unknown = None
    value__ = None
    VeryHighSpeedDsl = None
    Wireless80211 = None
    Wman = None
    Wwanpp = None
    Wwanpp2 = None


class OperationalStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the operational state of a network interface.
    
    enum OperationalStatus, values: Dormant (5), Down (2), LowerLayerDown (7), NotPresent (6), Testing (3), Unknown (4), Up (1)
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

    Dormant = None
    Down = None
    LowerLayerDown = None
    NotPresent = None
    Testing = None
    Unknown = None
    Up = None
    value__ = None


class PhysicalAddress(object):
    """
    Provides the Media Access Control (MAC) address for a network interface (adapter).
    
    PhysicalAddress(address: Array[Byte])
    """
    def Equals(self, comparand):
        """
        Equals(self: PhysicalAddress, comparand: object) -> bool
        
            Compares two System.Net.NetworkInformation.PhysicalAddress instances.
        
            comparand: The System.Net.NetworkInformation.PhysicalAddress  to compare to the current instance.
            Returns: true if this instance and the specified instance contain the same address; otherwise false.
        """
        pass

    def GetAddressBytes(self):
        """
        GetAddressBytes(self: PhysicalAddress) -> Array[Byte]
        
            Returns the address of the current instance.
            Returns: A System.Byte array containing the address.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PhysicalAddress) -> int
        
            Returns the hash value of a physical address.
            Returns: An integer hash value.
        """
        pass

    @staticmethod
    def Parse(address):
        """
        Parse(address: str) -> PhysicalAddress
        
            Parses the specified System.String and stores its contents as the address bytes of the 
             System.Net.NetworkInformation.PhysicalAddress returned by this method.
        
        
            address: A System.String containing the address that will be used to initialize the 
             System.Net.NetworkInformation.PhysicalAddress instance returned by this method.
        
            Returns: A System.Net.NetworkInformation.PhysicalAddress instance with the specified address.
        """
        pass

    def ToString(self):
        """
        ToString(self: PhysicalAddress) -> str
        
            Returns the System.String representation of the address of this instance.
            Returns: A System.String containing the address contained in this instance.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, address):
        """ __new__(cls: type, address: Array[Byte]) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    None = None


class Ping(Component, IComponent, IDisposable):
    """
    Allows an application to determine whether a remote computer is accessible over the network.
    
    Ping()
    """
    def Dispose(self):
        """
        Dispose(self: Ping, disposing: bool)
            Releases the unmanaged resources used by the System.Net.NetworkInformation.Ping object, and 
             optionally disposes of the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to releases only unmanaged resources.
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

    def OnPingCompleted(self, *args): #cannot find CLR method
        """
        OnPingCompleted(self: Ping, e: PingCompletedEventArgs)
            Raises the System.Net.NetworkInformation.Ping.PingCompleted event.
        
            e: A System.Net.NetworkInformation.PingCompletedEventArgs  object that contains event data.
        """
        pass

    def Send(self, *__args):
        """
        Send(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte]) -> PingReply
        
            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified 
             data buffer to the computer that has the specified System.Net.IPAddress, and receive a 
             corresponding ICMP echo reply message from that computer. This overload allows you to specify a 
             time-out value for the operation.
        
        
            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo 
             message.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the 
             ICMP echo reply message. The array cannot contain more than 65,500 bytes.
        
            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo 
             reply message, if one was received, or provides the reason for the failure, if no message was 
             received. The method will return System.Net.NetworkInformation.IPStatus.PacketTooBig if the 
             packet exceeds the Maximum Transmission Unit (MTU).
        
        Send(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte]) -> PingReply
        
            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified 
             data buffer to the specified computer, and receive a corresponding ICMP echo reply message from 
             that computer. This overload allows you to specify a time-out value for the operation.
        
        
            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. 
             The value specified for this parameter can be a host name or a string representation of an IP 
             address.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the 
             ICMP echo reply message. The array cannot contain more than 65,500 bytes.
        
            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo 
             reply message if one was received, or provides the reason for the failure if no message was 
             received.
        
        Send(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], options: PingOptions) -> PingReply
        
            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified 
             data buffer to the computer that has the specified System.Net.IPAddress and receive a 
             corresponding ICMP echo reply message from that computer. This overload allows you to specify a 
             time-out value for the operation and control fragmentation and Time-to-Live values for the ICMP 
             echo message packet.
        
        
            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo 
             message.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the 
             ICMP echo reply message. The array cannot contain more than 65,500 bytes.
        
            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and 
             Time-to-Live values for the ICMP echo message packet.
        
            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo 
             reply message, if one was received, or provides the reason for the failure, if no message was 
             received. The method will return System.Net.NetworkInformation.IPStatus.PacketTooBig if the 
             packet exceeds the Maximum Transmission Unit (MTU).
        
        Send(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], options: PingOptions) -> PingReply
        
            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified 
             data buffer to the specified computer, and receive a corresponding ICMP echo reply message from 
             that computer. This overload allows you to specify a time-out value for the operation and 
             control fragmentation and Time-to-Live values for the ICMP packet.
        
        
            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. 
             The value specified for this parameter can be a host name or a string representation of an IP 
             address.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the 
             ICMP echo reply message. The array cannot contain more than 65,500 bytes.
        
            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and 
             Time-to-Live values for the ICMP echo message packet.
        
            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo 
             reply message if one was received, or provides the reason for the failure if no message was 
             received.
        
        Send(self: Ping, hostNameOrAddress: str, timeout: int) -> PingReply
        
            Attempts to send an Internet Control Message Protocol (ICMP) echo message to the specified 
             computer, and receive a corresponding ICMP echo reply message from that computer. This method 
             allows you to specify a time-out value for the operation.
        
        
            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. 
             The value specified for this parameter can be a host name or a string representation of an IP 
             address.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo 
             reply message if one was received, or provides the reason for the failure if no message was 
             received.
        
        Send(self: Ping, hostNameOrAddress: str) -> PingReply
        
            Attempts to send an Internet Control Message Protocol (ICMP) echo message to the specified 
             computer, and receive a corresponding ICMP echo reply message from that computer.
        
        
            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. 
             The value specified for this parameter can be a host name or a string representation of an IP 
             address.
        
            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo 
             reply message, if one was received, or provides the reason for the failure, if no message was 
             received.
        
        Send(self: Ping, address: IPAddress, timeout: int) -> PingReply
        
            Attempts to send an Internet Control Message Protocol (ICMP) echo message with the specified 
             data buffer to the computer that has the specified System.Net.IPAddress, and receive a 
             corresponding ICMP echo reply message from that computer. This method allows you to specify a 
             time-out value for the operation.
        
        
            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo 
             message.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo 
             reply message if one was received, or provides the reason for the failure if no message was 
             received.
        
        Send(self: Ping, address: IPAddress) -> PingReply
        
            Attempts to send an Internet Control Message Protocol (ICMP) echo message to the computer that 
             has the specified System.Net.IPAddress, and receive a corresponding ICMP echo reply message from 
             that computer.
        
        
            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo 
             message.
        
            Returns: A System.Net.NetworkInformation.PingReply object that provides information about the ICMP echo 
             reply message, if one was received, or describes the reason for the failure if no message was 
             received.
        """
        pass

    def SendAsync(self, *__args):
        """
        SendAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], userToken: object)
            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message with 
             the specified data buffer to the computer that has the specified System.Net.IPAddress, and 
             receive a corresponding ICMP echo reply message from that computer. This overload allows you to 
             specify a time-out value for the operation.
        
        
            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo 
             message.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the 
             ICMP echo reply message. The array cannot contain more than 65,500 bytes.
        
            userToken: An object that is passed to the method invoked when the asynchronous operation completes.
        SendAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], userToken: object)
            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message with 
             the specified data buffer to the specified computer, and receive a corresponding ICMP echo reply 
             message from that computer. This overload allows you to specify a time-out value for the 
             operation.
        
        
            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. 
             The value specified for this parameter can be a host name or a string representation of an IP 
             address.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            buffer: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the 
             ICMP echo reply message. The array cannot contain more than 65,500 bytes.
        
            userToken: An object that is passed to the method invoked when the asynchronous operation completes.
        SendAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], options: PingOptions, userToken: object)
            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message with 
             the specified data buffer to the computer that has the specified System.Net.IPAddress, and 
             receive a corresponding ICMP echo reply message from that computer. This overload allows you to 
             specify a time-out value for the operation and control fragmentation and Time-to-Live values for 
             the ICMP echo message packet.
        
        
            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo 
             message.
        
            timeout: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the 
             ICMP echo reply message. The array cannot contain more than 65,500 bytes.
        
            buffer: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and 
             Time-to-Live values for the ICMP echo message packet.
        
            userToken: An object that is passed to the method invoked when the asynchronous operation completes.
        SendAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], options: PingOptions, userToken: object)
            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message with 
             the specified data buffer to the specified computer, and receive a corresponding ICMP echo reply 
             message from that computer. This overload allows you to specify a time-out value for the 
             operation and control fragmentation and Time-to-Live values for the ICMP packet.
        
        
            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. 
             The value specified for this parameter can be a host name or a string representation of an IP 
             address.
        
            timeout: A System.Byte array that contains data to be sent with the ICMP echo message and returned in the 
             ICMP echo reply message. The array cannot contain more than 65,500 bytes.
        
            buffer: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            options: A System.Net.NetworkInformation.PingOptions  object used to control fragmentation and 
             Time-to-Live values for the ICMP echo message packet.
        
            userToken: An object that is passed to the method invoked when the asynchronous operation completes.
        SendAsync(self: Ping, hostNameOrAddress: str, timeout: int, userToken: object)
            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message to the 
             specified computer, and receive a corresponding ICMP echo reply message from that computer. This 
             overload allows you to specify a time-out value for the operation.
        
        
            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. 
             The value specified for this parameter can be a host name or a string representation of an IP 
             address.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            userToken: An object that is passed to the method invoked when the asynchronous operation completes.
        SendAsync(self: Ping, hostNameOrAddress: str, userToken: object)
            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message to the 
             specified computer, and receive a corresponding ICMP echo reply message from that computer.
        
        
            hostNameOrAddress: A System.String that identifies the computer that is the destination for the ICMP echo message. 
             The value specified for this parameter can be a host name or a string representation of an IP 
             address.
        
            userToken: An object that is passed to the method invoked when the asynchronous operation completes.
        SendAsync(self: Ping, address: IPAddress, timeout: int, userToken: object)
            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message to the 
             computer that has the specified System.Net.IPAddress, and receive a corresponding ICMP echo 
             reply message from that computer. This overload allows you to specify a time-out value for the 
             operation.
        
        
            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo 
             message.
        
            timeout: An System.Int32 value that specifies the maximum number of milliseconds (after sending the echo 
             message) to wait for the ICMP echo reply message.
        
            userToken: An object that is passed to the method invoked when the asynchronous operation completes.
        SendAsync(self: Ping, address: IPAddress, userToken: object)
            Asynchronously attempts to send an Internet Control Message Protocol (ICMP) echo message to the 
             computer that has the specified System.Net.IPAddress, and receive a corresponding ICMP echo 
             reply message from that computer.
        
        
            address: An System.Net.IPAddress that identifies the computer that is the destination for the ICMP echo 
             message.
        
            userToken: An object that is passed to the method invoked when the asynchronous operation completes.
        """
        pass

    def SendAsyncCancel(self):
        """
        SendAsyncCancel(self: Ping)
            Cancels all pending asynchronous requests to send an Internet Control Message Protocol (ICMP) 
             echo message and receives a corresponding ICMP echo reply message.
        """
        pass

    def SendPingAsync(self, *__args):
        """
        SendPingAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte]) -> Task[PingReply]
        SendPingAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte]) -> Task[PingReply]
        SendPingAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], options: PingOptions) -> Task[PingReply]
        SendPingAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], options: PingOptions) -> Task[PingReply]
        SendPingAsync(self: Ping, hostNameOrAddress: str) -> Task[PingReply]
        SendPingAsync(self: Ping, address: IPAddress) -> Task[PingReply]
        SendPingAsync(self: Ping, hostNameOrAddress: str, timeout: int) -> Task[PingReply]
        SendPingAsync(self: Ping, address: IPAddress, timeout: int) -> Task[PingReply]
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

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""


    PingCompleted = None


class PingCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.NetworkInformation.Ping.PingCompleted event. """
    Reply = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that contains data that describes an attempt to send an Internet Control Message Protocol (ICMP) echo request message and receive a corresponding ICMP echo reply message.

Get: Reply(self: PingCompletedEventArgs) -> PingReply

"""



class PingCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Net.NetworkInformation.Ping.PingCompleted event of a System.Net.NetworkInformation.Ping object.
    
    PingCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PingCompletedEventHandler, sender: object, e: PingCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: PingCompletedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PingCompletedEventHandler, sender: object, e: PingCompletedEventArgs) """
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


class PingException(InvalidOperationException, ISerializable, _Exception):
    """
    The exception that is thrown when a erload:System.Net.NetworkInformation.Ping.Send or erload:System.Net.NetworkInformation.Ping.SendAsync method calls a method that throws an exception.
    
    PingException(message: str)
    PingException(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message, innerException=None):
        """
        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class PingOptions(object):
    """
    Used to control how System.Net.NetworkInformation.Ping data packets are transmitted.
    
    PingOptions(ttl: int, dontFragment: bool)
    PingOptions()
    """
    @staticmethod # known case of __new__
    def __new__(self, ttl=None, dontFragment=None):
        """
        __new__(cls: type, ttl: int, dontFragment: bool)
        __new__(cls: type)
        """
        pass

    DontFragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that controls fragmentation of the data sent to the remote host.

Get: DontFragment(self: PingOptions) -> bool

Set: DontFragment(self: PingOptions) = value
"""

    Ttl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of routing nodes that can forward the System.Net.NetworkInformation.Ping data before it is discarded.

Get: Ttl(self: PingOptions) -> int

Set: Ttl(self: PingOptions) = value
"""



class PingReply(object):
    """ Provides information about the status and data resulting from a erload:System.Net.NetworkInformation.Ping.Send or erload:System.Net.NetworkInformation.Ping.SendAsync operation. """
    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the address of the host that sends the Internet Control Message Protocol (ICMP) echo reply.

Get: Address(self: PingReply) -> IPAddress

"""

    Buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the buffer of data received in an Internet Control Message Protocol (ICMP) echo reply message.

Get: Buffer(self: PingReply) -> Array[Byte]

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the options used to transmit the reply to an Internet Control Message Protocol (ICMP) echo request.

Get: Options(self: PingReply) -> PingOptions

"""

    RoundtripTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of milliseconds taken to send an Internet Control Message Protocol (ICMP) echo request and receive the corresponding ICMP echo reply message.

Get: RoundtripTime(self: PingReply) -> Int64

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the status of an attempt to send an Internet Control Message Protocol (ICMP) echo request and receive the corresponding ICMP echo reply message.

Get: Status(self: PingReply) -> IPStatus

"""



class PrefixOrigin(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how an IP address network prefix was located.
    
    enum PrefixOrigin, values: Dhcp (3), Manual (1), Other (0), RouterAdvertisement (4), WellKnown (2)
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

    Dhcp = None
    Manual = None
    Other = None
    RouterAdvertisement = None
    value__ = None
    WellKnown = None


class ScopeLevel(Enum, IComparable, IFormattable, IConvertible):
    """ enum ScopeLevel, values: Admin (4), Global (14), Interface (1), Link (2), None (0), Organization (8), Site (5), Subnet (3) """
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

    Admin = None
    Global = None
    Interface = None
    Link = None
    None = None
    Organization = None
    Site = None
    Subnet = None
    value__ = None


class SuffixOrigin(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how an IP address host suffix was located.
    
    enum SuffixOrigin, values: LinkLayerAddress (4), Manual (1), OriginDhcp (3), Other (0), Random (5), WellKnown (2)
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

    LinkLayerAddress = None
    Manual = None
    OriginDhcp = None
    Other = None
    Random = None
    value__ = None
    WellKnown = None


class TcpConnectionInformation(object):
    """ Provides information about the Transmission Control Protocol (TCP) connections on the local computer. """
    LocalEndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the local endpoint of a Transmission Control Protocol (TCP) connection.

Get: LocalEndPoint(self: TcpConnectionInformation) -> IPEndPoint

"""

    RemoteEndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the remote endpoint of a Transmission Control Protocol (TCP) connection.

Get: RemoteEndPoint(self: TcpConnectionInformation) -> IPEndPoint

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of this Transmission Control Protocol (TCP) connection.

Get: State(self: TcpConnectionInformation) -> TcpState

"""



class TcpState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the states of a Transmission Control Protocol (TCP) connection.
    
    enum TcpState, values: Closed (1), CloseWait (8), Closing (9), DeleteTcb (12), Established (5), FinWait1 (6), FinWait2 (7), LastAck (10), Listen (2), SynReceived (4), SynSent (3), TimeWait (11), Unknown (0)
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

    Closed = None
    CloseWait = None
    Closing = None
    DeleteTcb = None
    Established = None
    FinWait1 = None
    FinWait2 = None
    LastAck = None
    Listen = None
    SynReceived = None
    SynSent = None
    TimeWait = None
    Unknown = None
    value__ = None


class TcpStatistics(object):
    """ Provides Transmission Control Protocol (TCP) statistical data. """
    ConnectionsAccepted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of accepted Transmission Control Protocol (TCP) connection requests.

Get: ConnectionsAccepted(self: TcpStatistics) -> Int64

"""

    ConnectionsInitiated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Transmission Control Protocol (TCP) connection requests made by clients.

Get: ConnectionsInitiated(self: TcpStatistics) -> Int64

"""

    CumulativeConnections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the total number of Transmission Control Protocol (TCP) connections established.

Get: CumulativeConnections(self: TcpStatistics) -> Int64

"""

    CurrentConnections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of current Transmission Control Protocol (TCP) connections.

Get: CurrentConnections(self: TcpStatistics) -> Int64

"""

    ErrorsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Transmission Control Protocol (TCP) errors received.

Get: ErrorsReceived(self: TcpStatistics) -> Int64

"""

    FailedConnectionAttempts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of failed Transmission Control Protocol (TCP) connection attempts.

Get: FailedConnectionAttempts(self: TcpStatistics) -> Int64

"""

    MaximumConnections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum number of supported Transmission Control Protocol (TCP) connections.

Get: MaximumConnections(self: TcpStatistics) -> Int64

"""

    MaximumTransmissionTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum retransmission time-out value for Transmission Control Protocol (TCP) segments.

Get: MaximumTransmissionTimeout(self: TcpStatistics) -> Int64

"""

    MinimumTransmissionTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minimum retransmission time-out value for Transmission Control Protocol (TCP) segments.

Get: MinimumTransmissionTimeout(self: TcpStatistics) -> Int64

"""

    ResetConnections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of RST packets received by Transmission Control Protocol (TCP) connections.

Get: ResetConnections(self: TcpStatistics) -> Int64

"""

    ResetsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Transmission Control Protocol (TCP) segments sent with the reset flag set.

Get: ResetsSent(self: TcpStatistics) -> Int64

"""

    SegmentsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Transmission Control Protocol (TCP) segments received.

Get: SegmentsReceived(self: TcpStatistics) -> Int64

"""

    SegmentsResent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Transmission Control Protocol (TCP) segments re-sent.

Get: SegmentsResent(self: TcpStatistics) -> Int64

"""

    SegmentsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of Transmission Control Protocol (TCP) segments sent.

Get: SegmentsSent(self: TcpStatistics) -> Int64

"""



class UdpStatistics(object):
    """ Provides User Datagram Protocol (UDP) statistical data. """
    DatagramsReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of User Datagram Protocol (UDP) datagrams that were received.

Get: DatagramsReceived(self: UdpStatistics) -> Int64

"""

    DatagramsSent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of User Datagram Protocol (UDP) datagrams that were sent.

Get: DatagramsSent(self: UdpStatistics) -> Int64

"""

    IncomingDatagramsDiscarded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of User Datagram Protocol (UDP) datagrams that were received and discarded because of port errors.

Get: IncomingDatagramsDiscarded(self: UdpStatistics) -> Int64

"""

    IncomingDatagramsWithErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of User Datagram Protocol (UDP) datagrams that were received and discarded because of errors other than bad port information.

Get: IncomingDatagramsWithErrors(self: UdpStatistics) -> Int64

"""

    UdpListeners = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of local endpoints that are listening for User Datagram Protocol (UDP) datagrams.

Get: UdpListeners(self: UdpStatistics) -> int

"""



class UnicastIPAddressInformation(IPAddressInformation):
    """ Provides information about a network interface's unicast address. """
    AddressPreferredLifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of seconds remaining during which this address is the preferred address.

Get: AddressPreferredLifetime(self: UnicastIPAddressInformation) -> Int64

"""

    AddressValidLifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of seconds remaining during which this address is valid.

Get: AddressValidLifetime(self: UnicastIPAddressInformation) -> Int64

"""

    DhcpLeaseLifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the amount of time remaining on the Dynamic Host Configuration Protocol (DHCP) lease for this IP address.

Get: DhcpLeaseLifetime(self: UnicastIPAddressInformation) -> Int64

"""

    DuplicateAddressDetectionState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the state of the duplicate address detection algorithm.

Get: DuplicateAddressDetectionState(self: UnicastIPAddressInformation) -> DuplicateAddressDetectionState

"""

    IPv4Mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the IPv4 mask.

Get: IPv4Mask(self: UnicastIPAddressInformation) -> IPAddress

"""

    PrefixLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrefixLength(self: UnicastIPAddressInformation) -> int

"""

    PrefixOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the source of a unicast Internet Protocol (IP) address prefix.

Get: PrefixOrigin(self: UnicastIPAddressInformation) -> PrefixOrigin

"""

    SuffixOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the source of a unicast Internet Protocol (IP) address suffix.

Get: SuffixOrigin(self: UnicastIPAddressInformation) -> SuffixOrigin

"""



class UnicastIPAddressInformationCollection(object, ICollection[UnicastIPAddressInformation], IEnumerable[UnicastIPAddressInformation], IEnumerable):
    """ Stores a set of System.Net.NetworkInformation.UnicastIPAddressInformation types. """
    def Add(self, address):
        """
        Add(self: UnicastIPAddressInformationCollection, address: UnicastIPAddressInformation)
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        
        
            address: The object to be added to the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: UnicastIPAddressInformationCollection)
            Throws a System.NotSupportedException because this operation is not supported for this 
             collection.
        """
        pass

    def Contains(self, address):
        """
        Contains(self: UnicastIPAddressInformationCollection, address: UnicastIPAddressInformation) -> bool
        
            Checks whether the collection contains the specified 
             System.Net.NetworkInformation.UnicastIPAddressInformation object.
        
        
            address: The System.Net.NetworkInformation.UnicastIPAddressInformation object to be searched in the 
             collection.
        
            Returns: true if the System.Net.NetworkInformation.UnicastIPAddressInformation object exists in the 
             collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, offset):
        """
        CopyTo(self: UnicastIPAddressInformationCollection, array: Array[UnicastIPAddressInformation], offset: int)
            Copies the elements in this collection to a one-dimensional array of type 
             System.Net.NetworkInformation.UnicastIPAddressInformation.
        
        
            array: A one-dimensional array that receives a copy of the collection.
            offset: The zero-based index in array at which the copy begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: UnicastIPAddressInformationCollection) -> IEnumerator[UnicastIPAddressInformation]
        
            Returns an object that can be used to iterate through this collection.
            Returns: An object that implements the System.Collections.IEnumerator interface and provides access to 
             the System.Net.NetworkInformation.UnicastIPAddressInformation types in this collection.
        """
        pass

    def Remove(self, address):
        """
        Remove(self: UnicastIPAddressInformationCollection, address: UnicastIPAddressInformation) -> bool
        
            Throws a System.NotSupportedException because the collection is read-only and elements cannot be 
             removed.
        
        
            address: The object to be removed.
            Returns: Always throws a System.NotSupportedException.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[UnicastIPAddressInformation], item: UnicastIPAddressInformation) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Net.NetworkInformation.UnicastIPAddressInformation types in this collection.

Get: Count(self: UnicastIPAddressInformationCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to this collection is read-only.

Get: IsReadOnly(self: UnicastIPAddressInformationCollection) -> bool

"""



