import os

class Connection:
    def __init__(self, timeout=10):
        self.__connected = False
        self.__timeout = timeout
        self.__connections = []

        self.__AvailableConnections()
        

    @property
    def Connected(self):
        self.__ConnectionState()
        return self.__connected


    def __AvailableConnections(self):
        path = "/sys/class/net"

        for content in os.listdir(path):
            if os.path.isdir(content):
                self.__connections.append(content)


    def __ConnectionState(self):
        for connection in self.__connections:
            try:
                state = open(connection).read()

                if state:
                    if int(state) == 1:
                        self.__connected = True
                        return

            except OSError:
                self.__connected = False


    def TryConnection(self):
        self.__ConnectionState()

        for i in range(self.__timeout):
            if self.__connected:
                return self.__connected

            self.__ConnectionState()
            
                    
        

    

                

    
