import serial, time


class light_control(object):
    def __init__(self, comport, baudrate, timeout):
        self.comport = comport
        self.baudrate = baudrate
        self.timeout = timeout
        self.s = serial.Serial(comport, baudrate, timeout=timeout)

    def enable(self):
        if self.s.is_open:
            self.s.write("@00F01400DB\r\n".encode())
            i = self.s.readlines()
            print("Message from LED LIGHT CONTROLLER: ")
            print(i)
            if i == "":
                i = self.s.readlines()
            else:
                self.s.write("@00L11D\r\n".encode())
                _ = self.s.readlines()

    def disable(self):
        if self.s.is_open:
            self.s.write("@00F00000D6\r\n".encode())
            i = self.s.readlines()
            print("Message from LED LIGHT CONTROLLER: ")
            print(i)
            if i == "":
                i = self.s.readlines()
            else:
                self.s.write("@00L11D\r\n".encode())
                _ = self.s.readlines()
            # print(_)

    def open(self):
        if not self.s.is_open:
            self.s.open()

    def close(self):
            self.s.close()

def test_light_control():
    s = light_control("COM5", 38400, 1)
    s.open()
    s.enable()
    time.sleep(3)
    s.disable()

if __name__ == "__main__":
    test_light_control()
