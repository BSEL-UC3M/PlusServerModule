__author__ = 'E. Marinetto'

# Importing need files
from xml.etree import ElementTree
from Plus import PrettyXMLPrint


class TrackerPolarisTool(object):

    """
    Class that represents a Polaris Tracking Tool

    Example:
		<DataSource Type="Tool" Id="Pointer" RomFile="Z:/Development/Plus_connect_Polaris/Tools/100001.rom" AveragedItemsForFiltering="20" BufferSize="500"  />
    """

    def __init__(self):
        """
        Void Initialization
        """
        self.type('Tool')
        self.id('ToolName')
        self.romfilepath('Where the *.rom file is placed')
        self.averageditemsforfiltering(20)
        self.buffersize(500)
        self.xmlDataSource = self.generatexml()

    def generatexml(self):
        """
        Get the code configuration for the PlusServer app
        """
        DataSource = ElementTree.Element('DataSource')

        DataSource.set('Type', self.id)
        DataSource.set('Id', self.id)
        DataSource.set('RomFile', self.romfilepath)
        DataSource.set('AveragedItemsForFiltering', str(self.averageditemsforfiltering))
        DataSource.set('BufferSize', str(self.buffersize))

        return DataSource

    def prettyprint(self):
        print PrettyXMLPrint.prettify(self.xmlDataSource)


    def type(self):
        return self.type

    def type(self, value):
        self.type = value

    def id(self):
        return self.id

    def id(self, value):
        self.id = value

    def romfilepath(self):
        return self.romfilepath

    def romfilepath(self, value):
        self.romfilepath = value

    def averageditemsforfiltering(self):
        return self.averageditemsforfiltering

    def averageditemsforfiltering(self, value):
        self.averageditemsforfiltering = value

    def buffersize(self):
        return self.buffersize

    def buffersize(self, value):
        self.buffersize = value

