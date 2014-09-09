__author__ = 'E. Marinetto'

# Importing need files
from Plus import USProbe as Plus
from xml.etree import ElementTree
from Plus import PrettyXMLPrint

class USProbeIntersonNewSDK(Plus.USProbe):

    """
    Class that represents a Interson UBS Probe New SDK

    Example:

		<Device
          Id="VideoDeviceIntersonNewSDK"
          Type="IntersonSDKCxxVideo"
          RfDecimation="0"
          PulseVoltage="20"
          AcquisitionRate="12"
          FrequencyMhz="5.0">
            <DataSources>
                <DataSource Type="Video" Id="BmodeVideoIntersonNewSDK" PortName="B" PortUsImageOrientation="UF" />
                <DataSource Type="Video" Id="RfVideoIntersonNewSDK" PortName="Rf" PortUsImageOrientation="FU" />
            </DataSources>
            <OutputChannels>
                <OutputChannel Id="BmodeVideoStreamIntersonNewSDK" VideoDataSourceId="BmodeVideoIntersonNewSDK">
                <OutputChannel Id="RfVideoStreamIntersonNewSDK" VideoDataSourceId="RfVideoIntersonNewSDK" />
                    <RfProcessing>
                        <ScanConversion
                          TransducerName="Interson USB 99-5903"
                          TransducerGeometry="CURVILINEAR"
                          RadiusStartMm="12.4"
                          RadiusStopMm="105.5"
                          ThetaStartDeg="-45.0"
                          ThetaStopDeg="45.0"
                          OutputImageSizePixel="800 600"
                          TransducerCenterPixel="400 50"
                          OutputImageSpacingMmPerPixel="0.20 0.20" />
                    </RfProcessing>
                </OutputChannel>
            </OutputChannels>
        </Device>

    """

    def __init__(self):
        """
        Void Initialization
        """
        self.id = 'VideoDeviceIntersonNewSDK'
        self.type = 'IntersonSDKCxxVideo'
        self.acquisitionrate = 15
        self.frequencymhz = 7.5
        self.codeXmlDevice = self.generatexml()


    def generatexml(self):
        """
        Get the code configuration for the PlusServer app
        """
        codeXmlDevice = ElementTree.Element('Device')
        codeXmlDevice.set('Id', self.id)
        codeXmlDevice.set('Type', 'IntersonSDKCxxVideo')
        codeXmlDevice.set('AcquisitionRate', str(self.acquisitionrate))
        codeXmlDevice.set('FrequencyMhz', str(self.frequencymhz))

        """
            Add the Data Sources
        """
        DataSources = ElementTree.SubElement(codeXmlDevice, 'DataSources')

        DataSourceBMode = ElementTree.SubElement(DataSources, 'DataSource')
        DataSourceBMode.set('Type','Video')
        DataSourceBMode.set('Id','BmodeVideoIntersonNewSDK')
        DataSourceBMode.set('PortName','B')
        DataSourceBMode.set('PortUsImageOrientation','UF')

        DataSourceRfMode = ElementTree.SubElement(DataSources, 'DataSource')
        DataSourceRfMode.set('Type','Video')
        DataSourceRfMode.set('Id','RfVideoIntersonNewSDK')
        DataSourceRfMode.set('PortName','Rf')
        DataSourceRfMode.set('PortUsImageOrientation','FU')

        """
            Add the Output Channels
        """
        OuputChannels = ElementTree.SubElement(codeXmlDevice, 'OutputChannels')

        OutputChannelBMode = ElementTree.SubElement(OuputChannels, 'OutputChannel')
        OutputChannelBMode.set('Id', 'BmodeVideoStreamIntersonNewSDK')
        OutputChannelBMode.set('VideoDataSourceId','BmodeVideoIntersonNewSDK')

        OutputChannelRfMode = ElementTree.SubElement(OuputChannels, 'OutputChannel')
        OutputChannelRfMode.set('Id', 'RfVideoStreamIntersonNewSDK')
        OutputChannelRfMode.set('VideoDataSourceId','RfVideoIntersonNewSDK')

        """
            Add the filter for Rf Images
        """

        RfProcessing = ElementTree.SubElement(OuputChannels, 'RfProcessing')
        ScanConversion = ElementTree.SubElement(RfProcessing, 'ScanConversion')
        ScanConversion.set('TransducerName','Interson USB 99-5903')
        ScanConversion.set('TransducerGeometry','CURVILINEAR')
        ScanConversion.set('RadiusStartMm','12.4')
        ScanConversion.set('RadiusStopMm','105.5')
        ScanConversion.set('ThetaStartDeg','-45.0')
        ScanConversion.set('ThetaStopDeg','45.0')
        ScanConversion.set('OutputImageSizePixel','800 600')
        ScanConversion.set('TransducerCenterPixel','400 50')
        ScanConversion.set('OutputImageSpacingMmPerPixel','0.20 0.20')

        return codeXmlDevice








# TEST CODE

# Create a Tracker
myprobe = USProbeIntersonNewSDK()

# print the generated xml file
myprobe.prettyprint()