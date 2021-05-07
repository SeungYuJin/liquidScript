from Hooks import Hooks, Hook

"""
    By default, as per:

    RequiredAttrs = ['Author', 'Description', 'Hooks']
    RequiredFuncs = ['onLoad', 'onUnload']

    in ScriptManager.py, this is bare minimum, what a plugin
    should look like. This may change in the future.
"""

class MyFirstPlugin:
    Author = "Seung"
    Description = "Just a test plugin. Nothing Special!"
    Hooks = Hooks() 
    
    def __init__(self):
        pass
    
    def onLoad(self):
        print("Plugin Loaded!")

    def onUnload(self):
        print("Plugin Unloaded!")

    def testFunc(self):
        passx`