class ScriptObject:

    def __init__(self, scriptName, script, functions, variables, integrity, classInstance, classImports):
        self.ScriptName = scriptName
        self.ClassRef = script
        self.ClassImports = classImports
        self.Functions = functions
        self.Variables = variables
        self.Integrity = integrity
        self.INSTANCE = classInstance

    def _scriptInfo(self):
        print("[~] Script File: ", self.ScriptName)
        print("[~] Script Class: ", self.ClassRef)
        print("[~] Class Imports: ", self.ClassImports)
        print("[~] Functions: ", self.Functions)
        print("[~] Variables", self.Variables)
        print("[~] Verified Valid: ", self.Integrity)
        print("[~] Instance: ", self.INSTANCE)