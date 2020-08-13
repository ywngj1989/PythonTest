class A:
    # 全局变量
    t = 1

    # 实例方法
    def m_a(self):
        a = 1
        print("A.m_a")
        print(a)

    # 类方法
    @classmethod
    def ca(cls):
        print("这是一个类方法，可以直接用类名点方法名进行访问")
        print(cls.t)

class B:
    def m_b(self):
        print("B.m_b")


print(A)
print(B)


a1 = A()
a2 = A()
print(a1.t)
print(a2.t)

a1.t = 2
print(a1.t)
print(a2.t)


a2.t = 3
print(a1.t)
print(a2.t)
print(A.t)

A.t = 4
print(a1.t)
print(a2.t)
print(A.t)

# 类名点方法名
A.ca()
