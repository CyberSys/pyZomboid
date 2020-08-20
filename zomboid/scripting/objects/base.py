class BaseScriptObject:
    module = None # cant use hints due to import recursion. ..module.ScriptModue

    def Load(self, name, data):
        pass

    def getModule(self):
        return self.module

