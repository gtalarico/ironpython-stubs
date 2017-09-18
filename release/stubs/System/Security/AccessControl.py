# encoding: utf-8
# module System.Security.AccessControl calls itself AccessControl
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# functions

def AccessRule(*args, **kwargs): # real signature unknown
    """ Represents a combination of a user's identity, an access mask, and an access control type (allow or deny). An System.Security.AccessControl.AccessRule object also contains information about the how the rule is inherited by child objects and how that inheritance is propagated. """
    pass

def AuditRule(*args, **kwargs): # real signature unknown
    """ Represents a combination of a user's identity and an access mask. An System.Security.AccessControl.AuditRule object also contains information about how the rule is inherited by child objects, how that inheritance is propagated, and for what conditions it is audited. """
    pass

def ObjectSecurity(*args, **kwargs): # real signature unknown
    """ Provides the ability to control access to objects without direct manipulation of Access Control Lists (ACLs). This class is the abstract base class for the System.Security.AccessControl.CommonObjectSecurity and System.Security.AccessControl.DirectoryObjectSecurity classes. """
    pass

# classes

class AccessControlActions(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the actions that are permitted for securable objects.
    
    enum (flags) AccessControlActions, values: Change (2), None (0), View (1)
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

    Change = None
    None = None
    value__ = None
    View = None


class AccessControlModification(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of access control modification to perform. This enumeration is used by methods of the System.Security.AccessControl.ObjectSecurity class and its descendents.
    
    enum AccessControlModification, values: Add (0), Remove (3), RemoveAll (4), RemoveSpecific (5), Reset (2), Set (1)
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

    Add = None
    Remove = None
    RemoveAll = None
    RemoveSpecific = None
    Reset = None
    Set = None
    value__ = None


class AccessControlSections(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies which sections of a security descriptor to save or load.
    
    enum (flags) AccessControlSections, values: Access (2), All (15), Audit (1), Group (8), None (0), Owner (4)
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

    Access = None
    All = None
    Audit = None
    Group = None
    None = None
    Owner = None
    value__ = None


class AccessControlType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies whether an System.Security.AccessControl.AccessRule object is used to allow or deny access. These values are not flags, and they cannot be combined.
    
    enum AccessControlType, values: Allow (0), Deny (1)
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

    Allow = None
    Deny = None
    value__ = None


class AceEnumerator(object, IEnumerator):
    """ Provides the ability to iterate through the access control entries (ACEs) in an access control list (ACL). """
    def MoveNext(self):
        """
        MoveNext(self: AceEnumerator) -> bool
        
            Advances the enumerator to the next element of the System.Security.AccessControl.GenericAce 
             collection.
        
            Returns: true if the enumerator was successfully advanced to the next element; false if the enumerator 
             has passed the end of the collection.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """
        Reset(self: AceEnumerator)
            Sets the enumerator to its initial position, which is before the first element in the 
             System.Security.AccessControl.GenericAce collection.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current element in the System.Security.AccessControl.GenericAce collection. This property gets the type-friendly version of the object.

Get: Current(self: AceEnumerator) -> GenericAce

"""



class AceFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the inheritance and auditing behavior of an access control entry (ACE).
    
    enum (flags) AceFlags, values: AuditFlags (192), ContainerInherit (2), FailedAccess (128), InheritanceFlags (15), Inherited (16), InheritOnly (8), None (0), NoPropagateInherit (4), ObjectInherit (1), SuccessfulAccess (64)
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

    AuditFlags = None
    ContainerInherit = None
    FailedAccess = None
    InheritanceFlags = None
    Inherited = None
    InheritOnly = None
    None = None
    NoPropagateInherit = None
    ObjectInherit = None
    SuccessfulAccess = None
    value__ = None


class AceQualifier(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the function of an access control entry (ACE).
    
    enum AceQualifier, values: AccessAllowed (0), AccessDenied (1), SystemAlarm (3), SystemAudit (2)
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

    AccessAllowed = None
    AccessDenied = None
    SystemAlarm = None
    SystemAudit = None
    value__ = None


class AceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the available access control entry (ACE) types.
    
    enum AceType, values: AccessAllowed (0), AccessAllowedCallback (9), AccessAllowedCallbackObject (11), AccessAllowedCompound (4), AccessAllowedObject (5), AccessDenied (1), AccessDeniedCallback (10), AccessDeniedCallbackObject (12), AccessDeniedObject (6), MaxDefinedAceType (16), SystemAlarm (3), SystemAlarmCallback (14), SystemAlarmCallbackObject (16), SystemAlarmObject (8), SystemAudit (2), SystemAuditCallback (13), SystemAuditCallbackObject (15), SystemAuditObject (7)
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

    AccessAllowed = None
    AccessAllowedCallback = None
    AccessAllowedCallbackObject = None
    AccessAllowedCompound = None
    AccessAllowedObject = None
    AccessDenied = None
    AccessDeniedCallback = None
    AccessDeniedCallbackObject = None
    AccessDeniedObject = None
    MaxDefinedAceType = None
    SystemAlarm = None
    SystemAlarmCallback = None
    SystemAlarmCallbackObject = None
    SystemAlarmObject = None
    SystemAudit = None
    SystemAuditCallback = None
    SystemAuditCallbackObject = None
    SystemAuditObject = None
    value__ = None


class AuditFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the conditions for auditing attempts to access a securable object.
    
    enum (flags) AuditFlags, values: Failure (2), None (0), Success (1)
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

    Failure = None
    None = None
    Success = None
    value__ = None


class AuthorizationRule(object):
    """ Determines access to securable objects. The derived classes System.Security.AccessControl.AccessRule and System.Security.AccessControl.AuditRule offer specializations for access and audit functionality. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, identity: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    IdentityReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Security.Principal.IdentityReference to which this rule applies.

Get: IdentityReference(self: AuthorizationRule) -> IdentityReference

"""

    InheritanceFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of flags that determine how this rule is inherited by child objects.

Get: InheritanceFlags(self: AuthorizationRule) -> InheritanceFlags

"""

    IsInherited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this rule is explicitly set or is inherited from a parent container object.

Get: IsInherited(self: AuthorizationRule) -> bool

"""

    PropagationFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the propagation flags, which determine how inheritance of this rule is propagated to child objects. This property is significant only when the value of the System.Security.AccessControl.InheritanceFlags enumeration is not System.Security.AccessControl.InheritanceFlags.None.

Get: PropagationFlags(self: AuthorizationRule) -> PropagationFlags

"""



class AuthorizationRuleCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """
    Represents a collection of System.Security.AccessControl.AuthorizationRule objects.
    
    AuthorizationRuleCollection()
    """
    def AddRule(self, rule):
        """ AddRule(self: AuthorizationRuleCollection, rule: AuthorizationRule) """
        pass

    def CopyTo(self, rules, index):
        """
        CopyTo(self: AuthorizationRuleCollection, rules: Array[AuthorizationRule], index: int)
            Copies the contents of the collection to an array.
        
            rules: An array to which to copy the contents of the collection.
            index: The zero-based index from which to begin copying.
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

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.

"""



class GenericAce(object):
    """ Represents an Access Control Entry (ACE), and is the base class for all other ACE classes. """
    def Copy(self):
        """
        Copy(self: GenericAce) -> GenericAce
        
            Creates a deep copy of this Access Control Entry (ACE).
            Returns: The System.Security.AccessControl.GenericAce object that this method creates.
        """
        pass

    @staticmethod
    def CreateFromBinaryForm(binaryForm, offset):
        """
        CreateFromBinaryForm(binaryForm: Array[Byte], offset: int) -> GenericAce
        
            Creates a System.Security.AccessControl.GenericAce object from the specified binary data.
        
            binaryForm: The binary data from which to create the new System.Security.AccessControl.GenericAce object.
            offset: The offset at which to begin unmarshaling.
            Returns: The System.Security.AccessControl.GenericAce object this method creates.
        """
        pass

    def Equals(self, o):
        """
        Equals(self: GenericAce, o: object) -> bool
        
            Determines whether the specified System.Security.AccessControl.GenericAce object is equal to the 
             current System.Security.AccessControl.GenericAce object.
        
        
            o: The System.Security.AccessControl.GenericAce object to compare to the current 
             System.Security.AccessControl.GenericAce object.
        
            Returns: true if the specified System.Security.AccessControl.GenericAce object is equal to the current 
             System.Security.AccessControl.GenericAce object; otherwise, false.
        """
        pass

    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: GenericAce, binaryForm: Array[Byte], offset: int)
            Marshals the contents of the System.Security.AccessControl.GenericAce object into the specified 
             byte array beginning at the specified offset.
        
        
            binaryForm: The byte array into which the contents of the System.Security.AccessControl.GenericAce is 
             marshaled.
        
            offset: The offset at which to start marshaling.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: GenericAce) -> int
        
            Serves as a hash function for the System.Security.AccessControl.GenericAce class. The  
             System.Security.AccessControl.GenericAce.GetHashCode method is suitable for use in hashing 
             algorithms and data structures like a hash table.
        
            Returns: A hash code for the current System.Security.AccessControl.GenericAce object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AceFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Security.AccessControl.AceFlags associated with this System.Security.AccessControl.GenericAce object.

Get: AceFlags(self: GenericAce) -> AceFlags

Set: AceFlags(self: GenericAce) = value
"""

    AceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of this Access Control Entry (ACE).

Get: AceType(self: GenericAce) -> AceType

"""

    AuditFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the audit information associated with this Access Control Entry (ACE).

Get: AuditFlags(self: GenericAce) -> AuditFlags

"""

    BinaryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.GenericAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.GenericAce.GetBinaryForm method.

Get: BinaryLength(self: GenericAce) -> int

"""

    InheritanceFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets flags that specify the inheritance properties of this Access Control Entry (ACE).

Get: InheritanceFlags(self: GenericAce) -> InheritanceFlags

"""

    IsInherited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this Access Control Entry (ACE) is inherited or is set explicitly.

Get: IsInherited(self: GenericAce) -> bool

"""

    PropagationFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets flags that specify the inheritance propagation properties of this Access Control Entry (ACE).

Get: PropagationFlags(self: GenericAce) -> PropagationFlags

"""



class KnownAce(GenericAce):
    """ Encapsulates all Access Control Entry (ACE) types currently defined by Microsoft Corporation. All System.Security.AccessControl.KnownAce objects contain a 32-bit access mask and a System.Security.Principal.SecurityIdentifier object. """
    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the access mask for this System.Security.AccessControl.KnownAce object.

Get: AccessMask(self: KnownAce) -> int

Set: AccessMask(self: KnownAce) = value
"""

    SecurityIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Security.Principal.SecurityIdentifier object associated with this System.Security.AccessControl.KnownAce object.

Get: SecurityIdentifier(self: KnownAce) -> SecurityIdentifier

Set: SecurityIdentifier(self: KnownAce) = value
"""



class QualifiedAce(KnownAce):
    """ Represents an Access Control Entry (ACE) that contains a qualifier. The qualifier, represented by an System.Security.AccessControl.AceQualifier object, specifies whether the ACE allows access, denies access, causes system audits, or causes system alarms. The System.Security.AccessControl.QualifiedAce class is the abstract base class for the System.Security.AccessControl.CommonAce and System.Security.AccessControl.ObjectAce classes. """
    def GetOpaque(self):
        """
        GetOpaque(self: QualifiedAce) -> Array[Byte]
        
            Returns the opaque callback data associated with this System.Security.AccessControl.QualifiedAce 
             object.
        
            Returns: An array of byte values that represents the opaque callback data associated with this 
             System.Security.AccessControl.QualifiedAce object.
        """
        pass

    def SetOpaque(self, opaque):
        """
        SetOpaque(self: QualifiedAce, opaque: Array[Byte])
            Sets the opaque callback data associated with this System.Security.AccessControl.QualifiedAce 
             object.
        
        
            opaque: An array of byte values that represents the opaque callback data for this 
             System.Security.AccessControl.QualifiedAce object.
        """
        pass

    AceQualifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies whether the ACE allows access, denies access, causes system audits, or causes system alarms.

Get: AceQualifier(self: QualifiedAce) -> AceQualifier

"""

    IsCallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether this System.Security.AccessControl.QualifiedAce object contains callback data.

Get: IsCallback(self: QualifiedAce) -> bool

"""

    OpaqueLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the opaque callback data associated with this System.Security.AccessControl.QualifiedAce object. This property is valid only for callback Access Control Entries (ACEs).

Get: OpaqueLength(self: QualifiedAce) -> int

"""



class CommonAce(QualifiedAce):
    """
    Represents an access control entry (ACE).
    
    CommonAce(flags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, isCallback: bool, opaque: Array[Byte])
    """
    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: CommonAce, binaryForm: Array[Byte], offset: int)
            Marshals the contents of the System.Security.AccessControl.CommonAce object into the specified 
             byte array beginning at the specified offset.
        
        
            binaryForm: The byte array into which the contents of the System.Security.AccessControl.CommonAce object is 
             marshaled.
        
            offset: The offset at which to start marshaling.
        """
        pass

    @staticmethod
    def MaxOpaqueLength(isCallback):
        """
        MaxOpaqueLength(isCallback: bool) -> int
        
            Gets the maximum allowed length of an opaque data BLOB for callback access control entries 
             (ACEs).
        
        
            isCallback: true to specify that the System.Security.AccessControl.CommonAce object is a callback ACE type.
            Returns: The allowed length of an opaque data BLOB.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, flags, qualifier, accessMask, sid, isCallback, opaque):
        """ __new__(cls: type, flags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, isCallback: bool, opaque: Array[Byte]) """
        pass

    BinaryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.CommonAce object. Use this length with the System.Security.AccessControl.CommonAce.GetBinaryForm(System.Byte[],System.Int32) method before marshaling the ACL into a binary array.

Get: BinaryLength(self: CommonAce) -> int

"""



class GenericAcl(object, ICollection, IEnumerable):
    """ Represents an access control list (ACL) and is the base class for the System.Security.AccessControl.CommonAcl, System.Security.AccessControl.DiscretionaryAcl, System.Security.AccessControl.RawAcl, and System.Security.AccessControl.SystemAcl classes. """
    def CopyTo(self, array, index):
        """
        CopyTo(self: GenericAcl, array: Array[GenericAce], index: int)
            Copies each System.Security.AccessControl.GenericAce of the current 
             System.Security.AccessControl.GenericAcl into the specified array.
        
        
            array: The array into which copies of the System.Security.AccessControl.GenericAce objects contained by 
             the current System.Security.AccessControl.GenericAcl are placed.
        
            index: The zero-based index of array where the copying begins.
        """
        pass

    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: GenericAcl, binaryForm: Array[Byte], offset: int)
            Marshals the contents of the System.Security.AccessControl.GenericAcl object into the specified 
             byte array beginning at the specified offset.
        
        
            binaryForm: The byte array into which the contents of the System.Security.AccessControl.GenericAcl is 
             marshaled.
        
            offset: The offset at which to start marshaling.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: GenericAcl) -> AceEnumerator
        
            Returns a new instance of the System.Security.AccessControl.AceEnumerator class.
            Returns: The Security.AccessControl.AceEnumerator that this method returns.
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    BinaryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.GenericAcl object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.GenericAcl.GetBinaryForm method.

Get: BinaryLength(self: GenericAcl) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of access control entries (ACEs) in the current System.Security.AccessControl.GenericAcl object.

Get: Count(self: GenericAcl) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is always set to false. It is implemented only because it is required for the implementation of the System.Collections.ICollection interface.

Get: IsSynchronized(self: GenericAcl) -> bool

"""

    Revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the revision level of the System.Security.AccessControl.GenericAcl.

Get: Revision(self: GenericAcl) -> Byte

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property always returns null. It is implemented only because it is required for the implementation of the System.Collections.ICollection interface.

Get: SyncRoot(self: GenericAcl) -> object

"""


    AclRevision = None
    AclRevisionDS = None
    MaxBinaryLength = 65535


class CommonAcl(GenericAcl, ICollection, IEnumerable):
    """ Represents an access control list (ACL) and is the base class for the System.Security.AccessControl.DiscretionaryAcl and System.Security.AccessControl.SystemAcl classes. """
    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: CommonAcl, binaryForm: Array[Byte], offset: int)
            Marshals the contents of the System.Security.AccessControl.CommonAcl object into the specified 
             byte array beginning at the specified offset.
        
        
            binaryForm: The byte array into which the contents of the System.Security.AccessControl.CommonAcl is 
             marshaled.
        
            offset: The offset at which to start marshaling.
        """
        pass

    def Purge(self, sid):
        """
        Purge(self: CommonAcl, sid: SecurityIdentifier)
            Removes all access control entries (ACEs) contained by this 
             System.Security.AccessControl.CommonAcl object that are associated with the specified 
             System.Security.Principal.SecurityIdentifier object.
        
        
            sid: The System.Security.Principal.SecurityIdentifier object to check for.
        """
        pass

    def RemoveInheritedAces(self):
        """
        RemoveInheritedAces(self: CommonAcl)
            Removes all inherited access control entries (ACEs) from this 
             System.Security.AccessControl.CommonAcl object.
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    BinaryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.CommonAcl object. This length should be used before marshaling the access control list (ACL) into a binary array by using the System.Security.AccessControl.CommonAcl.GetBinaryForm method.

Get: BinaryLength(self: CommonAcl) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of access control entries (ACEs) in the current System.Security.AccessControl.CommonAcl object.

Get: Count(self: CommonAcl) -> int

"""

    IsCanonical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether the access control entries (ACEs) in the current System.Security.AccessControl.CommonAcl object are in canonical order.

Get: IsCanonical(self: CommonAcl) -> bool

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets whether the System.Security.AccessControl.CommonAcl object is a container.

Get: IsContainer(self: CommonAcl) -> bool

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets whether the current System.Security.AccessControl.CommonAcl object is a directory object access control list (ACL).

Get: IsDS(self: CommonAcl) -> bool

"""

    Revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the revision level of the System.Security.AccessControl.CommonAcl.

Get: Revision(self: CommonAcl) -> Byte

"""



class CommonObjectSecurity(ObjectSecurity):
    """ Controls access to objects without direct manipulation of access control lists (ACLs). This class is the abstract base class for the System.Security.AccessControl.NativeObjectSecurity class. """
    def AddAccessRule(self, *args): #cannot find CLR method
        """
        AddAccessRule(self: CommonObjectSecurity, rule: AccessRule)
            Adds the specified access rule to the Discretionary Access Control List (DACL) associated with 
             this System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to add.
        """
        pass

    def AddAuditRule(self, *args): #cannot find CLR method
        """
        AddAuditRule(self: CommonObjectSecurity, rule: AuditRule)
            Adds the specified audit rule to the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to add.
        """
        pass

    def GetAccessRules(self, includeExplicit, includeInherited, targetType):
        """
        GetAccessRules(self: CommonObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection
        
            Gets a collection of the access rules associated with the specified security identifier.
        
            includeExplicit: true to include access rules explicitly set for the object.
            includeInherited: true to include inherited access rules.
            targetType: Specifies whether the security identifier for which to retrieve access rules is of type 
             T:System.Security.Principal.SecurityIdentifier or type T:System.Security.Principal.NTAccount. 
             The value of this parameter must be a type that can be translated to  the 
             System.Security.Principal.SecurityIdentifier type.
        
            Returns: The collection of access rules associated with the specified 
             System.Security.Principal.SecurityIdentifier object.
        """
        pass

    def GetAuditRules(self, includeExplicit, includeInherited, targetType):
        """
        GetAuditRules(self: CommonObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection
        
            Gets a collection of the audit rules associated with the specified security identifier.
        
            includeExplicit: true to include audit rules explicitly set for the object.
            includeInherited: true to include inherited audit rules.
            targetType: The security identifier for which to retrieve audit rules. This must be an object that can be 
             cast as a System.Security.Principal.SecurityIdentifier object.
        
            Returns: The collection of audit rules associated with the specified 
             System.Security.Principal.SecurityIdentifier object.
        """
        pass

    def RemoveAccessRule(self, *args): #cannot find CLR method
        """
        RemoveAccessRule(self: CommonObjectSecurity, rule: AccessRule) -> bool
        
            Removes access rules that contain the same security identifier and access mask as the specified 
             access rule from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to remove.
            Returns: true if the access rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAccessRuleAll(self, *args): #cannot find CLR method
        """
        RemoveAccessRuleAll(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules that have the same security identifier as the specified access rule 
             from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAccessRuleSpecific(self, *args): #cannot find CLR method
        """
        RemoveAccessRuleSpecific(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules that exactly match the specified access rule from the Discretionary 
             Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAuditRule(self, *args): #cannot find CLR method
        """
        RemoveAuditRule(self: CommonObjectSecurity, rule: AuditRule) -> bool
        
            Removes audit rules that contain the same security identifier and access mask as the specified 
             audit rule from the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to remove.
            Returns: true if the audit rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAuditRuleAll(self, *args): #cannot find CLR method
        """
        RemoveAuditRuleAll(self: CommonObjectSecurity, rule: AuditRule)
            Removes all audit rules that have the same security identifier as the specified audit rule from 
             the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def RemoveAuditRuleSpecific(self, *args): #cannot find CLR method
        """
        RemoveAuditRuleSpecific(self: CommonObjectSecurity, rule: AuditRule)
            Removes all audit rules that exactly match the specified audit rule from the System Access 
             Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity 
             object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def ResetAccessRule(self, *args): #cannot find CLR method
        """
        ResetAccessRule(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 
             rule.
        
        
            rule: The access rule to reset.
        """
        pass

    def SetAccessRule(self, *args): #cannot find CLR method
        """
        SetAccessRule(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules that contain the same security identifier and qualifier as the 
             specified access rule in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 
             rule.
        
        
            rule: The access rule to set.
        """
        pass

    def SetAuditRule(self, *args): #cannot find CLR method
        """
        SetAuditRule(self: CommonObjectSecurity, rule: AuditRule)
            Removes all audit rules that contain the same security identifier and qualifier as the specified 
             audit rule in the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object and then adds the specified audit 
             rule.
        
        
            rule: The audit rule to set.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, isContainer: bool) """
        pass

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class GenericSecurityDescriptor(object):
    """ Represents a security descriptor. A security descriptor includes an owner, a primary group, a Discretionary Access Control List (DACL), and a System Access Control List (SACL). """
    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: GenericSecurityDescriptor, binaryForm: Array[Byte], offset: int)
            Returns an array of byte values that represents the information contained in this 
             System.Security.AccessControl.GenericSecurityDescriptor object.
        
        
            binaryForm: The byte array into which the contents of the 
             System.Security.AccessControl.GenericSecurityDescriptor is marshaled.
        
            offset: The offset at which to start marshaling.
        """
        pass

    def GetSddlForm(self, includeSections):
        """
        GetSddlForm(self: GenericSecurityDescriptor, includeSections: AccessControlSections) -> str
        
            Returns the Security Descriptor Definition Language (SDDL) representation of the specified 
             sections of the security descriptor that this 
             System.Security.AccessControl.GenericSecurityDescriptor object represents.
        
        
            includeSections: Specifies which sections (access rules, audit rules, primary group, owner) of the security 
             descriptor to get.
        
            Returns: The SDDL representation of the specified sections of the security descriptor associated with 
             this System.Security.AccessControl.GenericSecurityDescriptor object.
        """
        pass

    @staticmethod
    def IsSddlConversionSupported():
        """
        IsSddlConversionSupported() -> bool
        
            Returns a boolean value that specifies whether the security descriptor associated with this  
             System.Security.AccessControl.GenericSecurityDescriptor object can be converted to the Security 
             Descriptor Definition Language (SDDL) format.
        
            Returns: true if the security descriptor associated with this  
             System.Security.AccessControl.GenericSecurityDescriptor object can be converted to the Security 
             Descriptor Definition Language (SDDL) format; otherwise, false.
        """
        pass

    BinaryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.GenericSecurityDescriptor object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.GenericSecurityDescriptor.GetBinaryForm method.

Get: BinaryLength(self: GenericSecurityDescriptor) -> int

"""

    ControlFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets values that specify behavior of the System.Security.AccessControl.GenericSecurityDescriptor object.

Get: ControlFlags(self: GenericSecurityDescriptor) -> ControlFlags

"""

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the primary group for this System.Security.AccessControl.GenericSecurityDescriptor object.

Get: Group(self: GenericSecurityDescriptor) -> SecurityIdentifier

Set: Group(self: GenericSecurityDescriptor) = value
"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the owner of the object associated with this System.Security.AccessControl.GenericSecurityDescriptor object.

Get: Owner(self: GenericSecurityDescriptor) -> SecurityIdentifier

Set: Owner(self: GenericSecurityDescriptor) = value
"""


    Revision = None


class CommonSecurityDescriptor(GenericSecurityDescriptor):
    """
    Represents a security descriptor. A security descriptor includes an owner, a primary group, a Discretionary Access Control List (DACL), and a System Access Control List (SACL).
    
    CommonSecurityDescriptor(isContainer: bool, isDS: bool, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: SystemAcl, discretionaryAcl: DiscretionaryAcl)
    CommonSecurityDescriptor(isContainer: bool, isDS: bool, rawSecurityDescriptor: RawSecurityDescriptor)
    CommonSecurityDescriptor(isContainer: bool, isDS: bool, sddlForm: str)
    CommonSecurityDescriptor(isContainer: bool, isDS: bool, binaryForm: Array[Byte], offset: int)
    """
    def AddDiscretionaryAcl(self, revision, trusted):
        """ AddDiscretionaryAcl(self: CommonSecurityDescriptor, revision: Byte, trusted: int) """
        pass

    def AddSystemAcl(self, revision, trusted):
        """ AddSystemAcl(self: CommonSecurityDescriptor, revision: Byte, trusted: int) """
        pass

    def PurgeAccessControl(self, sid):
        """
        PurgeAccessControl(self: CommonSecurityDescriptor, sid: SecurityIdentifier)
            Removes all access rules for the specified security identifier from the Discretionary Access 
             Control List (DACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor 
             object.
        
        
            sid: The security identifier for which to remove access rules.
        """
        pass

    def PurgeAudit(self, sid):
        """
        PurgeAudit(self: CommonSecurityDescriptor, sid: SecurityIdentifier)
            Removes all audit rules for the specified security identifier from the System Access Control 
             List (SACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object.
        
        
            sid: The security identifier for which to remove audit rules.
        """
        pass

    def SetDiscretionaryAclProtection(self, isProtected, preserveInheritance):
        """
        SetDiscretionaryAclProtection(self: CommonSecurityDescriptor, isProtected: bool, preserveInheritance: bool)
            Sets the inheritance protection for the Discretionary Access Control List (DACL) associated with 
             this System.Security.AccessControl.CommonSecurityDescriptor object. DACLs that are protected do 
             not inherit access rules from parent containers.
        
        
            isProtected: true to protect the DACL from inheritance.
            preserveInheritance: true to keep inherited access rules in the DACL; false to remove inherited access rules from the 
             DACL.
        """
        pass

    def SetSystemAclProtection(self, isProtected, preserveInheritance):
        """
        SetSystemAclProtection(self: CommonSecurityDescriptor, isProtected: bool, preserveInheritance: bool)
            Sets the inheritance protection for the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonSecurityDescriptor object. SACLs that are protected do not 
             inherit audit rules from parent containers.
        
        
            isProtected: true to protect the SACL from inheritance.
            preserveInheritance: true to keep inherited audit rules in the SACL; false to remove inherited audit rules from the 
             SACL.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, isContainer, isDS, *__args):
        """
        __new__(cls: type, isContainer: bool, isDS: bool, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: SystemAcl, discretionaryAcl: DiscretionaryAcl)
        __new__(cls: type, isContainer: bool, isDS: bool, rawSecurityDescriptor: RawSecurityDescriptor)
        __new__(cls: type, isContainer: bool, isDS: bool, sddlForm: str)
        __new__(cls: type, isContainer: bool, isDS: bool, binaryForm: Array[Byte], offset: int)
        """
        pass

    ControlFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets values that specify behavior of the System.Security.AccessControl.CommonSecurityDescriptor object.

Get: ControlFlags(self: CommonSecurityDescriptor) -> ControlFlags

"""

    DiscretionaryAcl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the discretionary access control list (DACL) for this System.Security.AccessControl.CommonSecurityDescriptor object. The DACL contains access rules.

Get: DiscretionaryAcl(self: CommonSecurityDescriptor) -> DiscretionaryAcl

Set: DiscretionaryAcl(self: CommonSecurityDescriptor) = value
"""

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the primary group for this System.Security.AccessControl.CommonSecurityDescriptor object.

Get: Group(self: CommonSecurityDescriptor) -> SecurityIdentifier

Set: Group(self: CommonSecurityDescriptor) = value
"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether the object associated with this System.Security.AccessControl.CommonSecurityDescriptor object is a container object.

Get: IsContainer(self: CommonSecurityDescriptor) -> bool

"""

    IsDiscretionaryAclCanonical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object is in canonical order.

Get: IsDiscretionaryAclCanonical(self: CommonSecurityDescriptor) -> bool

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether the object associated with this System.Security.AccessControl.CommonSecurityDescriptor object is a directory object.

Get: IsDS(self: CommonSecurityDescriptor) -> bool

"""

    IsSystemAclCanonical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object is in canonical order.

Get: IsSystemAclCanonical(self: CommonSecurityDescriptor) -> bool

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the owner of the object associated with this System.Security.AccessControl.CommonSecurityDescriptor object.

Get: Owner(self: CommonSecurityDescriptor) -> SecurityIdentifier

Set: Owner(self: CommonSecurityDescriptor) = value
"""

    SystemAcl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System Access Control List (SACL) for this System.Security.AccessControl.CommonSecurityDescriptor object. The SACL contains audit rules.

Get: SystemAcl(self: CommonSecurityDescriptor) -> SystemAcl

Set: SystemAcl(self: CommonSecurityDescriptor) = value
"""



class CompoundAce(KnownAce):
    """
    Represents a compound Access Control Entry (ACE).
    
    CompoundAce(flags: AceFlags, accessMask: int, compoundAceType: CompoundAceType, sid: SecurityIdentifier)
    """
    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: CompoundAce, binaryForm: Array[Byte], offset: int)
            Marshals the contents of the System.Security.AccessControl.CompoundAce object into the specified 
             byte array beginning at the specified offset.
        
        
            binaryForm: The byte array into which the contents of the System.Security.AccessControl.CompoundAce is 
             marshaled.
        
            offset: The offset at which to start marshaling.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, flags, accessMask, compoundAceType, sid):
        """ __new__(cls: type, flags: AceFlags, accessMask: int, compoundAceType: CompoundAceType, sid: SecurityIdentifier) """
        pass

    BinaryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.CompoundAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.CompoundAce.GetBinaryForm method.

Get: BinaryLength(self: CompoundAce) -> int

"""

    CompoundAceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of this System.Security.AccessControl.CompoundAce object.

Get: CompoundAceType(self: CompoundAce) -> CompoundAceType

Set: CompoundAceType(self: CompoundAce) = value
"""



class CompoundAceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of a System.Security.AccessControl.CompoundAce object.
    
    enum CompoundAceType, values: Impersonation (1)
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

    Impersonation = None
    value__ = None


class ControlFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    These flags affect the security descriptor behavior.
    
    enum (flags) ControlFlags, values: DiscretionaryAclAutoInherited (1024), DiscretionaryAclAutoInheritRequired (256), DiscretionaryAclDefaulted (8), DiscretionaryAclPresent (4), DiscretionaryAclProtected (4096), DiscretionaryAclUntrusted (64), GroupDefaulted (2), None (0), OwnerDefaulted (1), RMControlValid (16384), SelfRelative (32768), ServerSecurity (128), SystemAclAutoInherited (2048), SystemAclAutoInheritRequired (512), SystemAclDefaulted (32), SystemAclPresent (16), SystemAclProtected (8192)
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

    DiscretionaryAclAutoInherited = None
    DiscretionaryAclAutoInheritRequired = None
    DiscretionaryAclDefaulted = None
    DiscretionaryAclPresent = None
    DiscretionaryAclProtected = None
    DiscretionaryAclUntrusted = None
    GroupDefaulted = None
    None = None
    OwnerDefaulted = None
    RMControlValid = None
    SelfRelative = None
    ServerSecurity = None
    SystemAclAutoInherited = None
    SystemAclAutoInheritRequired = None
    SystemAclDefaulted = None
    SystemAclPresent = None
    SystemAclProtected = None
    value__ = None


class CryptoKeyAccessRule(AccessRule):
    """
    Represents an access rule for a cryptographic key. An access rule represents a combination of a user's identity, an access mask, and an access control type (allow or deny). An access rule object also contains information about the how the rule is inherited by child objects and how that inheritance is propagated.
    
    CryptoKeyAccessRule(identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, type: AccessControlType)
    CryptoKeyAccessRule(identity: str, cryptoKeyRights: CryptoKeyRights, type: AccessControlType)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, cryptoKeyRights, type):
        """
        __new__(cls: type, identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, type: AccessControlType)
        __new__(cls: type, identity: str, cryptoKeyRights: CryptoKeyRights, type: AccessControlType)
        """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    CryptoKeyRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the cryptographic key operation to which this access rule controls access.

Get: CryptoKeyRights(self: CryptoKeyAccessRule) -> CryptoKeyRights

"""



class CryptoKeyAuditRule(AuditRule):
    """
    Represents an audit rule for a cryptographic key. An audit rule represents a combination of a user's identity and an access mask. An audit rule also contains information about the how the rule is inherited by child objects, how that inheritance is propagated, and for what conditions it is audited.
    
    CryptoKeyAuditRule(identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags)
    CryptoKeyAuditRule(identity: str, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, cryptoKeyRights, flags):
        """
        __new__(cls: type, identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags)
        __new__(cls: type, identity: str, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags)
        """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    CryptoKeyRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the cryptographic key operation for which this audit rule generates audits.

Get: CryptoKeyRights(self: CryptoKeyAuditRule) -> CryptoKeyRights

"""



class CryptoKeyRights(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the cryptographic key operation for which an authorization rule controls access or auditing.
    
    enum (flags) CryptoKeyRights, values: ChangePermissions (262144), Delete (65536), FullControl (2032027), GenericAll (268435456), GenericExecute (536870912), GenericRead (-2147483648), GenericWrite (1073741824), ReadAttributes (128), ReadData (1), ReadExtendedAttributes (8), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288), WriteAttributes (256), WriteData (2), WriteExtendedAttributes (16)
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

    ChangePermissions = None
    Delete = None
    FullControl = None
    GenericAll = None
    GenericExecute = None
    GenericRead = None
    GenericWrite = None
    ReadAttributes = None
    ReadData = None
    ReadExtendedAttributes = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None
    WriteAttributes = None
    WriteData = None
    WriteExtendedAttributes = None


class NativeObjectSecurity(CommonObjectSecurity):
    """ Provides the ability to control access to native objects without direct manipulation of Access Control Lists (ACLs). Native object types are defined by the System.Security.AccessControl.ResourceType enumeration. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, isContainer: bool, resourceType: ResourceType)
        __new__(cls: type, isContainer: bool, resourceType: ResourceType, exceptionFromErrorCode: ExceptionFromErrorCode, exceptionContext: object)
        __new__(cls: type, isContainer: bool, resourceType: ResourceType, name: str, includeSections: AccessControlSections, exceptionFromErrorCode: ExceptionFromErrorCode, exceptionContext: object)
        __new__(cls: type, isContainer: bool, resourceType: ResourceType, name: str, includeSections: AccessControlSections)
        __new__(cls: type, isContainer: bool, resourceType: ResourceType, handle: SafeHandle, includeSections: AccessControlSections, exceptionFromErrorCode: ExceptionFromErrorCode, exceptionContext: object)
        __new__(cls: type, isContainer: bool, resourceType: ResourceType, handle: SafeHandle, includeSections: AccessControlSections)
        """
        pass

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""


    ExceptionFromErrorCode = None


class CryptoKeySecurity(NativeObjectSecurity):
    """
    Provides the ability to control access to a cryptographic key object without direct manipulation of  an Access Control List (ACL).
    
    CryptoKeySecurity()
    CryptoKeySecurity(securityDescriptor: CommonSecurityDescriptor)
    """
    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: CryptoKeySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule
        
            Initializes a new instance of the System.Security.AccessControl.AccessRule class with the 
             specified values.
        
        
            identityReference: The identity to which the access rule applies.  It must be an object that can be cast as a 
             System.Security.Principal.SecurityIdentifier.
        
            accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits, the 
             meaning of which is defined by the individual integrators.
        
            isInherited: true if this rule is inherited from a parent container.
            inheritanceFlags: Specifies the inheritance properties of the access rule.
            propagationFlags: Specifies whether inherited access rules are automatically propagated. The propagation flags are 
             ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.
        
            type: Specifies the valid access control type.
            Returns: The System.Security.AccessControl.AccessRule object that this method creates.
        """
        pass

    def AddAccessRule(self, rule):
        """
        AddAccessRule(self: CryptoKeySecurity, rule: CryptoKeyAccessRule)
            Adds the specified access rule to the Discretionary Access Control List (DACL) associated with 
             this System.Security.AccessControl.CryptoKeySecurity object.
        
        
            rule: The access rule to add.
        """
        pass

    def AddAuditRule(self, rule):
        """
        AddAuditRule(self: CryptoKeySecurity, rule: CryptoKeyAuditRule)
            Adds the specified audit rule to the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CryptoKeySecurity object.
        
        
            rule: The audit rule to add.
        """
        pass

    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: CryptoKeySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule
        
            Initializes a new instance of the System.Security.AccessControl.AuditRule class with the 
             specified values.
        
        
            identityReference: The identity to which the audit rule applies.  It must be an object that can be cast as a 
             System.Security.Principal.SecurityIdentifier.
        
            accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits, the 
             meaning of which is defined by the individual integrators.
        
            isInherited: true if this rule is inherited from a parent container.
            inheritanceFlags: Specifies the inheritance properties of the audit rule.
            propagationFlags: Specifies whether inherited audit rules are automatically propagated. The propagation flags are 
             ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.
        
            flags: Specifies the conditions for which the rule is audited.
            Returns: The System.Security.AccessControl.AuditRule object that this method creates.
        """
        pass

    def RemoveAccessRule(self, rule):
        """
        RemoveAccessRule(self: CryptoKeySecurity, rule: CryptoKeyAccessRule) -> bool
        
            Removes access rules that contain the same security identifier and access mask as the specified 
             access rule from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CryptoKeySecurity object.
        
        
            rule: The access rule to remove.
            Returns: true if the access rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAccessRuleAll(self, rule):
        """
        RemoveAccessRuleAll(self: CryptoKeySecurity, rule: CryptoKeyAccessRule)
            Removes all access rules that have the same security identifier as the specified access rule 
             from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CryptoKeySecurity object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAccessRuleSpecific(self, rule):
        """
        RemoveAccessRuleSpecific(self: CryptoKeySecurity, rule: CryptoKeyAccessRule)
            Removes all access rules that exactly match the specified access rule from the Discretionary 
             Access Control List (DACL) associated with this System.Security.AccessControl.CryptoKeySecurity 
             object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAuditRule(self, rule):
        """
        RemoveAuditRule(self: CryptoKeySecurity, rule: CryptoKeyAuditRule) -> bool
        
            Removes audit rules that contain the same security identifier and access mask as the specified 
             audit rule from the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CryptoKeySecurity object.
        
        
            rule: The audit rule to remove.
            Returns: true if the audit rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAuditRuleAll(self, rule):
        """
        RemoveAuditRuleAll(self: CryptoKeySecurity, rule: CryptoKeyAuditRule)
            Removes all audit rules that have the same security identifier as the specified audit rule from 
             the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CryptoKeySecurity object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def RemoveAuditRuleSpecific(self, rule):
        """
        RemoveAuditRuleSpecific(self: CryptoKeySecurity, rule: CryptoKeyAuditRule)
            Removes all audit rules that exactly match the specified audit rule from the System Access 
             Control List (SACL) associated with this System.Security.AccessControl.CryptoKeySecurity object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def ResetAccessRule(self, rule):
        """
        ResetAccessRule(self: CryptoKeySecurity, rule: CryptoKeyAccessRule)
            Removes all access rules in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CryptoKeySecurity object and then adds the specified access rule.
        
        
            rule: The access rule to reset.
        """
        pass

    def SetAccessRule(self, rule):
        """
        SetAccessRule(self: CryptoKeySecurity, rule: CryptoKeyAccessRule)
            Removes all access rules that contain the same security identifier and qualifier as the 
             specified access rule in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CryptoKeySecurity object and then adds the specified access rule.
        
        
            rule: The access rule to set.
        """
        pass

    def SetAuditRule(self, rule):
        """
        SetAuditRule(self: CryptoKeySecurity, rule: CryptoKeyAuditRule)
            Removes all audit rules that contain the same security identifier and qualifier as the specified 
             audit rule in the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CryptoKeySecurity object and then adds the specified audit rule.
        
        
            rule: The audit rule to set.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, securityDescriptor=None):
        """
        __new__(cls: type)
        __new__(cls: type, securityDescriptor: CommonSecurityDescriptor)
        """
        pass

    AccessRightType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Type of the securable object associated with this System.Security.AccessControl.CryptoKeySecurity object.

Get: AccessRightType(self: CryptoKeySecurity) -> Type

"""

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AccessRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Type of the object associated with the access rules of this System.Security.AccessControl.CryptoKeySecurity object. The System.Type object must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.

Get: AccessRuleType(self: CryptoKeySecurity) -> Type

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Type object associated with the audit rules of this System.Security.AccessControl.CryptoKeySecurity object. The System.Type object must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.

Get: AuditRuleType(self: CryptoKeySecurity) -> Type

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class CustomAce(GenericAce):
    """
    Represents an Access Control Entry (ACE) that is not defined by one of the members of the System.Security.AccessControl.AceType enumeration.
    
    CustomAce(type: AceType, flags: AceFlags, opaque: Array[Byte])
    """
    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: CustomAce, binaryForm: Array[Byte], offset: int)
            Marshals the contents of the System.Security.AccessControl.CustomAce object into the specified 
             byte array beginning at the specified offset.
        
        
            binaryForm: The byte array into which the contents of the System.Security.AccessControl.CustomAce is 
             marshaled.
        
            offset: The offset at which to start marshaling.
        """
        pass

    def GetOpaque(self):
        """
        GetOpaque(self: CustomAce) -> Array[Byte]
        
            Returns the opaque data associated with this System.Security.AccessControl.CustomAce object.
            Returns: An array of byte values that represents the opaque data associated with this 
             System.Security.AccessControl.CustomAce object.
        """
        pass

    def SetOpaque(self, opaque):
        """
        SetOpaque(self: CustomAce, opaque: Array[Byte])
            Sets the opaque callback data associated with this System.Security.AccessControl.CustomAce 
             object.
        
        
            opaque: An array of byte values that represents the opaque callback data for this 
             System.Security.AccessControl.CustomAce object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type, flags, opaque):
        """ __new__(cls: type, type: AceType, flags: AceFlags, opaque: Array[Byte]) """
        pass

    BinaryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.CustomAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.CustomAce.GetBinaryForm method.

Get: BinaryLength(self: CustomAce) -> int

"""

    OpaqueLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the opaque data associated with this System.Security.AccessControl.CustomAce object.

Get: OpaqueLength(self: CustomAce) -> int

"""


    MaxOpaqueLength = 65531


class DirectoryObjectSecurity(ObjectSecurity):
    """ Provides the ability to control access to directory objects without direct manipulation of Access Control Lists (ACLs). """
    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type, objectType=None, inheritedObjectType=None):
        """
        AccessRuleFactory(self: DirectoryObjectSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType, objectType: Guid, inheritedObjectType: Guid) -> AccessRule
        
            Initializes a new instance of the System.Security.AccessControl.AccessRule class with the 
             specified values.
        
        
            identityReference: The identity to which the access rule applies.  It must be an object that can be cast as a 
             System.Security.Principal.SecurityIdentifier.
        
            accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits, the 
             meaning of which is defined by the individual integrators.
        
            isInherited: true if this rule is inherited from a parent container.
            inheritanceFlags: Specifies the inheritance properties of the access rule.
            propagationFlags: Specifies whether inherited access rules are automatically propagated. The propagation flags are 
             ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.
        
            type: Specifies the valid access control type.
            objectType: The identity of the class of objects to which the new access rule applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the new access rule.
            Returns: The System.Security.AccessControl.AccessRule object that this method creates.
        """
        pass

    def AddAccessRule(self, *args): #cannot find CLR method
        """
        AddAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule)
            Adds the specified access rule to the Discretionary Access Control List (DACL) associated with 
             this System.Security.AccessControl.DirectoryObjectSecurity object.
        
        
            rule: The access rule to add.
        """
        pass

    def AddAuditRule(self, *args): #cannot find CLR method
        """
        AddAuditRule(self: DirectoryObjectSecurity, rule: ObjectAuditRule)
            Adds the specified audit rule to the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.DirectoryObjectSecurity object.
        
        
            rule: The audit rule to add.
        """
        pass

    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags, objectType=None, inheritedObjectType=None):
        """
        AuditRuleFactory(self: DirectoryObjectSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags, objectType: Guid, inheritedObjectType: Guid) -> AuditRule
        
            Initializes a new instance of the System.Security.AccessControl.AuditRule class with the 
             specified values.
        
        
            identityReference: The identity to which the audit rule applies.  It must be an object that can be cast as a 
             System.Security.Principal.SecurityIdentifier.
        
            accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits, the 
             meaning of which is defined by the individual integrators.
        
            isInherited: true if this rule is inherited from a parent container.
            inheritanceFlags: Specifies the inheritance properties of the audit rule.
            propagationFlags: Specifies whether inherited audit rules are automatically propagated. The propagation flags are 
             ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.
        
            flags: Specifies the conditions for which the rule is audited.
            objectType: The identity of the class of objects to which the new audit rule applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the new audit rule.
            Returns: The System.Security.AccessControl.AuditRule object that this method creates.
        """
        pass

    def GetAccessRules(self, includeExplicit, includeInherited, targetType):
        """
        GetAccessRules(self: DirectoryObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection
        
            Gets a collection of the access rules associated with the specified security identifier.
        
            includeExplicit: true to include access rules explicitly set for the object.
            includeInherited: true to include inherited access rules.
            targetType: The security identifier for which to retrieve access rules. This must be an object that can be 
             cast as a System.Security.Principal.SecurityIdentifier object.
        
            Returns: The collection of access rules associated with the specified 
             System.Security.Principal.SecurityIdentifier object.
        """
        pass

    def GetAuditRules(self, includeExplicit, includeInherited, targetType):
        """
        GetAuditRules(self: DirectoryObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection
        
            Gets a collection of the audit rules associated with the specified security identifier.
        
            includeExplicit: true to include audit rules explicitly set for the object.
            includeInherited: true to include inherited audit rules.
            targetType: The security identifier for which to retrieve audit rules. This must be an object that can be 
             cast as a System.Security.Principal.SecurityIdentifier object.
        
            Returns: The collection of audit rules associated with the specified 
             System.Security.Principal.SecurityIdentifier object.
        """
        pass

    def RemoveAccessRule(self, *args): #cannot find CLR method
        """
        RemoveAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule) -> bool
        
            Removes access rules that contain the same security identifier and access mask as the specified 
             access rule from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.DirectoryObjectSecurity object.
        
        
            rule: The access rule to remove.
            Returns: true if the access rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAccessRuleAll(self, *args): #cannot find CLR method
        """
        RemoveAccessRuleAll(self: DirectoryObjectSecurity, rule: ObjectAccessRule)
            Removes all access rules that have the same security identifier as the specified access rule 
             from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.DirectoryObjectSecurity object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAccessRuleSpecific(self, *args): #cannot find CLR method
        """
        RemoveAccessRuleSpecific(self: DirectoryObjectSecurity, rule: ObjectAccessRule)
            Removes all access rules that exactly match the specified access rule from the Discretionary 
             Access Control List (DACL) associated with this 
             System.Security.AccessControl.DirectoryObjectSecurity object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAuditRule(self, *args): #cannot find CLR method
        """
        RemoveAuditRule(self: DirectoryObjectSecurity, rule: ObjectAuditRule) -> bool
        
            Removes audit rules that contain the same security identifier and access mask as the specified 
             audit rule from the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to remove.
            Returns: true if the audit rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAuditRuleAll(self, *args): #cannot find CLR method
        """
        RemoveAuditRuleAll(self: DirectoryObjectSecurity, rule: ObjectAuditRule)
            Removes all audit rules that have the same security identifier as the specified audit rule from 
             the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.DirectoryObjectSecurity object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def RemoveAuditRuleSpecific(self, *args): #cannot find CLR method
        """
        RemoveAuditRuleSpecific(self: DirectoryObjectSecurity, rule: ObjectAuditRule)
            Removes all audit rules that exactly match the specified audit rule from the System Access 
             Control List (SACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity 
             object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def ResetAccessRule(self, *args): #cannot find CLR method
        """
        ResetAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule)
            Removes all access rules in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.DirectoryObjectSecurity object and then adds the specified access 
             rule.
        
        
            rule: The access rule to reset.
        """
        pass

    def SetAccessRule(self, *args): #cannot find CLR method
        """
        SetAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule)
            Removes all access rules that contain the same security identifier and qualifier as the 
             specified access rule in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.DirectoryObjectSecurity object and then adds the specified access 
             rule.
        
        
            rule: The access rule to set.
        """
        pass

    def SetAuditRule(self, *args): #cannot find CLR method
        """
        SetAuditRule(self: DirectoryObjectSecurity, rule: ObjectAuditRule)
            Removes all audit rules that contain the same security identifier and qualifier as the specified 
             audit rule in the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.DirectoryObjectSecurity object and then adds the specified audit 
             rule.
        
        
            rule: The audit rule to set.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, securityDescriptor: CommonSecurityDescriptor)
        """
        pass

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class FileSystemSecurity(NativeObjectSecurity):
    """ Represents the access control and audit security for a file or directory. """
    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: FileSystemSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule
        
            Initializes a new instance of the System.Security.AccessControl.FileSystemAccessRule class that 
             represents a new access control rule for the specified user, with the specified access rights, 
             access control, and flags.
        
        
            identityReference: An System.Security.Principal.IdentityReference object that represents a user account.
            accessMask: An integer that specifies an access type.
            isInherited: true if the access rule is inherited; otherwise, false.
            inheritanceFlags: One of the System.Security.AccessControl.InheritanceFlags values that specifies how to propagate 
             access masks to child objects.
        
            propagationFlags: One of the System.Security.AccessControl.PropagationFlags values that specifies how to propagate 
             Access Control Entries (ACEs) to child objects.
        
            type: One of the System.Security.AccessControl.AccessControlType values that specifies whether access 
             is allowed or denied.
        
            Returns: A new System.Security.AccessControl.FileSystemAccessRule object that represents a new access 
             control rule for the specified user, with the specified access rights, access control, and 
             flags.
        """
        pass

    def AddAccessRule(self, rule):
        """
        AddAccessRule(self: FileSystemSecurity, rule: FileSystemAccessRule)
            Adds the specified access control list (ACL) permission to the current file or directory.
        
            rule: A System.Security.AccessControl.FileSystemAccessRule object that represents an access control 
             list (ACL) permission to add to a file or directory.
        """
        pass

    def AddAuditRule(self, rule):
        """
        AddAuditRule(self: FileSystemSecurity, rule: FileSystemAuditRule)
            Adds the specified audit rule to the current file or directory.
        
            rule: A System.Security.AccessControl.FileSystemAuditRule  object that represents an audit rule to add 
             to a file or directory.
        """
        pass

    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: FileSystemSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule
        
            Initializes a new instance of the System.Security.AccessControl.FileSystemAuditRule class 
             representing the specified audit rule for the specified user.
        
        
            identityReference: An System.Security.Principal.IdentityReference object that represents a user account.
            accessMask: An integer that specifies an access type.
            isInherited: true if the access rule is inherited; otherwise, false.
            inheritanceFlags: One of the System.Security.AccessControl.InheritanceFlags values that specifies how to propagate 
             access masks to child objects.
        
            propagationFlags: One of the System.Security.AccessControl.PropagationFlags values that specifies how to propagate 
             Access Control Entries (ACEs) to child objects.
        
            flags: One of the System.Security.AccessControl.AuditFlags values that specifies the type of auditing 
             to perform.
        
            Returns: A new System.Security.AccessControl.FileSystemAuditRule object representing the specified audit 
             rule for the specified user.
        """
        pass

    def RemoveAccessRule(self, rule):
        """
        RemoveAccessRule(self: FileSystemSecurity, rule: FileSystemAccessRule) -> bool
        
            Removes all matching allow or deny access control list (ACL) permissions from the current file 
             or directory.
        
        
            rule: A System.Security.AccessControl.FileSystemAccessRule object that represents an access control 
             list (ACL) permission to remove from a file or directory.
        
            Returns: true if the access rule was removed; otherwise, false.
        """
        pass

    def RemoveAccessRuleAll(self, rule):
        """
        RemoveAccessRuleAll(self: FileSystemSecurity, rule: FileSystemAccessRule)
            Removes all access control list (ACL) permissions for the specified user from the current file 
             or directory.
        
        
            rule: A System.Security.AccessControl.FileSystemAccessRule object that specifies a user whose access 
             control list (ACL) permissions should be removed from a file or directory.
        """
        pass

    def RemoveAccessRuleSpecific(self, rule):
        """
        RemoveAccessRuleSpecific(self: FileSystemSecurity, rule: FileSystemAccessRule)
            Removes a single matching allow or deny access control list (ACL) permission from the current 
             file or directory.
        
        
            rule: A System.Security.AccessControl.FileSystemAccessRule object that specifies a user whose access 
             control list (ACL) permissions should be removed from a file or directory.
        """
        pass

    def RemoveAuditRule(self, rule):
        """
        RemoveAuditRule(self: FileSystemSecurity, rule: FileSystemAuditRule) -> bool
        
            Removes all matching allow or deny audit rules from the current file or directory.
        
            rule: A System.Security.AccessControl.FileSystemAuditRule  object that represents an audit rule to 
             remove from a file or directory.
        
            Returns: true if the audit rule was removed; otherwise, false
        """
        pass

    def RemoveAuditRuleAll(self, rule):
        """
        RemoveAuditRuleAll(self: FileSystemSecurity, rule: FileSystemAuditRule)
            Removes all audit rules for the specified user from the current file or directory.
        
            rule: A System.Security.AccessControl.FileSystemAuditRule object that specifies a user whose audit 
             rules should be removed from a file or directory.
        """
        pass

    def RemoveAuditRuleSpecific(self, rule):
        """
        RemoveAuditRuleSpecific(self: FileSystemSecurity, rule: FileSystemAuditRule)
            Removes a single matching allow or deny audit rule from the current file or directory.
        
            rule: A System.Security.AccessControl.FileSystemAuditRule  object that represents an audit rule to 
             remove from a file or directory.
        """
        pass

    def ResetAccessRule(self, rule):
        """
        ResetAccessRule(self: FileSystemSecurity, rule: FileSystemAccessRule)
            Adds the specified access control list (ACL) permission to the current file or directory and 
             removes all matching ACL permissions.
        
        
            rule: A System.Security.AccessControl.FileSystemAccessRule object that represents an access control 
             list (ACL) permission to add to a file or directory.
        """
        pass

    def SetAccessRule(self, rule):
        """
        SetAccessRule(self: FileSystemSecurity, rule: FileSystemAccessRule)
            Sets the specified access control list (ACL) permission for the current file or directory.
        
            rule: A System.Security.AccessControl.FileSystemAccessRule object that represents an access control 
             list (ACL) permission to set for a file or directory.
        """
        pass

    def SetAuditRule(self, rule):
        """
        SetAuditRule(self: FileSystemSecurity, rule: FileSystemAuditRule)
            Sets the specified audit rule for the current file or directory.
        
            rule: A System.Security.AccessControl.FileSystemAuditRule object that represents an audit rule to set 
             for a file or directory.
        """
        pass

    AccessRightType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the enumeration that the System.Security.AccessControl.FileSystemSecurity class uses to represent access rights.

Get: AccessRightType(self: FileSystemSecurity) -> Type

"""

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AccessRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the enumeration that the System.Security.AccessControl.FileSystemSecurity class uses to represent access rules.

Get: AccessRuleType(self: FileSystemSecurity) -> Type

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that the System.Security.AccessControl.FileSystemSecurity class uses to represent audit rules.

Get: AuditRuleType(self: FileSystemSecurity) -> Type

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class DirectorySecurity(FileSystemSecurity):
    """
    Represents the access control and audit security for a directory. This class cannot be inherited.
    
    DirectorySecurity()
    DirectorySecurity(name: str, includeSections: AccessControlSections)
    """
    def AddAccessRule(self, rule):
        """
        AddAccessRule(self: CommonObjectSecurity, rule: AccessRule)
            Adds the specified access rule to the Discretionary Access Control List (DACL) associated with 
             this System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to add.
        """
        pass

    def AddAuditRule(self, rule):
        """
        AddAuditRule(self: CommonObjectSecurity, rule: AuditRule)
            Adds the specified audit rule to the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to add.
        """
        pass

    def RemoveAccessRule(self, rule):
        """
        RemoveAccessRule(self: CommonObjectSecurity, rule: AccessRule) -> bool
        
            Removes access rules that contain the same security identifier and access mask as the specified 
             access rule from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to remove.
            Returns: true if the access rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAccessRuleAll(self, rule):
        """
        RemoveAccessRuleAll(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules that have the same security identifier as the specified access rule 
             from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAccessRuleSpecific(self, rule):
        """
        RemoveAccessRuleSpecific(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules that exactly match the specified access rule from the Discretionary 
             Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAuditRule(self, rule):
        """
        RemoveAuditRule(self: CommonObjectSecurity, rule: AuditRule) -> bool
        
            Removes audit rules that contain the same security identifier and access mask as the specified 
             audit rule from the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to remove.
            Returns: true if the audit rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAuditRuleAll(self, rule):
        """
        RemoveAuditRuleAll(self: CommonObjectSecurity, rule: AuditRule)
            Removes all audit rules that have the same security identifier as the specified audit rule from 
             the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def RemoveAuditRuleSpecific(self, rule):
        """
        RemoveAuditRuleSpecific(self: CommonObjectSecurity, rule: AuditRule)
            Removes all audit rules that exactly match the specified audit rule from the System Access 
             Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity 
             object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def ResetAccessRule(self, rule):
        """
        ResetAccessRule(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 
             rule.
        
        
            rule: The access rule to reset.
        """
        pass

    def SetAccessRule(self, rule):
        """
        SetAccessRule(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules that contain the same security identifier and qualifier as the 
             specified access rule in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 
             rule.
        
        
            rule: The access rule to set.
        """
        pass

    def SetAuditRule(self, rule):
        """
        SetAuditRule(self: CommonObjectSecurity, rule: AuditRule)
            Removes all audit rules that contain the same security identifier and qualifier as the specified 
             audit rule in the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object and then adds the specified audit 
             rule.
        
        
            rule: The audit rule to set.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, includeSections=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, includeSections: AccessControlSections)
        """
        pass

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class DiscretionaryAcl(CommonAcl, ICollection, IEnumerable):
    """
    Represents a Discretionary Access Control List (DACL).
    
    DiscretionaryAcl(isContainer: bool, isDS: bool, capacity: int)
    DiscretionaryAcl(isContainer: bool, isDS: bool, revision: Byte, capacity: int)
    DiscretionaryAcl(isContainer: bool, isDS: bool, rawAcl: RawAcl)
    """
    def AddAccess(self, accessType, sid, *__args):
        """
        AddAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)
            Adds an Access Control Entry (ACE) with the specified settings to the current 
             System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object 
             Access Control Lists (ACLs) when specifying the object type or the inherited object type for the 
             new ACE.
        
        
            accessType: The type of access control (allow or deny) to add.
            sid: The System.Security.Principal.SecurityIdentifier for which to add an ACE.
            accessMask: The access rule for the new ACE.
            inheritanceFlags: Flags that specify the inheritance properties of the new ACE.
            propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.
            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.
            objectType: The identity of the class of objects to which the new ACE applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the new ACE.
        AddAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule)AddAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)
            Adds an Access Control Entry (ACE) with the specified settings to the current 
             System.Security.AccessControl.DiscretionaryAcl object.
        
        
            accessType: The type of access control (allow or deny) to add.
            sid: The System.Security.Principal.SecurityIdentifier for which to add an ACE.
            accessMask: The access rule for the new ACE.
            inheritanceFlags: Flags that specify the inheritance properties of the new ACE.
            propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.
        """
        pass

    def RemoveAccess(self, accessType, sid, *__args):
        """
        RemoveAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> bool
        
            Removes the specified access control rule from the current 
             System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object 
             Access Control Lists (ACLs) when specifying the object type or the inherited object type.
        
        
            accessType: The type of access control (allow or deny) to remove.
            sid: The System.Security.Principal.SecurityIdentifier for which to remove an access control rule.
            accessMask: The access mask for the access control rule to be removed.
            inheritanceFlags: Flags that specify the inheritance properties of the access control rule to be removed.
            propagationFlags: Flags that specify the inheritance propagation properties for the access control rule to be 
             removed.
        
            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.
            objectType: The identity of the class of objects to which the removed access control rule applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the removed access control rule.
            Returns: true if this method successfully removes the specified access; otherwise, false.
        RemoveAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule) -> bool
        RemoveAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> bool
        
            Removes the specified access control rule from the current 
             System.Security.AccessControl.DiscretionaryAcl object.
        
        
            accessType: The type of access control (allow or deny) to remove.
            sid: The System.Security.Principal.SecurityIdentifier for which to remove an access control rule.
            accessMask: The access mask for the rule to be removed.
            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.
            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.
            Returns: true if this method successfully removes the specified access; otherwise, false.
        """
        pass

    def RemoveAccessSpecific(self, accessType, sid, *__args):
        """
        RemoveAccessSpecific(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)
            Removes the specified Access Control Entry (ACE) from the current 
             System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object 
             Access Control Lists (ACLs) when specifying the object type or the inherited object type for the 
             ACE to be removed.
        
        
            accessType: The type of access control (allow or deny) to remove.
            sid: The System.Security.Principal.SecurityIdentifier for which to remove an ACE.
            accessMask: The access mask for the ACE to be removed.
            inheritanceFlags: Flags that specify the inheritance properties of the ACE to be removed.
            propagationFlags: Flags that specify the inheritance propagation properties for the ACE to be removed.
            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.
            objectType: The identity of the class of objects to which the removed ACE applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the removed ACE.
        RemoveAccessSpecific(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule)RemoveAccessSpecific(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)
            Removes the specified Access Control Entry (ACE) from the current 
             System.Security.AccessControl.DiscretionaryAcl object.
        
        
            accessType: The type of access control (allow or deny) to remove.
            sid: The System.Security.Principal.SecurityIdentifier for which to remove an ACE.
            accessMask: The access mask for the ACE to be removed.
            inheritanceFlags: Flags that specify the inheritance properties of the ACE to be removed.
            propagationFlags: Flags that specify the inheritance propagation properties for the ACE to be removed.
        """
        pass

    def SetAccess(self, accessType, sid, *__args):
        """
        SetAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)
            Sets the specified access control for the specified System.Security.Principal.SecurityIdentifier 
             object.
        
        
            accessType: The type of access control (allow or deny) to set.
            sid: The System.Security.Principal.SecurityIdentifier for which to set an ACE.
            accessMask: The access rule for the new ACE.
            inheritanceFlags: Flags that specify the inheritance properties of the new ACE.
            propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.
            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.
            objectType: The identity of the class of objects to which the new ACE applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the new ACE.
        SetAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule)SetAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)
            Sets the specified access control for the specified System.Security.Principal.SecurityIdentifier 
             object.
        
        
            accessType: The type of access control (allow or deny) to set.
            sid: The System.Security.Principal.SecurityIdentifier for which to set an ACE.
            accessMask: The access rule for the new ACE.
            inheritanceFlags: Flags that specify the inheritance properties of the new ACE.
            propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.
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

    @staticmethod # known case of __new__
    def __new__(self, isContainer, isDS, *__args):
        """
        __new__(cls: type, isContainer: bool, isDS: bool, capacity: int)
        __new__(cls: type, isContainer: bool, isDS: bool, revision: Byte, capacity: int)
        __new__(cls: type, isContainer: bool, isDS: bool, rawAcl: RawAcl)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class EventWaitHandleAccessRule(AccessRule):
    """
    Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.
    
    EventWaitHandleAccessRule(identity: IdentityReference, eventRights: EventWaitHandleRights, type: AccessControlType)
    EventWaitHandleAccessRule(identity: str, eventRights: EventWaitHandleRights, type: AccessControlType)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, eventRights, type):
        """
        __new__(cls: type, identity: IdentityReference, eventRights: EventWaitHandleRights, type: AccessControlType)
        __new__(cls: type, identity: str, eventRights: EventWaitHandleRights, type: AccessControlType)
        """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    EventWaitHandleRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rights allowed or denied by the access rule.

Get: EventWaitHandleRights(self: EventWaitHandleAccessRule) -> EventWaitHandleRights

"""



class EventWaitHandleAuditRule(AuditRule):
    """
    Represents a set of access rights to be audited for a user or group. This class cannot be inherited.
    
    EventWaitHandleAuditRule(identity: IdentityReference, eventRights: EventWaitHandleRights, flags: AuditFlags)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, eventRights, flags):
        """ __new__(cls: type, identity: IdentityReference, eventRights: EventWaitHandleRights, flags: AuditFlags) """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    EventWaitHandleRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access rights affected by the audit rule.

Get: EventWaitHandleRights(self: EventWaitHandleAuditRule) -> EventWaitHandleRights

"""



class EventWaitHandleRights(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the access control rights that can be applied to named system event objects.
    
    enum (flags) EventWaitHandleRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031619), Modify (2), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288)
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

    ChangePermissions = None
    Delete = None
    FullControl = None
    Modify = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None


class EventWaitHandleSecurity(NativeObjectSecurity):
    """
    Represents the Windows access control security applied to a named system wait handle. This class cannot be inherited.
    
    EventWaitHandleSecurity()
    """
    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: EventWaitHandleSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule
        
            Creates a new access control rule for the specified user, with the specified access rights, 
             access control, and flags.
        
        
            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 
             applies to.
        
            accessMask: A bitwise combination of System.Security.AccessControl.EventWaitHandleRights values specifying 
             the access rights to allow or deny, cast to an integer.
        
            isInherited: Meaningless for named wait handles, because they have no hierarchy.
            inheritanceFlags: Meaningless for named wait handles, because they have no hierarchy.
            propagationFlags: Meaningless for named wait handles, because they have no hierarchy.
            type: One of the System.Security.AccessControl.AccessControlType values specifying whether the rights 
             are allowed or denied.
        
            Returns: An System.Security.AccessControl.EventWaitHandleAccessRule object representing the specified 
             rights for the specified user.
        """
        pass

    def AddAccessRule(self, rule):
        """
        AddAccessRule(self: EventWaitHandleSecurity, rule: EventWaitHandleAccessRule)
            Searches for a matching access control rule with which the new rule can be merged. If none are 
             found, adds the new rule.
        
        
            rule: The access control rule to add.
        """
        pass

    def AddAuditRule(self, rule):
        """
        AddAuditRule(self: EventWaitHandleSecurity, rule: EventWaitHandleAuditRule)
            Searches for an audit rule with which the new rule can be merged. If none are found, adds the 
             new rule.
        
        
            rule: The audit rule to add. The user specified by this rule determines the search.
        """
        pass

    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: EventWaitHandleSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule
        
            Creates a new audit rule, specifying the user the rule applies to, the access rights to audit, 
             and the outcome that triggers the audit rule.
        
        
            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 
             applies to.
        
            accessMask: A bitwise combination of System.Security.AccessControl.EventWaitHandleRights values specifying 
             the access rights to audit, cast to an integer.
        
            isInherited: Meaningless for named wait handles, because they have no hierarchy.
            inheritanceFlags: Meaningless for named wait handles, because they have no hierarchy.
            propagationFlags: Meaningless for named wait handles, because they have no hierarchy.
            flags: A bitwise combination of System.Security.AccessControl.AuditFlags values specifying whether to 
             audit successful access, failed access, or both.
        
            Returns: An System.Security.AccessControl.EventWaitHandleAuditRule object representing the specified 
             audit rule for the specified user. The return type of the method is the base class, 
             System.Security.AccessControl.AuditRule, but the return value can be cast safely to the derived 
             class.
        """
        pass

    def RemoveAccessRule(self, rule):
        """
        RemoveAccessRule(self: EventWaitHandleSecurity, rule: EventWaitHandleAccessRule) -> bool
        
            Searches for an access control rule with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified access rule, 
             and with compatible inheritance and propagation flags; if such a rule is found, the rights 
             contained in the specified access rule are removed from it.
        
        
            rule: An System.Security.AccessControl.EventWaitHandleAccessRule that specifies the user and 
             System.Security.AccessControl.AccessControlType to search for, and a set of inheritance and 
             propagation flags that a matching rule, if found, must be compatible with. Specifies the rights 
             to remove from the compatible rule, if found.
        
            Returns: true if a compatible rule is found; otherwise, false.
        """
        pass

    def RemoveAccessRuleAll(self, rule):
        """
        RemoveAccessRuleAll(self: EventWaitHandleSecurity, rule: EventWaitHandleAccessRule)
            Searches for all access control rules with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule and, if 
             found, removes them.
        
        
            rule: An System.Security.AccessControl.EventWaitHandleAccessRule that specifies the user and 
             System.Security.AccessControl.AccessControlType to search for. Any rights specified by this rule 
             are ignored.
        """
        pass

    def RemoveAccessRuleSpecific(self, rule):
        """
        RemoveAccessRuleSpecific(self: EventWaitHandleSecurity, rule: EventWaitHandleAccessRule)
            Searches for an access control rule that exactly matches the specified rule and, if found, 
             removes it.
        
        
            rule: The System.Security.AccessControl.EventWaitHandleAccessRule to remove.
        """
        pass

    def RemoveAuditRule(self, rule):
        """
        RemoveAuditRule(self: EventWaitHandleSecurity, rule: EventWaitHandleAuditRule) -> bool
        
            Searches for an audit rule with the same user as the specified rule, and with compatible 
             inheritance and propagation flags; if a compatible rule is found, the rights contained in the 
             specified rule are removed from it.
        
        
            rule: An System.Security.AccessControl.EventWaitHandleAuditRule that specifies the user to search for 
             and a set of inheritance and propagation flags that a matching rule, if found, must be 
             compatible with. Specifies the rights to remove from the compatible rule, if found.
        
            Returns: true if a compatible rule is found; otherwise, false.
        """
        pass

    def RemoveAuditRuleAll(self, rule):
        """
        RemoveAuditRuleAll(self: EventWaitHandleSecurity, rule: EventWaitHandleAuditRule)
            Searches for all audit rules with the same user as the specified rule and, if found, removes 
             them.
        
        
            rule: An System.Security.AccessControl.EventWaitHandleAuditRule that specifies the user to search for. 
             Any rights specified by this rule are ignored.
        """
        pass

    def RemoveAuditRuleSpecific(self, rule):
        """
        RemoveAuditRuleSpecific(self: EventWaitHandleSecurity, rule: EventWaitHandleAuditRule)
            Searches for an audit rule that exactly matches the specified rule and, if found, removes it.
        
            rule: The System.Security.AccessControl.EventWaitHandleAuditRule to remove.
        """
        pass

    def ResetAccessRule(self, rule):
        """
        ResetAccessRule(self: EventWaitHandleSecurity, rule: EventWaitHandleAccessRule)
            Removes all access control rules with the same user as the specified rule, regardless of 
             System.Security.AccessControl.AccessControlType, and then adds the specified rule.
        
        
            rule: The System.Security.AccessControl.EventWaitHandleAccessRule to add. The user specified by this 
             rule determines the rules to remove before this rule is added.
        """
        pass

    def SetAccessRule(self, rule):
        """
        SetAccessRule(self: EventWaitHandleSecurity, rule: EventWaitHandleAccessRule)
            Removes all access control rules with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule, and then 
             adds the specified rule.
        
        
            rule: The System.Security.AccessControl.EventWaitHandleAccessRule to add. The user and 
             System.Security.AccessControl.AccessControlType of this rule determine the rules to remove 
             before this rule is added.
        """
        pass

    def SetAuditRule(self, rule):
        """
        SetAuditRule(self: EventWaitHandleSecurity, rule: EventWaitHandleAuditRule)
            Removes all audit rules with the same user as the specified rule, regardless of the 
             System.Security.AccessControl.AuditFlags value, and then adds the specified rule.
        
        
            rule: The System.Security.AccessControl.EventWaitHandleAuditRule to add. The user specified by this 
             rule determines the rules to remove before this rule is added.
        """
        pass

    AccessRightType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the enumeration type that the System.Security.AccessControl.EventWaitHandleSecurity class uses to represent access rights.

Get: AccessRightType(self: EventWaitHandleSecurity) -> Type

"""

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AccessRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that the System.Security.AccessControl.EventWaitHandleSecurity class uses to represent access rules.

Get: AccessRuleType(self: EventWaitHandleSecurity) -> Type

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that the System.Security.AccessControl.EventWaitHandleSecurity class uses to represent audit rules.

Get: AuditRuleType(self: EventWaitHandleSecurity) -> Type

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class FileSecurity(FileSystemSecurity):
    """
    Represents the access control and audit security for a file. This class cannot be inherited.
    
    FileSecurity(fileName: str, includeSections: AccessControlSections)
    FileSecurity()
    """
    def AddAccessRule(self, rule):
        """
        AddAccessRule(self: CommonObjectSecurity, rule: AccessRule)
            Adds the specified access rule to the Discretionary Access Control List (DACL) associated with 
             this System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to add.
        """
        pass

    def AddAuditRule(self, rule):
        """
        AddAuditRule(self: CommonObjectSecurity, rule: AuditRule)
            Adds the specified audit rule to the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to add.
        """
        pass

    def RemoveAccessRule(self, rule):
        """
        RemoveAccessRule(self: CommonObjectSecurity, rule: AccessRule) -> bool
        
            Removes access rules that contain the same security identifier and access mask as the specified 
             access rule from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to remove.
            Returns: true if the access rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAccessRuleAll(self, rule):
        """
        RemoveAccessRuleAll(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules that have the same security identifier as the specified access rule 
             from the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAccessRuleSpecific(self, rule):
        """
        RemoveAccessRuleSpecific(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules that exactly match the specified access rule from the Discretionary 
             Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The access rule to remove.
        """
        pass

    def RemoveAuditRule(self, rule):
        """
        RemoveAuditRule(self: CommonObjectSecurity, rule: AuditRule) -> bool
        
            Removes audit rules that contain the same security identifier and access mask as the specified 
             audit rule from the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to remove.
            Returns: true if the audit rule was successfully removed; otherwise, false.
        """
        pass

    def RemoveAuditRuleAll(self, rule):
        """
        RemoveAuditRuleAll(self: CommonObjectSecurity, rule: AuditRule)
            Removes all audit rules that have the same security identifier as the specified audit rule from 
             the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def RemoveAuditRuleSpecific(self, rule):
        """
        RemoveAuditRuleSpecific(self: CommonObjectSecurity, rule: AuditRule)
            Removes all audit rules that exactly match the specified audit rule from the System Access 
             Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity 
             object.
        
        
            rule: The audit rule to remove.
        """
        pass

    def ResetAccessRule(self, rule):
        """
        ResetAccessRule(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 
             rule.
        
        
            rule: The access rule to reset.
        """
        pass

    def SetAccessRule(self, rule):
        """
        SetAccessRule(self: CommonObjectSecurity, rule: AccessRule)
            Removes all access rules that contain the same security identifier and qualifier as the 
             specified access rule in the Discretionary Access Control List (DACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 
             rule.
        
        
            rule: The access rule to set.
        """
        pass

    def SetAuditRule(self, rule):
        """
        SetAuditRule(self: CommonObjectSecurity, rule: AuditRule)
            Removes all audit rules that contain the same security identifier and qualifier as the specified 
             audit rule in the System Access Control List (SACL) associated with this 
             System.Security.AccessControl.CommonObjectSecurity object and then adds the specified audit 
             rule.
        
        
            rule: The audit rule to set.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fileName=None, includeSections=None):
        """
        __new__(cls: type)
        __new__(cls: type, fileName: str, includeSections: AccessControlSections)
        """
        pass

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class FileSystemAccessRule(AccessRule):
    """
    Represents an abstraction of an access control entry (ACE) that defines an access rule for a file or directory. This class cannot be inherited.
    
    FileSystemAccessRule(identity: IdentityReference, fileSystemRights: FileSystemRights, type: AccessControlType)
    FileSystemAccessRule(identity: str, fileSystemRights: FileSystemRights, type: AccessControlType)
    FileSystemAccessRule(identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    FileSystemAccessRule(identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, fileSystemRights, *__args):
        """
        __new__(cls: type, identity: IdentityReference, fileSystemRights: FileSystemRights, type: AccessControlType)
        __new__(cls: type, identity: str, fileSystemRights: FileSystemRights, type: AccessControlType)
        __new__(cls: type, identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
        __new__(cls: type, identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
        """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    FileSystemRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Security.AccessControl.FileSystemRights flags associated with the current System.Security.AccessControl.FileSystemAccessRule object.

Get: FileSystemRights(self: FileSystemAccessRule) -> FileSystemRights

"""



class FileSystemAuditRule(AuditRule):
    """
    Represents an abstraction of an access control entry (ACE) that defines an audit rule for a file or directory. This class cannot be inherited.
    
    FileSystemAuditRule(identity: IdentityReference, fileSystemRights: FileSystemRights, flags: AuditFlags)
    FileSystemAuditRule(identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    FileSystemAuditRule(identity: str, fileSystemRights: FileSystemRights, flags: AuditFlags)
    FileSystemAuditRule(identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, fileSystemRights, *__args):
        """
        __new__(cls: type, identity: IdentityReference, fileSystemRights: FileSystemRights, flags: AuditFlags)
        __new__(cls: type, identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
        __new__(cls: type, identity: str, fileSystemRights: FileSystemRights, flags: AuditFlags)
        __new__(cls: type, identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
        """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    FileSystemRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Security.AccessControl.FileSystemRights flags associated with the current System.Security.AccessControl.FileSystemAuditRule object.

Get: FileSystemRights(self: FileSystemAuditRule) -> FileSystemRights

"""



class FileSystemRights(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the access rights to use when creating access and audit rules.
    
    enum (flags) FileSystemRights, values: AppendData (4), ChangePermissions (262144), CreateDirectories (4), CreateFiles (2), Delete (65536), DeleteSubdirectoriesAndFiles (64), ExecuteFile (32), FullControl (2032127), ListDirectory (1), Modify (197055), Read (131209), ReadAndExecute (131241), ReadAttributes (128), ReadData (1), ReadExtendedAttributes (8), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288), Traverse (32), Write (278), WriteAttributes (256), WriteData (2), WriteExtendedAttributes (16)
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

    AppendData = None
    ChangePermissions = None
    CreateDirectories = None
    CreateFiles = None
    Delete = None
    DeleteSubdirectoriesAndFiles = None
    ExecuteFile = None
    FullControl = None
    ListDirectory = None
    Modify = None
    Read = None
    ReadAndExecute = None
    ReadAttributes = None
    ReadData = None
    ReadExtendedAttributes = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    Traverse = None
    value__ = None
    Write = None
    WriteAttributes = None
    WriteData = None
    WriteExtendedAttributes = None


class InheritanceFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Inheritance flags specify the semantics of inheritance for access control entries (ACEs).
    
    enum (flags) InheritanceFlags, values: ContainerInherit (1), None (0), ObjectInherit (2)
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

    ContainerInherit = None
    None = None
    ObjectInherit = None
    value__ = None


class MutexAccessRule(AccessRule):
    """
    Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.
    
    MutexAccessRule(identity: IdentityReference, eventRights: MutexRights, type: AccessControlType)
    MutexAccessRule(identity: str, eventRights: MutexRights, type: AccessControlType)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, eventRights, type):
        """
        __new__(cls: type, identity: IdentityReference, eventRights: MutexRights, type: AccessControlType)
        __new__(cls: type, identity: str, eventRights: MutexRights, type: AccessControlType)
        """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    MutexRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rights allowed or denied by the access rule.

Get: MutexRights(self: MutexAccessRule) -> MutexRights

"""



class MutexAuditRule(AuditRule):
    """
    Represents a set of access rights to be audited for a user or group. This class cannot be inherited.
    
    MutexAuditRule(identity: IdentityReference, eventRights: MutexRights, flags: AuditFlags)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, eventRights, flags):
        """ __new__(cls: type, identity: IdentityReference, eventRights: MutexRights, flags: AuditFlags) """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    MutexRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access rights affected by the audit rule.

Get: MutexRights(self: MutexAuditRule) -> MutexRights

"""



class MutexRights(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the access control rights that can be applied to named system mutex objects.
    
    enum (flags) MutexRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031617), Modify (1), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288)
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

    ChangePermissions = None
    Delete = None
    FullControl = None
    Modify = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None


class MutexSecurity(NativeObjectSecurity):
    """
    Represents the Windows access control security for a named mutex. This class cannot be inherited.
    
    MutexSecurity()
    MutexSecurity(name: str, includeSections: AccessControlSections)
    """
    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: MutexSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule
        
            Creates a new access control rule for the specified user, with the specified access rights, 
             access control, and flags.
        
        
            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 
             applies to.
        
            accessMask: A bitwise combination of System.Security.AccessControl.MutexRights values specifying the access 
             rights to allow or deny, cast to an integer.
        
            isInherited: Meaningless for named mutexes, because they have no hierarchy.
            inheritanceFlags: Meaningless for named mutexes, because they have no hierarchy.
            propagationFlags: Meaningless for named mutexes, because they have no hierarchy.
            type: One of the System.Security.AccessControl.AccessControlType values specifying whether the rights 
             are allowed or denied.
        
            Returns: A System.Security.AccessControl.MutexAccessRule object representing the specified rights for the 
             specified user.
        """
        pass

    def AddAccessRule(self, rule):
        """
        AddAccessRule(self: MutexSecurity, rule: MutexAccessRule)
            Searches for a matching access control rule with which the new rule can be merged. If none are 
             found, adds the new rule.
        
        
            rule: The access control rule to add.
        """
        pass

    def AddAuditRule(self, rule):
        """
        AddAuditRule(self: MutexSecurity, rule: MutexAuditRule)
            Searches for an audit rule with which the new rule can be merged. If none are found, adds the 
             new rule.
        
        
            rule: The audit rule to add. The user specified by this rule determines the search.
        """
        pass

    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: MutexSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule
        
            Creates a new audit rule, specifying the user the rule applies to, the access rights to audit, 
             and the outcome that triggers the audit rule.
        
        
            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 
             applies to.
        
            accessMask: A bitwise combination of System.Security.AccessControl.MutexRights values specifying the access 
             rights to audit, cast to an integer.
        
            isInherited: Meaningless for named wait handles, because they have no hierarchy.
            inheritanceFlags: Meaningless for named wait handles, because they have no hierarchy.
            propagationFlags: Meaningless for named wait handles, because they have no hierarchy.
            flags: A bitwise combination of System.Security.AccessControl.AuditFlags values that specify whether to 
             audit successful access, failed access, or both.
        
            Returns: A System.Security.AccessControl.MutexAuditRule object representing the specified audit rule for 
             the specified user. The return type of the method is the base class, 
             System.Security.AccessControl.AuditRule, but the return value can be cast safely to the derived 
             class.
        """
        pass

    def RemoveAccessRule(self, rule):
        """
        RemoveAccessRule(self: MutexSecurity, rule: MutexAccessRule) -> bool
        
            Searches for an access control rule with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule, and with 
             compatible inheritance and propagation flags; if such a rule is found, the rights contained in 
             the specified access rule are removed from it.
        
        
            rule: A System.Security.AccessControl.MutexAccessRule that specifies the user and 
             System.Security.AccessControl.AccessControlType to search for, and a set of inheritance and 
             propagation flags that a matching rule, if found, must be compatible with. Specifies the rights 
             to remove from the compatible rule, if found.
        
            Returns: true if a compatible rule is found; otherwise false.
        """
        pass

    def RemoveAccessRuleAll(self, rule):
        """
        RemoveAccessRuleAll(self: MutexSecurity, rule: MutexAccessRule)
            Searches for all access control rules with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule and, if 
             found, removes them.
        
        
            rule: A System.Security.AccessControl.MutexAccessRule that specifies the user and 
             System.Security.AccessControl.AccessControlType to search for. Any rights specified by this rule 
             are ignored.
        """
        pass

    def RemoveAccessRuleSpecific(self, rule):
        """
        RemoveAccessRuleSpecific(self: MutexSecurity, rule: MutexAccessRule)
            Searches for an access control rule that exactly matches the specified rule and, if found, 
             removes it.
        
        
            rule: The System.Security.AccessControl.MutexAccessRule to remove.
        """
        pass

    def RemoveAuditRule(self, rule):
        """
        RemoveAuditRule(self: MutexSecurity, rule: MutexAuditRule) -> bool
        
            Searches for an audit control rule with the same user as the specified rule, and with compatible 
             inheritance and propagation flags; if a compatible rule is found, the rights contained in the 
             specified rule are removed from it.
        
        
            rule: A System.Security.AccessControl.MutexAuditRule that specifies the user to search for, and a set 
             of inheritance and propagation flags that a matching rule, if found, must be compatible with. 
             Specifies the rights to remove from the compatible rule, if found.
        
            Returns: true if a compatible rule is found; otherwise, false.
        """
        pass

    def RemoveAuditRuleAll(self, rule):
        """
        RemoveAuditRuleAll(self: MutexSecurity, rule: MutexAuditRule)
            Searches for all audit rules with the same user as the specified rule and, if found, removes 
             them.
        
        
            rule: A System.Security.AccessControl.MutexAuditRule that specifies the user to search for. Any rights 
             specified by this rule are ignored.
        """
        pass

    def RemoveAuditRuleSpecific(self, rule):
        """
        RemoveAuditRuleSpecific(self: MutexSecurity, rule: MutexAuditRule)
            Searches for an audit rule that exactly matches the specified rule and, if found, removes it.
        
            rule: The System.Security.AccessControl.MutexAuditRule to be removed.
        """
        pass

    def ResetAccessRule(self, rule):
        """
        ResetAccessRule(self: MutexSecurity, rule: MutexAccessRule)
            Removes all access control rules with the same user as the specified rule, regardless of 
             System.Security.AccessControl.AccessControlType, and then adds the specified rule.
        
        
            rule: The System.Security.AccessControl.MutexAccessRule to add. The user specified by this rule 
             determines the rules to remove before this rule is added.
        """
        pass

    def SetAccessRule(self, rule):
        """
        SetAccessRule(self: MutexSecurity, rule: MutexAccessRule)
            Removes all access control rules with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule, and then 
             adds the specified rule.
        
        
            rule: The System.Security.AccessControl.MutexAccessRule to add. The user and 
             System.Security.AccessControl.AccessControlType of this rule determine the rules to remove 
             before this rule is added.
        """
        pass

    def SetAuditRule(self, rule):
        """
        SetAuditRule(self: MutexSecurity, rule: MutexAuditRule)
            Removes all audit rules with the same user as the specified rule, regardless of the 
             System.Security.AccessControl.AuditFlags value, and then adds the specified rule.
        
        
            rule: The System.Security.AccessControl.MutexAuditRule to add. The user specified by this rule 
             determines the rules to remove before this rule is added.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, includeSections=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, includeSections: AccessControlSections)
        """
        pass

    AccessRightType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the enumeration that the System.Security.AccessControl.MutexSecurity class uses to represent access rights.

Get: AccessRightType(self: MutexSecurity) -> Type

"""

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AccessRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that the System.Security.AccessControl.MutexSecurity class uses to represent access rules.

Get: AccessRuleType(self: MutexSecurity) -> Type

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that the System.Security.AccessControl.MutexSecurity class uses to represent audit rules.

Get: AuditRuleType(self: MutexSecurity) -> Type

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class ObjectAccessRule(AccessRule):
    """ Represents a combination of a user's identity, an access mask, and an access control type (allow or deny). An System.Security.AccessControl.ObjectAccessRule object also contains information about the type of object to which the rule applies, the type of child object that can inherit the rule, how the rule is inherited by child objects, and how that inheritance is propagated. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, identity: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectType: Guid, inheritedObjectType: Guid, type: AccessControlType) """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    InheritedObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of child object that can inherit the stem.Security.AccessControl.ObjectAccessRule object.

Get: InheritedObjectType(self: ObjectAccessRule) -> Guid

"""

    ObjectFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets flags that specify if the System.Security.AccessControl.ObjectAccessRule.ObjectType and System.Security.AccessControl.ObjectAccessRule.InheritedObjectType properties of the stem.Security.AccessControl.ObjectAccessRule object contain valid values.

Get: ObjectFlags(self: ObjectAccessRule) -> ObjectAceFlags

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of object to which the stem.Security.AccessControl.ObjectAccessRule applies.

Get: ObjectType(self: ObjectAccessRule) -> Guid

"""



class ObjectAce(QualifiedAce):
    """
    Controls access to Directory Services objects. This class represents an Access Control Entry (ACE) associated with a directory object.
    
    ObjectAce(aceFlags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, flags: ObjectAceFlags, type: Guid, inheritedType: Guid, isCallback: bool, opaque: Array[Byte])
    """
    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: ObjectAce, binaryForm: Array[Byte], offset: int)
            Marshals the contents of the System.Security.AccessControl.ObjectAce object into the specified 
             byte array beginning at the specified offset.
        
        
            binaryForm: The byte array into which the contents of the System.Security.AccessControl.ObjectAce is 
             marshaled.
        
            offset: The offset at which to start marshaling.
        """
        pass

    @staticmethod
    def MaxOpaqueLength(isCallback):
        """
        MaxOpaqueLength(isCallback: bool) -> int
        
            Returns the maximum allowed length, in bytes, of an opaque data BLOB for callback Access Control 
             Entries (ACEs).
        
        
            isCallback: True if the System.Security.AccessControl.ObjectAce is a callback ACE type.
            Returns: The maximum allowed length, in bytes, of an opaque data BLOB for callback Access Control Entries 
             (ACEs).
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, aceFlags, qualifier, accessMask, sid, flags, type, inheritedType, isCallback, opaque):
        """ __new__(cls: type, aceFlags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, flags: ObjectAceFlags, type: Guid, inheritedType: Guid, isCallback: bool, opaque: Array[Byte]) """
        pass

    BinaryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.ObjectAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.ObjectAce.GetBinaryForm method.

Get: BinaryLength(self: ObjectAce) -> int

"""

    InheritedObjectAceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the GUID of the object type that can inherit the Access Control Entry (ACE) that this System.Security.AccessControl.ObjectAce object represents.

Get: InheritedObjectAceType(self: ObjectAce) -> Guid

Set: InheritedObjectAceType(self: ObjectAce) = value
"""

    ObjectAceFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets flags that specify whether the System.Security.AccessControl.ObjectAce.ObjectAceType and System.Security.AccessControl.ObjectAce.InheritedObjectAceType properties contain values that identify valid object types.

Get: ObjectAceFlags(self: ObjectAce) -> ObjectAceFlags

Set: ObjectAceFlags(self: ObjectAce) = value
"""

    ObjectAceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the GUID of the object type associated with this System.Security.AccessControl.ObjectAce object.

Get: ObjectAceType(self: ObjectAce) -> Guid

Set: ObjectAceType(self: ObjectAce) = value
"""



class ObjectAceFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the presence of object types for Access Control Entries (ACEs).
    
    enum (flags) ObjectAceFlags, values: InheritedObjectAceTypePresent (2), None (0), ObjectAceTypePresent (1)
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

    InheritedObjectAceTypePresent = None
    None = None
    ObjectAceTypePresent = None
    value__ = None


class ObjectAuditRule(AuditRule):
    """ Represents a combination of a user's identity, an access mask, and audit conditions. An System.Security.AccessControl.ObjectAuditRule object also contains information about the type of object to which the rule applies, the type of child object that can inherit the rule, how the rule is inherited by child objects, and how that inheritance is propagated. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, identity: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectType: Guid, inheritedObjectType: Guid, auditFlags: AuditFlags) """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    InheritedObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of child object that can inherit the stem.Security.AccessControl.ObjectAuditRule object.

Get: InheritedObjectType(self: ObjectAuditRule) -> Guid

"""

    ObjectFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """System.Security.AccessControl.ObjectAuditRule.ObjectType and System.Security.AccessControl.ObjectAuditRule.InheritedObjectType properties of the stem.Security.AccessControl.ObjectAuditRule object contain valid values.

Get: ObjectFlags(self: ObjectAuditRule) -> ObjectAceFlags

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of object to which the stem.Security.AccessControl.ObjectAuditRule applies.

Get: ObjectType(self: ObjectAuditRule) -> Guid

"""



class PrivilegeNotHeldException(UnauthorizedAccessException, ISerializable, _Exception):
    """
    The exception that is thrown when a method in the System.Security.AccessControl namespace attempts to enable a privilege that it does not have.
    
    PrivilegeNotHeldException()
    PrivilegeNotHeldException(privilege: str)
    PrivilegeNotHeldException(privilege: str, inner: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: PrivilegeNotHeldException, info: SerializationInfo, context: StreamingContext)
            Sets the info parameter with information about the exception.
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about 
             the exception being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the 
             source or destination.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, privilege=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, privilege: str)
        __new__(cls: type, privilege: str, inner: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PrivilegeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the privilege that is not enabled.

Get: PrivilegeName(self: PrivilegeNotHeldException) -> str

"""



class PropagationFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how Access Control Entries (ACEs) are propagated to child objects.  These flags are significant only if inheritance flags are present.
    
    enum (flags) PropagationFlags, values: InheritOnly (2), None (0), NoPropagateInherit (1)
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

    InheritOnly = None
    None = None
    NoPropagateInherit = None
    value__ = None


class RawAcl(GenericAcl, ICollection, IEnumerable):
    """
    Represents an Access Control List (ACL).
    
    RawAcl(revision: Byte, capacity: int)
    RawAcl(binaryForm: Array[Byte], offset: int)
    """
    def GetBinaryForm(self, binaryForm, offset):
        """
        GetBinaryForm(self: RawAcl, binaryForm: Array[Byte], offset: int)
            Marshals the contents of the System.Security.AccessControl.RawAcl object into the specified byte 
             array beginning at the specified offset.
        
        
            binaryForm: The byte array into which the contents of the System.Security.AccessControl.RawAcl is marshaled.
            offset: The offset at which to start marshaling.
        """
        pass

    def InsertAce(self, index, ace):
        """
        InsertAce(self: RawAcl, index: int, ace: GenericAce)
            Inserts the specified Access Control Entry (ACE) at the specified index.
        
            index: The position at which to add the new ACE. Specify the value of the 
             System.Security.AccessControl.RawAcl.Count property to insert an ACE at the end of the 
             System.Security.AccessControl.RawAcl object.
        
            ace: The ACE to insert.
        """
        pass

    def RemoveAce(self, index):
        """
        RemoveAce(self: RawAcl, index: int)
            Removes the Access Control Entry (ACE) at the specified location.
        
            index: The zero-based index of the ACE to remove.
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, revision: Byte, capacity: int)
        __new__(cls: type, binaryForm: Array[Byte], offset: int)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    BinaryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length, in bytes, of the binary representation of the current System.Security.AccessControl.RawAcl object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.RawAcl.GetBinaryForm method.

Get: BinaryLength(self: RawAcl) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of access control entries (ACEs) in the current System.Security.AccessControl.RawAcl object.

Get: Count(self: RawAcl) -> int

"""

    Revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the revision level of the System.Security.AccessControl.RawAcl.

Get: Revision(self: RawAcl) -> Byte

"""



class RawSecurityDescriptor(GenericSecurityDescriptor):
    """
    Represents a security descriptor. A security descriptor includes an owner, a primary group, a Discretionary Access Control List (DACL), and a System Access Control List (SACL).
    
    RawSecurityDescriptor(flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: RawAcl, discretionaryAcl: RawAcl)
    RawSecurityDescriptor(sddlForm: str)
    RawSecurityDescriptor(binaryForm: Array[Byte], offset: int)
    """
    def SetFlags(self, flags):
        """
        SetFlags(self: RawSecurityDescriptor, flags: ControlFlags)
            Sets the System.Security.AccessControl.RawSecurityDescriptor.ControlFlags property of this 
             System.Security.AccessControl.RawSecurityDescriptor object to the specified value.
        
        
            flags: One or more values of the System.Security.AccessControl.ControlFlags enumeration combined with a 
             logical OR operation.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: RawAcl, discretionaryAcl: RawAcl)
        __new__(cls: type, sddlForm: str)
        __new__(cls: type, binaryForm: Array[Byte], offset: int)
        """
        pass

    ControlFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets values that specify behavior of the System.Security.AccessControl.RawSecurityDescriptor object.

Get: ControlFlags(self: RawSecurityDescriptor) -> ControlFlags

"""

    DiscretionaryAcl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Discretionary Access Control List (DACL) for this System.Security.AccessControl.RawSecurityDescriptor object. The DACL contains access rules.

Get: DiscretionaryAcl(self: RawSecurityDescriptor) -> RawAcl

Set: DiscretionaryAcl(self: RawSecurityDescriptor) = value
"""

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the primary group for this System.Security.AccessControl.RawSecurityDescriptor object.

Get: Group(self: RawSecurityDescriptor) -> SecurityIdentifier

Set: Group(self: RawSecurityDescriptor) = value
"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the owner of the object associated with this System.Security.AccessControl.RawSecurityDescriptor object.

Get: Owner(self: RawSecurityDescriptor) -> SecurityIdentifier

Set: Owner(self: RawSecurityDescriptor) = value
"""

    ResourceManagerControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a byte value that represents the resource manager control bits associated with this System.Security.AccessControl.RawSecurityDescriptor object.

Get: ResourceManagerControl(self: RawSecurityDescriptor) -> Byte

Set: ResourceManagerControl(self: RawSecurityDescriptor) = value
"""

    SystemAcl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System Access Control List (SACL) for this System.Security.AccessControl.RawSecurityDescriptor object. The SACL contains audit rules.

Get: SystemAcl(self: RawSecurityDescriptor) -> RawAcl

Set: SystemAcl(self: RawSecurityDescriptor) = value
"""



class RegistryAccessRule(AccessRule):
    """
    Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.
    
    RegistryAccessRule(identity: IdentityReference, registryRights: RegistryRights, type: AccessControlType)
    RegistryAccessRule(identity: str, registryRights: RegistryRights, type: AccessControlType)
    RegistryAccessRule(identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    RegistryAccessRule(identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, registryRights, *__args):
        """
        __new__(cls: type, identity: IdentityReference, registryRights: RegistryRights, type: AccessControlType)
        __new__(cls: type, identity: str, registryRights: RegistryRights, type: AccessControlType)
        __new__(cls: type, identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
        __new__(cls: type, identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
        """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    RegistryRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rights allowed or denied by the access rule.

Get: RegistryRights(self: RegistryAccessRule) -> RegistryRights

"""



class RegistryAuditRule(AuditRule):
    """
    Represents a set of access rights to be audited for a user or group. This class cannot be inherited.
    
    RegistryAuditRule(identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    RegistryAuditRule(identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, registryRights, inheritanceFlags, propagationFlags, flags):
        """
        __new__(cls: type, identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
        __new__(cls: type, identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
        """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    RegistryRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access rights affected by the audit rule.

Get: RegistryRights(self: RegistryAuditRule) -> RegistryRights

"""



class RegistryRights(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the access control rights that can be applied to registry objects.
    
    enum (flags) RegistryRights, values: ChangePermissions (262144), CreateLink (32), CreateSubKey (4), Delete (65536), EnumerateSubKeys (8), ExecuteKey (131097), FullControl (983103), Notify (16), QueryValues (1), ReadKey (131097), ReadPermissions (131072), SetValue (2), TakeOwnership (524288), WriteKey (131078)
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

    ChangePermissions = None
    CreateLink = None
    CreateSubKey = None
    Delete = None
    EnumerateSubKeys = None
    ExecuteKey = None
    FullControl = None
    Notify = None
    QueryValues = None
    ReadKey = None
    ReadPermissions = None
    SetValue = None
    TakeOwnership = None
    value__ = None
    WriteKey = None


class RegistrySecurity(NativeObjectSecurity):
    """
    Represents the Windows access control security for a registry key. This class cannot be inherited.
    
    RegistrySecurity()
    """
    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: RegistrySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule
        
            Creates a new access control rule for the specified user, with the specified access rights, 
             access control, and flags.
        
        
            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 
             applies to.
        
            accessMask: A bitwise combination of System.Security.AccessControl.RegistryRights values specifying the 
             access rights to allow or deny, cast to an integer.
        
            isInherited: A Boolean value specifying whether the rule is inherited.
            inheritanceFlags: A bitwise combination of System.Security.AccessControl.InheritanceFlags values specifying how 
             the rule is inherited by subkeys.
        
            propagationFlags: A bitwise combination of System.Security.AccessControl.PropagationFlags values that modify the 
             way the rule is inherited by subkeys. Meaningless if the value of inheritanceFlags is 
             System.Security.AccessControl.InheritanceFlags.None.
        
            type: One of the System.Security.AccessControl.AccessControlType values specifying whether the rights 
             are allowed or denied.
        
            Returns: A System.Security.AccessControl.RegistryAccessRule object representing the specified rights for 
             the specified user.
        """
        pass

    def AddAccessRule(self, rule):
        """
        AddAccessRule(self: RegistrySecurity, rule: RegistryAccessRule)
            Searches for a matching access control with which the new rule can be merged. If none are found, 
             adds the new rule.
        
        
            rule: The access control rule to add.
        """
        pass

    def AddAuditRule(self, rule):
        """
        AddAuditRule(self: RegistrySecurity, rule: RegistryAuditRule)
            Searches for an audit rule with which the new rule can be merged. If none are found, adds the 
             new rule.
        
        
            rule: The audit rule to add. The user specified by this rule determines the search.
        """
        pass

    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: RegistrySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule
        
            Creates a new audit rule, specifying the user the rule applies to, the access rights to audit, 
             the inheritance and propagation of the rule, and the outcome that triggers the rule.
        
        
            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 
             applies to.
        
            accessMask: A bitwise combination of System.Security.AccessControl.RegistryRights values specifying the 
             access rights to audit, cast to an integer.
        
            isInherited: A Boolean value specifying whether the rule is inherited.
            inheritanceFlags: A bitwise combination of System.Security.AccessControl.InheritanceFlags values specifying how 
             the rule is inherited by subkeys.
        
            propagationFlags: A bitwise combination of System.Security.AccessControl.PropagationFlags values that modify the 
             way the rule is inherited by subkeys. Meaningless if the value of inheritanceFlags is 
             System.Security.AccessControl.InheritanceFlags.None.
        
            flags: A bitwise combination of System.Security.AccessControl.AuditFlags values specifying whether to 
             audit successful access, failed access, or both.
        
            Returns: A System.Security.AccessControl.RegistryAuditRule object representing the specified audit rule 
             for the specified user, with the specified flags. The return type of the method is the base 
             class, System.Security.AccessControl.AuditRule, but the return value can be cast safely to the 
             derived class.
        """
        pass

    def RemoveAccessRule(self, rule):
        """
        RemoveAccessRule(self: RegistrySecurity, rule: RegistryAccessRule) -> bool
        
            Searches for an access control rule with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified access rule, 
             and with compatible inheritance and propagation flags; if such a rule is found, the rights 
             contained in the specified access rule are removed from it.
        
        
            rule: A System.Security.AccessControl.RegistryAccessRule that specifies the user and 
             System.Security.AccessControl.AccessControlType to search for, and a set of inheritance and 
             propagation flags that a matching rule, if found, must be compatible with. Specifies the rights 
             to remove from the compatible rule, if found.
        
            Returns: true if a compatible rule is found; otherwise false.
        """
        pass

    def RemoveAccessRuleAll(self, rule):
        """
        RemoveAccessRuleAll(self: RegistrySecurity, rule: RegistryAccessRule)
            Searches for all access control rules with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule and, if 
             found, removes them.
        
        
            rule: A System.Security.AccessControl.RegistryAccessRule that specifies the user and 
             System.Security.AccessControl.AccessControlType to search for. Any rights, inheritance flags, or 
             propagation flags specified by this rule are ignored.
        """
        pass

    def RemoveAccessRuleSpecific(self, rule):
        """
        RemoveAccessRuleSpecific(self: RegistrySecurity, rule: RegistryAccessRule)
            Searches for an access control rule that exactly matches the specified rule and, if found, 
             removes it.
        
        
            rule: The System.Security.AccessControl.RegistryAccessRule to remove.
        """
        pass

    def RemoveAuditRule(self, rule):
        """
        RemoveAuditRule(self: RegistrySecurity, rule: RegistryAuditRule) -> bool
        
            Searches for an audit control rule with the same user as the specified rule, and with compatible 
             inheritance and propagation flags; if a compatible rule is found, the rights contained in the 
             specified rule are removed from it.
        
        
            rule: A System.Security.AccessControl.RegistryAuditRule that specifies the user to search for, and a 
             set of inheritance and propagation flags that a matching rule, if found, must be compatible 
             with. Specifies the rights to remove from the compatible rule, if found.
        
            Returns: true if a compatible rule is found; otherwise, false.
        """
        pass

    def RemoveAuditRuleAll(self, rule):
        """
        RemoveAuditRuleAll(self: RegistrySecurity, rule: RegistryAuditRule)
            Searches for all audit rules with the same user as the specified rule and, if found, removes 
             them.
        
        
            rule: A System.Security.AccessControl.RegistryAuditRule that specifies the user to search for. Any 
             rights, inheritance flags, or propagation flags specified by this rule are ignored.
        """
        pass

    def RemoveAuditRuleSpecific(self, rule):
        """
        RemoveAuditRuleSpecific(self: RegistrySecurity, rule: RegistryAuditRule)
            Searches for an audit rule that exactly matches the specified rule and, if found, removes it.
        
            rule: The System.Security.AccessControl.RegistryAuditRule to be removed.
        """
        pass

    def ResetAccessRule(self, rule):
        """
        ResetAccessRule(self: RegistrySecurity, rule: RegistryAccessRule)
            Removes all access control rules with the same user as the specified rule, regardless of 
             System.Security.AccessControl.AccessControlType, and then adds the specified rule.
        
        
            rule: The System.Security.AccessControl.RegistryAccessRule to add. The user specified by this rule 
             determines the rules to remove before this rule is added.
        """
        pass

    def SetAccessRule(self, rule):
        """
        SetAccessRule(self: RegistrySecurity, rule: RegistryAccessRule)
            Removes all access control rules with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule, and then 
             adds the specified rule.
        
        
            rule: The System.Security.AccessControl.RegistryAccessRule to add. The user and 
             System.Security.AccessControl.AccessControlType of this rule determine the rules to remove 
             before this rule is added.
        """
        pass

    def SetAuditRule(self, rule):
        """
        SetAuditRule(self: RegistrySecurity, rule: RegistryAuditRule)
            Removes all audit rules with the same user as the specified rule, regardless of the 
             System.Security.AccessControl.AuditFlags value, and then adds the specified rule.
        
        
            rule: The System.Security.AccessControl.RegistryAuditRule to add. The user specified by this rule 
             determines the rules to remove before this rule is added.
        """
        pass

    AccessRightType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the enumeration type that the System.Security.AccessControl.RegistrySecurity class uses to represent access rights.

Get: AccessRightType(self: RegistrySecurity) -> Type

"""

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AccessRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that the System.Security.AccessControl.RegistrySecurity class uses to represent access rules.

Get: AccessRuleType(self: RegistrySecurity) -> Type

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that the System.Security.AccessControl.RegistrySecurity class uses to represent audit rules.

Get: AuditRuleType(self: RegistrySecurity) -> Type

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class ResourceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the defined native object types.
    
    enum ResourceType, values: DSObject (8), DSObjectAll (9), FileObject (1), KernelObject (6), LMShare (5), Printer (3), ProviderDefined (10), RegistryKey (4), RegistryWow6432Key (12), Service (2), Unknown (0), WindowObject (7), WmiGuidObject (11)
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

    DSObject = None
    DSObjectAll = None
    FileObject = None
    KernelObject = None
    LMShare = None
    Printer = None
    ProviderDefined = None
    RegistryKey = None
    RegistryWow6432Key = None
    Service = None
    Unknown = None
    value__ = None
    WindowObject = None
    WmiGuidObject = None


class SecurityInfos(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the section of a security descriptor to be queried or set.
    
    enum (flags) SecurityInfos, values: DiscretionaryAcl (4), Group (2), Owner (1), SystemAcl (8)
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

    DiscretionaryAcl = None
    Group = None
    Owner = None
    SystemAcl = None
    value__ = None


class SemaphoreAccessRule(AccessRule):
    """
    Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.
    
    SemaphoreAccessRule(identity: IdentityReference, eventRights: SemaphoreRights, type: AccessControlType)
    SemaphoreAccessRule(identity: str, eventRights: SemaphoreRights, type: AccessControlType)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, eventRights, type):
        """
        __new__(cls: type, identity: IdentityReference, eventRights: SemaphoreRights, type: AccessControlType)
        __new__(cls: type, identity: str, eventRights: SemaphoreRights, type: AccessControlType)
        """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    SemaphoreRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rights allowed or denied by the access rule.

Get: SemaphoreRights(self: SemaphoreAccessRule) -> SemaphoreRights

"""



class SemaphoreAuditRule(AuditRule):
    """
    Represents a set of access rights to be audited for a user or group. This class cannot be inherited.
    
    SemaphoreAuditRule(identity: IdentityReference, eventRights: SemaphoreRights, flags: AuditFlags)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, eventRights, flags):
        """ __new__(cls: type, identity: IdentityReference, eventRights: SemaphoreRights, flags: AuditFlags) """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    SemaphoreRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access rights affected by the audit rule.

Get: SemaphoreRights(self: SemaphoreAuditRule) -> SemaphoreRights

"""



class SemaphoreRights(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the access control rights that can be applied to named system semaphore objects.
    
    enum (flags) SemaphoreRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031619), Modify (2), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288)
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

    ChangePermissions = None
    Delete = None
    FullControl = None
    Modify = None
    ReadPermissions = None
    Synchronize = None
    TakeOwnership = None
    value__ = None


class SemaphoreSecurity(NativeObjectSecurity):
    """
    Represents the Windows access control security for a named semaphore. This class cannot be inherited.
    
    SemaphoreSecurity()
    SemaphoreSecurity(name: str, includeSections: AccessControlSections)
    """
    def AccessRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, type):
        """
        AccessRuleFactory(self: SemaphoreSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule
        
            Creates a new access control rule for the specified user, with the specified access rights, 
             access control, and flags.
        
        
            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 
             applies to.
        
            accessMask: A bitwise combination of System.Security.AccessControl.SemaphoreRights values specifying the 
             access rights to allow or deny, cast to an integer.
        
            isInherited: Meaningless for named semaphores, because they have no hierarchy.
            inheritanceFlags: Meaningless for named semaphores, because they have no hierarchy.
            propagationFlags: Meaningless for named semaphores, because they have no hierarchy.
            type: One of the System.Security.AccessControl.AccessControlType values specifying whether the rights 
             are allowed or denied.
        
            Returns: A System.Security.AccessControl.SemaphoreAccessRule object representing the specified rights for 
             the specified user.
        """
        pass

    def AddAccessRule(self, rule):
        """
        AddAccessRule(self: SemaphoreSecurity, rule: SemaphoreAccessRule)
            Searches for a matching rule with which the new rule can be merged. If none are found, adds the 
             new rule.
        
        
            rule: The access control rule to add.
        """
        pass

    def AddAuditRule(self, rule):
        """
        AddAuditRule(self: SemaphoreSecurity, rule: SemaphoreAuditRule)
            Searches for an audit rule with which the new rule can be merged. If none are found, adds the 
             new rule.
        
        
            rule: The audit rule to add. The user specified by this rule determines the search.
        """
        pass

    def AuditRuleFactory(self, identityReference, accessMask, isInherited, inheritanceFlags, propagationFlags, flags):
        """
        AuditRuleFactory(self: SemaphoreSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule
        
            Creates a new audit rule, specifying the user the rule applies to, the access rights to audit, 
             and the outcome that triggers the audit rule.
        
        
            identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 
             applies to.
        
            accessMask: A bitwise combination of System.Security.AccessControl.SemaphoreRights values specifying the 
             access rights to audit, cast to an integer.
        
            isInherited: Meaningless for named wait handles, because they have no hierarchy.
            inheritanceFlags: Meaningless for named wait handles, because they have no hierarchy.
            propagationFlags: Meaningless for named wait handles, because they have no hierarchy.
            flags: A bitwise combination of System.Security.AccessControl.AuditFlags values that specify whether to 
             audit successful access, failed access, or both.
        
            Returns: A System.Security.AccessControl.SemaphoreAuditRule object representing the specified audit rule 
             for the specified user. The return type of the method is the base class, 
             System.Security.AccessControl.AuditRule, but the return value can be cast safely to the derived 
             class.
        """
        pass

    def RemoveAccessRule(self, rule):
        """
        RemoveAccessRule(self: SemaphoreSecurity, rule: SemaphoreAccessRule) -> bool
        
            Searches for an access control rule with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule, and with 
             compatible inheritance and propagation flags; if such a rule is found, the rights contained in 
             the specified access rule are removed from it.
        
        
            rule: A System.Security.AccessControl.SemaphoreAccessRule that specifies the user and 
             System.Security.AccessControl.AccessControlType to search for, and a set of inheritance and 
             propagation flags that a matching rule, if found, must be compatible with. Specifies the rights 
             to remove from the compatible rule, if found.
        
            Returns: true if a compatible rule is found; otherwise false.
        """
        pass

    def RemoveAccessRuleAll(self, rule):
        """
        RemoveAccessRuleAll(self: SemaphoreSecurity, rule: SemaphoreAccessRule)
            Searches for all access control rules with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule and, if 
             found, removes them.
        
        
            rule: A System.Security.AccessControl.SemaphoreAccessRule that specifies the user and 
             System.Security.AccessControl.AccessControlType to search for. Any rights specified by this rule 
             are ignored.
        """
        pass

    def RemoveAccessRuleSpecific(self, rule):
        """
        RemoveAccessRuleSpecific(self: SemaphoreSecurity, rule: SemaphoreAccessRule)
            Searches for an access control rule that exactly matches the specified rule and, if found, 
             removes it.
        
        
            rule: The System.Security.AccessControl.SemaphoreAccessRule to remove.
        """
        pass

    def RemoveAuditRule(self, rule):
        """
        RemoveAuditRule(self: SemaphoreSecurity, rule: SemaphoreAuditRule) -> bool
        
            Searches for an audit control rule with the same user as the specified rule, and with compatible 
             inheritance and propagation flags; if a compatible rule is found, the rights contained in the 
             specified rule are removed from it.
        
        
            rule: A System.Security.AccessControl.SemaphoreAuditRule that specifies the user to search for, and a 
             set of inheritance and propagation flags that a matching rule, if found, must be compatible 
             with. Specifies the rights to remove from the compatible rule, if found.
        
            Returns: true if a compatible rule is found; otherwise, false.
        """
        pass

    def RemoveAuditRuleAll(self, rule):
        """
        RemoveAuditRuleAll(self: SemaphoreSecurity, rule: SemaphoreAuditRule)
            Searches for all audit rules with the same user as the specified rule and, if found, removes 
             them.
        
        
            rule: A System.Security.AccessControl.SemaphoreAuditRule that specifies the user to search for. Any 
             rights specified by this rule are ignored.
        """
        pass

    def RemoveAuditRuleSpecific(self, rule):
        """
        RemoveAuditRuleSpecific(self: SemaphoreSecurity, rule: SemaphoreAuditRule)
            Searches for an audit rule that exactly matches the specified rule and, if found, removes it.
        
            rule: The System.Security.AccessControl.SemaphoreAuditRule to remove.
        """
        pass

    def ResetAccessRule(self, rule):
        """
        ResetAccessRule(self: SemaphoreSecurity, rule: SemaphoreAccessRule)
            Removes all access control rules with the same user as the specified rule, regardless of 
             System.Security.AccessControl.AccessControlType, and then adds the specified rule.
        
        
            rule: The System.Security.AccessControl.SemaphoreAccessRule to add. The user specified by this rule 
             determines the rules to remove before this rule is added.
        """
        pass

    def SetAccessRule(self, rule):
        """
        SetAccessRule(self: SemaphoreSecurity, rule: SemaphoreAccessRule)
            Removes all access control rules with the same user and 
             System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule, and then 
             adds the specified rule.
        
        
            rule: The System.Security.AccessControl.SemaphoreAccessRule to add. The user and 
             System.Security.AccessControl.AccessControlType of this rule determine the rules to remove 
             before this rule is added.
        """
        pass

    def SetAuditRule(self, rule):
        """
        SetAuditRule(self: SemaphoreSecurity, rule: SemaphoreAuditRule)
            Removes all audit rules with the same user as the specified rule, regardless of the 
             System.Security.AccessControl.AuditFlags value, and then adds the specified rule.
        
        
            rule: The System.Security.AccessControl.SemaphoreAuditRule to add. The user specified by this rule 
             determines the rules to remove before this rule is added.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, includeSections=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, includeSections: AccessControlSections)
        """
        pass

    AccessRightType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the enumeration that the System.Security.AccessControl.SemaphoreSecurity class uses to represent access rights.

Get: AccessRightType(self: SemaphoreSecurity) -> Type

"""

    AccessRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AccessRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that the System.Security.AccessControl.SemaphoreSecurity class uses to represent access rules.

Get: AccessRuleType(self: SemaphoreSecurity) -> Type

"""

    AuditRulesModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.

"""

    AuditRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type that the System.Security.AccessControl.SemaphoreSecurity class uses to represent audit rules.

Get: AuditRuleType(self: SemaphoreSecurity) -> Type

"""

    GroupModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.

"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.

"""

    IsDS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.

"""

    OwnerModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.

"""



class SystemAcl(CommonAcl, ICollection, IEnumerable):
    """
    Represents a System Access Control List (SACL).
    
    SystemAcl(isContainer: bool, isDS: bool, capacity: int)
    SystemAcl(isContainer: bool, isDS: bool, revision: Byte, capacity: int)
    SystemAcl(isContainer: bool, isDS: bool, rawAcl: RawAcl)
    """
    def AddAudit(self, *__args):
        """
        AddAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)
            Adds an audit rule with the specified settings to the current 
             System.Security.AccessControl.SystemAcl object. Use this method for directory object Access 
             Control Lists (ACLs) when specifying the object type or the inherited object type for the new 
             audit rule.
        
        
            auditFlags: The type of audit rule to add.
            sid: The System.Security.Principal.SecurityIdentifier for which to add an audit rule.
            accessMask: The access mask for the new audit rule.
            inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.
            propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.
            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.
            objectType: The identity of the class of objects to which the new audit rule applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the new audit rule.
        AddAudit(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule)AddAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)
            Adds an audit rule to the current System.Security.AccessControl.SystemAcl object.
        
            auditFlags: The type of audit rule to add.
            sid: The System.Security.Principal.SecurityIdentifier for which to add an audit rule.
            accessMask: The access mask for the new audit rule.
            inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.
            propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.
        """
        pass

    def RemoveAudit(self, *__args):
        """
        RemoveAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> bool
        
            Removes the specified audit rule from the current System.Security.AccessControl.SystemAcl 
             object. Use this method for directory object Access Control Lists (ACLs) when specifying the 
             object type or the inherited object type.
        
        
            auditFlags: The type of audit rule to remove.
            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.
            accessMask: The access mask for the rule to be removed.
            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.
            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.
            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.
            objectType: The identity of the class of objects to which the removed audit control rule applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the removed audit rule.
            Returns: true if this method successfully removes the specified audit rule; otherwise, false.
        RemoveAudit(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule) -> bool
        RemoveAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> bool
        
            Removes the specified audit rule from the current System.Security.AccessControl.SystemAcl object.
        
            auditFlags: The type of audit rule to remove.
            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.
            accessMask: The access mask for the rule to be removed.
            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.
            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.
            Returns: true if this method successfully removes the specified audit rule; otherwise, false.
        """
        pass

    def RemoveAuditSpecific(self, *__args):
        """
        RemoveAuditSpecific(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)
            Removes the specified audit rule from the current System.Security.AccessControl.DiscretionaryAcl 
             object. Use this method for directory object Access Control Lists (ACLs) when specifying the 
             object type or the inherited object type.
        
        
            auditFlags: The type of audit rule to remove.
            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.
            accessMask: The access mask for the rule to be removed.
            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.
            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.
            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.
            objectType: The identity of the class of objects to which the removed audit control rule applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the removed audit rule.
        RemoveAuditSpecific(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule)RemoveAuditSpecific(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)
            Removes the specified audit rule from the current System.Security.AccessControl.DiscretionaryAcl 
             object.
        
        
            auditFlags: The type of audit rule to remove.
            sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.
            accessMask: The access mask for the rule to be removed.
            inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.
            propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.
        """
        pass

    def SetAudit(self, *__args):
        """
        SetAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid)
            Sets the specified audit rule for the specified System.Security.Principal.SecurityIdentifier 
             object. Use this method for directory object Access Control Lists (ACLs) when specifying the 
             object type or the inherited object type.
        
        
            auditFlags: The audit condition to set.
            sid: The System.Security.Principal.SecurityIdentifier for which to set an audit rule.
            accessMask: The access mask for the new audit rule.
            inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.
            propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.
            objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.
            objectType: The identity of the class of objects to which the new audit rule applies.
            inheritedObjectType: The identity of the class of child objects which can inherit the new audit rule.
        SetAudit(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule)SetAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)
            Sets the specified audit rule for the specified System.Security.Principal.SecurityIdentifier 
             object.
        
        
            auditFlags: The audit condition to set.
            sid: The System.Security.Principal.SecurityIdentifier for which to set an audit rule.
            accessMask: The access mask for the new audit rule.
            inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.
            propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.
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

    @staticmethod # known case of __new__
    def __new__(self, isContainer, isDS, *__args):
        """
        __new__(cls: type, isContainer: bool, isDS: bool, capacity: int)
        __new__(cls: type, isContainer: bool, isDS: bool, revision: Byte, capacity: int)
        __new__(cls: type, isContainer: bool, isDS: bool, rawAcl: RawAcl)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


