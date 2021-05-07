class Hook:

    def __init__(self, hookID, _regex=False):

        self.Key = hookID #original ID
        self.GUID = ""
        self.Hooked = False
        self.Props = {}
        self.PTR = None

        if _regex:
            self.Props['regex'] = True #Regex not implemented yet.

    def Fire(self, *args, **kwargs):
        if self.PTR:
            return self.PTR(self, *args, **kwargs)
        return None

class Hooks:

    def __init__(self):
        self.Hooks = {}

    def __getitem__(self, event):
        return self.Hooks[event] if self.HasHook(event) else None

    def HasHook(self, key):
        return True if key in self.Hooks.keys() else False
    
    def Unregister(self, events):
        for event in events:
            del self.Hooks[event]

    def Register(self, *events):
        def hook_registered(f):
            for event in events:
                if not self.HasHook(event):
                    _hook = Hook(event)
                    self.Hooks[event] = _hook
                    self.Hooks[event].PTR = f

            return f
        return hook_registered

