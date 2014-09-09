__author__ = 'E. Marinetto'

# Importing need files
from Plus import Tracker as Plus
from xml.etree import ElementTree
from Plus import PrettyXMLPrint

class TrackerPolaris(Plus.Tracker):

    """
    Class that represents a Polaris Tracking Device

    Example:

		<Device
			  Id="TrackerDevice"
			  Type="PolarisTracker"
			  SerialPort="6"
			  BaudRate="115200"
			  ToolReferenceFrame="Tracker" >
			  <DataSources>
				<DataSource Type="Tool" Id="Pointer" RomFile="Z:/Development/Plus_connect_Polaris/Tools/100001.rom" AveragedItemsForFiltering="20" BufferSize="500"  />
			  </DataSources>
			  <OutputChannels>
				<OutputChannel Id="TrackerStream" >
				  <DataSource Id="Pointer"/>
				</OutputChannel>
			  </OutputChannels>
		</Device>

    """

    def __init__(self):
        """
        Void Initialization
        """
        self.id = 'TrackerDevicePolaris'
        self.type = 'PolarisTracker'
        self.serialport = 0
        self.boundrate = 115200
        self.toolreferenceframe = 'Tracker'
        self.toolslist = []
        self.outputchannelname = 'TrackerStream'

        self.codeXmlDevice = self.generatexml()
        """:param codeXmlServer:  XML code for Device """

    def generatexml(self):
        """
        Get the code configuration for the PlusServer app
        """
        codeXmlDevice = ElementTree.Element('Device')
        codeXmlDevice.set('Id', 'TrackerDevicePolaris')
        codeXmlDevice.set('Type', 'Tracker')
        codeXmlDevice.set('SerialPort', str(self.serialport))
        codeXmlDevice.set('BaudRate', str(self.boundrate))
        codeXmlDevice.set('ToolReferenceFrame', self.toolreferenceframe)

        """
            Add the Data Sources
        """
        DataSources = ElementTree.SubElement(codeXmlDevice, 'DataSources')
        for tool in self.toolslist:
            DataSources.append(tool.generatexml())

        """
            Add the Output Channels
        """
        OuputChannels = ElementTree.SubElement(codeXmlDevice, 'OutputChannels')
        for tool in self.toolslist:
            id = tool.id
            DataSource = ElementTree.SubElement(OuputChannels, 'DataSource')
            DataSource.set('Id', id)

        return codeXmlDevice


    def addtool(self, tool):
        self.toolslist.append(tool)
        self.codeXmlDevice = self.generatexml()


    def serialport(self):
        return self.serialport

    def serialport(self, value):
        self.serialport = value

    def boundrate(self):
        return self.boundrate

    def boundrate(self, value):
        self.boundrate = value

    def toolreferenceframe(self):
        return self.toolreferenceframe

    def toolreferenceframe(self, value):
        self.toolreferenceframe = value

    def outputchannelname(self):
        return self.outputchannelname

    def outputchannelname(self, value):
        self.outputchannelname = value


# TEST CODE

# Create a Tracker
mytracker = TrackerPolaris()
# Create a Tool and add to tracker
from Plus import TrackerPolarisTool
mytool = TrackerPolarisTool.TrackerPolarisTool()
mytracker.addtool(mytool)

# print the generated xml file
mytracker.prettyprint()