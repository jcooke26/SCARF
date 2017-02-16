#SCARF frontend
#!/usr/bin/python3

from scripts/scarf_xml_parser.py import parseXmlToScarf

scarfList = parseXmlToScarf()

print(scarfList)