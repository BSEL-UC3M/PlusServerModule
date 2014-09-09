__author__ = 'E. Marinetto'
# Importing need files
from Plus import Device as Plus
from xml.etree import ElementTree


class Tracker(Plus.Device):

    """
    Class that represents a Tracker Device in Plus Library

    A Device can be:
        - Polaris System
    """

    def __init__(self):
        """
        Void Initialization
        """
        self.id = 'TrackerDevice'
        """:param id: String with the id name for the device """
        self.codeXmlDevice = self.generatexml()
        """:param codeXmlServer:  XML code for Device """

    def generatexml(self):
        """
        Get the code configuration for the PlusServer app
        """
        codeXmlDevice = ElementTree.Element('Device')
        codeXmlDevice.set('Id', self.id)

        comment = ElementTree.Comment('Generated by Plus Module (Marinetto)')
        codeXmlDevice.append(comment)

        return codeXmlDevice