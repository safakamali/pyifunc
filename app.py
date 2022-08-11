# this file is a example use for pyifunc
# import pyifunc
import pyifunc


# get the ui code in ui.xml
uicode = pyifunc.read_file('ui.xml')

# Create functions to connect to xml
# return given data in prop string
def ShowText(string):
    return string

# return a text for hello to user
def SayHello(name, lastname):
    return f"Hello {name} {lastname}"

# ../ Important \..
# make a interface for connect the component to functions
api_components = {
    'Text': ShowText,
    'Sayhello': SayHello
}

# write the result in the execute.txt file
pyifunc.write_file('execute.txt', pyifunc.execute(uicode, api_components))

# done! you can see result in execute.txt file