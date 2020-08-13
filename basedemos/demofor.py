print("hello from hogwarts")

words = ['cat', 'window', 'denfenestrate']
for w in words:
    print(w)

for i in range(3):
    print(i)

for i in range(len(words)):
    print(i)
    print(words[i])


# 变长参数:*args表示以元组传入参数，**kwargs表示以字典传入参数
def fun(*args):
    print("hogwarts")
    print(args)
    print(len(args))


fun()

fun(1)

fun('a', 'b')


def fun2(a, b, c):
    print(a+b+c)


a = [1, 2, 3]
# 打印出对象的方法
print(dir(a))

fun2(1, 2, 3)
fun2(a[0], a[1], a[2])

#以下是自动以fun2(a[0], a[1], a[2])形式传入参数
fun2(*a)

