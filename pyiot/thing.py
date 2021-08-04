class Thing:
    def __init__(self, name="thing", xtype="thing"):
        self.name = name
        self.xtype = xtype

    def __repr__(self):
        return f"<Thing(name={self.name}, xtype={self.xtype})>"

    def status(self):
        return True
