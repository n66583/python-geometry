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
    def diamond(self, side, angle):
        self.side = side
        self.angle = angle
        t.lt(180 - angle + (angle / 2))
        t.fd(self.side)
        t.lt(self.angle)
        t.fd(self.side)
        t.lt(180 - angle)
        t.fd(self.side)
        t.lt(self.angle)
        t.fd(self.side)
    def para(self, side1, side2, angle):
        self.side1 = side1
        self.side2 = side2
        self.angle = angle
        t.lt(angle)
        t.fd(self.side1)
        t.lt(180 - angle)
        t.fd(self.side2)
        t.lt(angle)
        t.fd(self.side1)
        t.lt(180 - angle)
        t.fd(self.side2)
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
    def os_node(self):
        print(platform.node())
    def os_release(self):
        print(platform.release())
    def os_info(self):
        #print(platform.uname())
        x = str(platform.uname())
        
        print(x[13:-2] + ", processor='"+platform.processor()+"'")
        
geometry = MyClass()
