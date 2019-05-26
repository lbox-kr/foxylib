from foxylib.tools.collections.collections_tools import l_singleton2obj
from foxylib.tools.file.file_tools import FileToolkit
import xml.etree.ElementTree as ET

class XMLToolkit:
    @classmethod
    def down(cls, root, tags):
        node = root

        for tag in tags:
            node = node.find(tag)
            if not node: return node

        return node

    @classmethod
    def down2text(cls, root, tags):
        node = root

        for tag in tags:
            node = node.find(tag)
            if not node: return node

        return node.text

    @classmethod
    def down2uniq(cls, root, tags):
        node = root
        for tag in tags:
            children = node.findall(tag)
            if not children:
                return None

            node = l_singleton2obj(children)
        return node

    @classmethod
    def x2text(cls, node): return node.text

    @classmethod
    def filepath2xml(cls, filepath):
        utf8 = FileToolkit.filepath2utf8(filepath)
        xml = ET.fromstring(utf8)
        return xml