"""Listener code for the IOT device."""

import socket
import threading


class ListeningThing:
    """This is a socket listening class."""

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.state = "off"

    def ltOpen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, PORT))
            s.listen()

            xids = 0
            while True:
                try:
                    conn, addr = s.accept()
                    xids += 1
                    start_new_thread(self.ltHandler, (conn, addr, xids))
                except KeyboardInterrupt as ki:
                    break

    def getState(self):
        return self.state

    def switchState(self):
        self.state = "off" if self.state == "on" else "on"
        return self.getState()

    def ltHandler(self, conn, addr, xids):
        data = conn.recv(1024)
        if data:
            sdata = str(data).lower()
            if sdata == "state":
                xstate = self.getState()
            elif sdata == "switch":
                tstate = self.getState()
                nstate = self.switchState()
                xstate = f"{tstate} => {nstate}"
            else:
                xstate = "Bad command error."
            conn.sendall(xstate)
        conn.close()
