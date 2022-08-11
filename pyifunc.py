import xmltodict, json

def read_file(file_addr):
    file = open(file_addr, 'r')
    data = file.read()
    file.close()
    return data

def write_file(file_addr, data):
    file = open(file_addr, 'w')
    file.write(data)
    file.close()

    return data

# |========                               ========|
# |=========== Pyifunc Main processing ===========|
# |========                               ========|
def execute(uicode: str, component_api):

    # convert xml to json
    json_uicode = xmltodict.parse(uicode)['body']
    json_uicode = json.dumps(json_uicode)
    json_uicode = json.loads(json_uicode)

    # print(json_uicode)
    # print(type(json_uicode))


    result = uicode.replace("<body>", "").replace("</body>", "")

    for component in json_uicode:
        a = "" # sorry ! (;
        b = "" # sorry ! (;
        thiscomponent_xml = ""
        component_props = json_uicode[component]

        for prop in component_props:
            prop = prop
            # print(prop)
            prop2 = prop.replace('@', '')
            a += f'{prop2}="{component_props[prop]}" '
            b += f'{prop2}="{component_props[prop]}", '
        
        thiscomponent_xml = f'<{component} {a}/>'
        json.dumps(component_props)


        component_result = eval(f"component_api[component]({b})")

        result = result.replace(thiscomponent_xml, component_result)

        # print(thiscomponent_xml)
        # print(component_api[component](component_props))
        # result = result.replace(thiscomponent_xml, str(component_api[component](component_props)))
    

    return str(result).replace('\n', "", 1)