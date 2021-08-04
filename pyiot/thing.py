class Thing:
    def __init__(self, name="thing", xtype="thing"):
        self.name = name
        self.xtype = xtype

    def __repr__(self):
        return f"<Thing(name={self.name}, xtype={self.xtype})>"

    def status(self):
        return True


class WindowSensor(Thing):
    def __init__(self, name="wsensor", xtype="sensor"):
        super().__init__(name=name, xtype=xtype)

    def __repr__(self):
        return f"<WindowSensor(name={self.name}, xtype={self.xtype})>"
