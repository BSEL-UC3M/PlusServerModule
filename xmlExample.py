from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


DataSource = ElementTree.Element('DataSource')

#DataSource.set('Type', 7)
DataSource.set('Id', 'asdfaf')
DataSource.set('RomFile', 'asdfasdf')
#DataSource.set('AveragedItemsForFiltering', 89)
#DataSource.set('BufferSize', 500)

print prettify(DataSource)