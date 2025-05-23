# 求任意三个数的乘积
def mul(a,b,c):
    print(a*b*c)

# 根据不同的用户名显示不同的欢迎信息   
def welcome(username):
    print('欢迎',username,'光临')

# mul(1,2,3)   
# welcome('孙悟空') 

# 定义一个函数
# 定义形参时，可以为形参指定默认值
# 指定了默认值以后，如果用户传递了参数则默认值没有任何作用
#   如果用户没有传递，则默认值就会生效
def fn(a = 5 , b = 10 , c = 20):
    print('a =',a)
    print('b =',b)
    print('c =',c)

# fn(1 , 2 , 3)
# fn(1 , 2)
# fn()

# 实参的传递方式
# 位置参数
# 位置参数就是将对应位置的实参复制给对应位置的形参
# 第一个实参赋值给第一个形参，第二个实参赋值给第二个形参 。。。
# fn(1 , 2 , 3)

# 关键字参数
# 关键字参数，可以不按照形参定义的顺序去传递，而直接根据参数名去传递参数
# fn(b=1 , c=2 , a=3)
# print('hello' , end='')  # end表示结束符号参数，默认值为\n
# 位置参数和关键字参数可以混合使用
# 混合使用关键字和位置参数时，必须将位置参数写到前面
# fn(1,c=30)

def fn2(a):
    print('a =',a)

# 函数在调用时，解析器不会检查实参的类型
# 实参可以传递任意类型的对象
b = 123
b = True
b = 'hello'
b = None
b = [1,2,3]

# fn2(b)    
fn2(fn)

def fn3(a , b):
    print(a+b)

# fn3(123,"456")

def fn4(a):
    # 在函数中对形参进行重新赋值，不会影响其他的变量
    # a = 20
    # a是一个列表，尝试修改列表中的元素
    # 如果形参执行的是一个对象，当我们通过形参去修改对象时
    #   会影响到所有指向该对象的变量
    a[0] = 30
    print('a =',a,id(a))

c = 10   
c = [1,2,3] 

# fn4(c)
# fn4(c.copy())
# fn4(c[:])

# print('c =',c,id(c))
