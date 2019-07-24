import os

PATHS = [
    # | Local Binaries
  'C:\\dev\\Trancon.WmsPro\\Source\\Wms.WarehouseServerConsole\\Source\\bin\\Debug'
    ]

ASSEMBLIES = [
    # | BOXwise
	 'Wms.RemotingImplementation',
	'Wms.RemotingObjects',
	'Wms.RemotingInterface',
	'Wms.SharedInfra',
	'Wms.EdiMessaging',

    # | System
    'System',
    #'System.Drawing',
    #'System.Windows.Forms',
    ]

BUILTINS = [
    'clr',
    ]

ASSEMBLIES.extend(BUILTINS)
ASSEMBLIES.sort()
