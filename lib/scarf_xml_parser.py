#Python XML Transformer
#!/usr/bin/python3

import xml.etree.ElementTree as etree

def parseXmlToScarf():
	
	#dictionary to hold
	scarfList = []

	tree = etree.parse('templates/irap_template.xml')
	template = tree.getroot()

	for control in template:
		#print(control[0].text)
		tempDict = {'id' : control[0].text}
		for element in control:
			if element.tag != 'id':
				#print(element.text.strip())
				tempDict[str(element.tag)] = element.text.strip()
		scarfList.append(tempDict)

	return(scarfList)

scarfList = parseXmlToScarf()
print(scarfList)