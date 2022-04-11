# Python Inertface for functiosns
With this tool, you can now attach XML file tags to Python functions.
To use, copy the pyifunc.py and NCommands.py files to your project.

## Use PyIFunc
First import the pyfunc.py
```python
import pyifunc
```

next create a xml file for your components and read the content
you can use read_file() function!
```python
uicode = pyifunc.read_file('ui.xml')
```

Now is the time to create desired functions, You can do nothing but return a value. Like changing a database
If you want your component to accept prop, you must set **one** input for your function.
You can use this input to access given props.
```python
def say_hello(data):
    return f"Hello {data['@name']} {data['@lastname']}"
```

Next you need to create a interface for connect components to functions
```python
api_component = {
    'Sayhello': say_hello,
    # ...
}
```

And end of all:

pyifunc.write_file('execute.txt', pyifunc.execute(uicode, api_components))

Now you can use the SayHello tag in the xml file and do the processing with Python.
```xml
<Sayhello name="Mohammad safa" lastname="kamali" />
```

## Notes:
- This tool has problems and is very sensitive. For example, there must be a space before /.

- Since this project was a practice project for me, this tool may not be suitable for large projects.

- This project is completely free and you can even use it for commercial projects and modify it. Ideas and changes are welcome.