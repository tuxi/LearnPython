# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 下午10:07
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : closure.py
# @Software: PyCharm

# 闭包
'''
闭包(closure)是函数式编程的重要的语法结构。
函数式编程是一种编程范式 (而面向过程编程和面向对象编程也都是编程范式)。
在面向过程编程中，我们见到过函数(function)；在面向对象编程中，我们见过对象(object)。
函数和对象的根本目的是以某种逻辑方式组织代码，并提高代码的可重复使用性(reusability)。
闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。

# 闭包函数的示例
'''

def test(num):
    print('----1----')
    def test_in(num1):
        print('----2----')
        print(num + num1)
        print('----3----')
    return test_in

# 使用t变量接受返回的函数
t = test(100)
# 执行内部函数
t(2)
t(200)

def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))

'''
一般情况下，在我们认知当中，如果一个函数结束，
函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。
但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，
就把这个临时变量绑定给了内部函数，然后自己再结束。
'''

# outer是外函数 a和b都是外函数的临时变量
def outer(a):
    b = 10
    #inner是内函数
    def inner():
        print(a+b)
    # 外函数的赶回值时内函数的引用
    return inner

# if __name__ == '__main__':
#     # 我们调用外函数传入参数5
#     # 此时外函数两个临时变量 a是5 b是10， 并创建了内函数，然后把内函数的引用返回存到了demo
#     # 外函数结束的时候发现内函数将会用到自己的临时变量，这两个临时变量不会释放，会绑定给这个内部函数
#     demo = outer(5)
#     # 调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
#     # demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
#     demo() # 15
#     demo2 = outer(7)
#     demo2() # 17

'''
外函数把临时变量绑定给内函数：

按照我们正常的认知，一个函数结束的时候，会把自己的临时变量都释放还给内存，之后变量都不存在了。
一般情况下，确实是这样的。但是闭包是一个特别的情况。
外部函数发现，自己的临时变量会在将来的内部函数中用到，自己在结束的时候，返回内函数的同时，会把外函数的临时变量送给内函数绑定在一起。
所以外函数已经结束了，调用内函数的时候仍然能够使用外函数的临时变量。
在我编写的实例中，我两次调用外部函数outer,分别传入的值是5和7。
内部函数只定义了一次，我们发现调用的时候，内部函数是能识别外函数的临时变量是不一样的。
python中一切都是对象，虽然函数我们只定义了一次，但是外函数在运行的时候，
实际上是按照里面代码执行的，外函数里创建了一个函数，我们每次调用外函数，它都创建一个内函数，虽然代码一样，但是却创建了不同的对象，
并且把每次传入的临时变量数值绑定给内函数，再把内函数引用返回。虽然内函数代码是一样的，
但其实，我们每次调用外函数，都返回不同的实例对象的引用，他们的功能是一样的，但是它们实际上不是同一个函数对象。
'''

# 闭包中内函数修改外函数局部变量：
'''
在基本的python语法当中，一个函数可以随意读取全局数据，但是要修改全局数据的时候有两种方法:1 global 声明全局变量 2 全局变量是可变类型数据的时候可以修改
'''
'''
在闭包内函数也是类似的情况。在内函数中想修改闭包变量（外函数绑定给内函数的局部变量）的时候：
1 在python3中，可以用nonlocal 关键字声明 一个变量， 表示这个变量不是局部变量空间的变量，需要向上一层变量空间找这个变量。
2 在python2中，没有nonlocal这个关键字，我们可以把闭包变量改成可变类型数据进行修改，比如列表。
'''

# 修改闭包变量的示例
# outer1是外部函数 a和b 都是外部函数的临时变量
def outer1(a):
    b = 10  # a 和 b都是临时变量
    c = [a] # 这里对应修改闭包变量的方法2
    # inner是内函数
    def inner():
        # 内函数中想修改闭包变量
        # 方法1 nonlocal关键字声明
        nonlocal b
        b += 1
        # 方法2 把闭包变量修改成可变数据类型，比如列表
        c[0] += 1
        print('a:%s' % c[0])
        print('b:%s' % b)
    # 外部函数的返回值是内函数的引用
    return inner

# if __name__ == '__main__':
#     demo = outer1(5)
#     demo()
'''
从上面代码中我们能看出来，在内函数中，分别对闭包变量进行了修改，打印出来的结果也确实是修改之后的结果。
以上两种方法就是内函数修改闭包变量的方法。
'''

'''
还有一点需要注意：使用闭包的过程中，一旦外函数被调用一次返回了内函数的引用，虽然每次调用内函数，是开启一个函数执行过后消亡，
但是闭包变量实际上只有一份，每次开启内函数都在使用同一份闭包变量
'''
def outer2(x):
    def inner(y):
        nonlocal x
        x += y
        return x
    return inner
a = outer2(10)
print(a(1))  # 11
print(a(3))  # 14
# 两次分别打印出11和14，由此可见，每次调用inner的时候，使用的闭包变量x实际上是同一个。

# 闭包的应用
'''
闭包有啥用？？！！

1装饰器！！！装饰器是做什么的？？其中一个应用就是，我们工作中写了一个登录功能，我们想统计这个功能执行花了多长时间，我们可以用装饰器装饰这个登录模块，装饰器帮我们完成登录函数执行之前和之后取时间。

2面向对象！！！经历了上面的分析，我们发现外函数的临时变量送给了内函数。大家回想一下类对象的情况，对象有好多类似的属性和方法，所以我们创建类，用类创建出来的对象都具有相同的属性方法。闭包也是实现面向对象的方法之一。在python当中虽然我们不这样用，在其他编程语言入比如avaScript中，经常用闭包来实现面向对象编程

3实现单利模式！！ 其实这也是装饰器的应用。单利模式毕竟比较高大，，需要有一定项目经验才能理解单利模式到底是干啥用的，我们就不探讨了。
'''