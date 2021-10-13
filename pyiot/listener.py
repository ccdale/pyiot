"""Listener code for the IOT device."""

import socket
import threading


class ListeningThing:
    """This is a socket listening class."""

    defaultport = 11223
    defaulthost = "localhost"
    defaultstate = "off"

    def __init__(self, host=None, port=None):
        self._host = host if host is not None else self.defaulthost
        self._port = self.defaultport if port is None else port
        self._state = self.defaultstate
        print(
            f"LT has been initialised host: {self._host}, port: {self._port} and state: {self._state}"
        )

    def ltOpen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self._host, PORT))
            s.listen()

            xids = 0
            while True:
                try:
                    conn, addr = s.accept()
                    xids += 1
                    start_new_thread(self._ltHandler, (conn, addr, xids))
                except KeyboardInterrupt as ki:
                    break

    def getState(self):
        return self._state

    def switchState(self):
        self._state = "off" if self._state == "on" else "on"
        return self.getState()

    def _ltHandler(self, conn, addr, xids):
        data = conn.recv(1024)
        if data:
            sdata = data.decode().lower()
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
