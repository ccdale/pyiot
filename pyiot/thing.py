class Thing:
    """This is the docstring for the Thing Class"""

    def __init__(self, name="thing", xtype="thing"):
        self.name = name
        self.xtype = xtype
        self.status = True

    def __repr__(self):
        return f"Thing(name={self.name}, xtype={self.xtype})"

    def health(self):
        return self.status

    def listen(self):
        pass

    def send(self):
        pass


class WindowSensor(Thing):
    def __init__(self, name="wsensor", xtype="sensor"):
        super().__init__(name=name, xtype=xtype)

    def __repr__(self):
        return f"WindowSensor(name={self.name}, xtype={self.xtype})"

    def wopen(self):
        self.status = False

    def wclose(self):
        self.status = True
