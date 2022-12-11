import turtle as t
import platform

class MyClass():
    def rect(self, x, y):
        self.x = x
        self.y = y
        for i in range(2):
            t.fd(self.x)
            t.lt(90)
            t.fd(self.y)
            t.lt(90)
    def square(self, leng):
        self.leng = leng
        for j in range(4):
            t.fd(self.leng)
            t.lt(90)
    def circle(self, r):
        self.r = r
        t.circle(self.r)
    def triangle(self, side):
        self.side = side
        for i in range(3):
            t.fd(self.side)
            t.lt(120)
    def self_triangle(self):
        print("Error: We don't have self triangle!")
    def diamond(self, side, angle_s1, angle_s2):
        self.side = side
        self.angle_s1 = 90 - angle_s1
        self.angle_s2 = 90 - angle_s2
        for g in range(2):
            t.lt(self.angle_s1)
            t.fd(self.side)
            t.lt(180 - angle_s2)
            t.fd(side)
    def n_star(self, side_num, side_len, angles):
        self.side_num = side_num
        self.side_len = side_len
        self.angles = 180 - angles
        for i in range(self.side_num-1):
            t.fd(self.side_len)
            t.lt(self.angles)
        t.home()
    def n_sides(self, side_num, side_len):
        self.side_num = side_num
        self.side_len = side_len
        angles = ((side_num-2)*180)/side_num
        for i in range(self.side_num):
            t.fd(self.side_len)
            t.lt(180-angles)
    def os(self):
        print(platform.system())
    def os_processor(self):
        print(platform.processor())
    def os_version(self):
        print(platform.version())
    def os_machine(self):
        print(platform.machine())
    def os_username(self):
        print(platform.node())
    def os_info(self):
        print(platform.uname())
        
geometry = MyClass()
