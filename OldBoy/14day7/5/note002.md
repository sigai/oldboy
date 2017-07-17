#类和对象
https://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python#
在理解元类之前,你需要掌握Python的类, Python借用了Smalltalk中的类特别的创意.
大多数编程语言中, 类就是用来描述如何创建对象的代码块. Python中也是这样的:
```
>>> class ObjectCreator(object):
...       pass
...       
>>> my_object = ObjectCreator()
>>> print(my_object)
<__main__.ObjectCreator object at 0x000001A3258982B0>
```
但是在Python中的类却远不止此. 类也是对象!
只要你用了class关键字, Python执行并创建一个对象, 这块代码:
```
>>> class ObjectCreator(object):
...       pass
...
```
在内存中创建了一个名为`ObjectCreator`的对象.
**这个类对象有创建对象的能力, 因此称之为类.**
但是, 因为类是一个对象, 所以:
1. 可以把类赋值给变量
1. 可以复制
1. 可以给它添加属性和方法
1. 可以当作函数的参数被传递

例如:
```
>>> print(ObjectCreator)  # 因为类也是对象, 所以可以打印它
<class '__main__.ObjectCreator'>
>>> def echo(o):
	print(o)


>>> echo(ObjectCreator) # 类可以作为参数去传递
<class '__main__.ObjectCreator'>
>>> ObjectCreator.new_attribute = 'foo' #可以为类添加新的属性
>>> print(hasattr(ObjectCreator,'new_attribute'))
True
>>> print(ObjectCreator.new_attribute)
foo
>>> ObjectCreatorMirror = ObjectCreator #可以把类复制给变量
>>> print(ObjectCreatorMirror.new_attribute)
foo
>>> print(ObjectCreatorMirror)
<class '__main__.ObjectCreator'>
```
#动态的创建类
既然类也是对象, 你也可以像创建对象一样, 动态的创建类.
1. 首先你可以在函数内部用`class`关键字创建类:

```
>>> def choose_class(name):
	if name == 'foo':
		class Foo(object):
			pass
		return Foo  #返回值是类, 不是实例
	else:
		class Bar(object):
			pass
		return Bar

>>> MyClass = choose_class('foo')
>>> print(MyClass)  # 函数返回了一个类, 不是实例
<class '__main__.choose_class.<locals>.Foo'>
>>> print(MyClass())  # 可以用这个类创建一个对象
<__main__.choose_class.<locals>.Foo object at 0x000002C83CB38F28>
```
但是,这还不是动态的, 整个类还是得自己写. 因为类是对象, 所以类也可以被其他什么的生成.
当你使用 `class`关键字的时候, Python自动创建了类对象, 但是跟其他多数东西一样, Python也提供了手动创建类的方法.
还记得`type`函数吗? 这个挺不错的老函数可以产看对象的类型:
```
>>> print(type(1))
<class 'int'>
>>> print(type('1'))
<class 'str'>
>>> print(type(ObjectCreator))
<type 'type'>
>>> print(type(ObjectCreator()))
<class '__main__.ObjectCreator'>
```
然而, `type`拥有完全不同的功能, 可以动态的创建类. `type`可以接收类的描述参数,返回一个类.
(一个函数根据参数数量的不同有不同的功能, 确实很蠢, 这是Python向后兼容产生的问题.)
`type`的用法:
```
type(name of the class,
     tuple of the parent class (for inheritance, can be empty),
     dictionary containing attributes names and values)
```
如下:
```
>>> class MyShinyClass(object):
...       pass
```
可以手动方式创建:
```
>>> MyShinyClass = type('MyShinyClass',(),{}) # 返回一个类对象
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'> # 创建类的实例
>>> print(MyShinyClass())
<__main__.MyShinyClass object at 0x000002C83CB38F28>
>>>
```
你会发现, 我们这里用`MyShinyClass`做类名, 并且引用类的变量名也是这个. 这里可以用不同的名字, 但是没必要把问题复杂化.
`type`接收一个字典去定义类的属性, 所以:
```
>>> class Foo(object):
	bar = True
```
也可以写成
```
>>> Foo = type('Foo',(),{'bar':True})
>>>
```
也可以像正常的类一样使用:
```
>>> print(Foo)
<class '__main__.Foo'>
>>> print(Foo.bar)
True
>>> f = Foo()
>>> print(f)
<__main__.Foo object at 0x000002C83CBD9748>
>>> print(f.bar)
True
>>>
```
当然, 你也可以继承它, 所以:
```
>>>   class FooChild(Foo):
...         pass
```
也就可以写成:
```
>>> FooChild = type('FooChild',(Foo,),{})
>>> print(FooChild)
<class '__main__.FooChild'>
>>> print(FooChild.bar) # bar是继承自Foo的
True
```
最后, 你需要为你的类添加方法的话, 只需要定义一个有切当的特征的函数, 然后将其作为属性分配.
```
>>> def echo_bar(self):
	print(self.bar)


>>> FooChild = type('FooChild',(Foo,),{'echo_bar':echo_bar})
>>> hasattr(Foo, 'echo_bar')
False
>>> hasattr(FooChild, 'echo_bar')
True
>>> my_foo = FooChild()
>>> my_foo.echo_bar()
True
```
动态的创建类之后你可以继续增加更多的方法, 就跟为正常方式创建的类添加方法一样.
```
>>> def echo_bar_more(self):
	print('more more more')


>>> FooChild.echo_bar_more = echo_bar_more
>>> hasattr(FooChild,'echo_bar_more')
True
```
总之, 在Python中, 类也是对象, 也可以动态的创建.
当你用关键字`class`时,Python是这样的, 当你使用元类的时候也是一样.
#什么是元类
元类是创建类的东西.
定义类是为了创建对象吧, 但是刚了解到Python中类也是对象, 那么元类就是创建类对象的家伙, 它们是类的类, 这样可以发现他们:
```
MyClass = MetaClass()
MyObject = MyClass()
```
我们知道`type`可以做下面的事:
```
MyClass = type('MyClass', (), {})
```
这是因为`type`函数其实是一个元类. `type`是Python在后台用来创建所有类的元类
现在你可能纠结为什么是小写的,不应该是`Type`么?
我觉得可能是跟创建string对象的`str`,还有创建整型对象的`int`保持一致性吧, `type`只是创建类对象的类而已.
检查__class__属性就能看出来了.
在Python里,一切都是对象, 包括整型, 字符串, 函数和类. 所有这些都是对象, 他们都是相应的类创建的.
```
>>> age = 35
>>> age.__class__
<type 'int'>
>>> name = 'bob'
>>> name.__class__
<type 'str'>
>>> def foo(): pass
>>> foo.__class__
<type 'function'>
>>> class Bar(object): pass
>>> b = Bar()
>>> b.__class__
<class '__main__.Bar'>
```
那么, 所有__class__的__class__是什么呢?
```
>>> age.__class__.__class__
<type 'type'>
>>> name.__class__.__class__
<type 'type'>
>>> foo.__class__.__class__
<type 'type'>
>>> b.__class__.__class__
<type 'type'>
```
可见, 元类就是创建类对象的东西.
如果你愿意也可以叫它类工厂.
`type`是Python使用的内置元类, 当然你也可以自己创建自己的元类.
# `__metaclass__`属性

可以为类添加一个 `__metaclass__`属性
```
class Foo(object):
  __metaclass__ = something...
  [...]
```
这样, Python会使用元类去创建类`Foo`.
注意了, 这里有陷阱!
你先写了`class Foo(object)`, 但是类对象`Foo`还没在内存中创建呢.
Python会查找类定义中的`__metaclass__`, 如果找到会用它去创建对象类`Foo`.如果没找到就会用`type`去创建类.
多读几遍....
当你:
```
class Foo(Bar):
  pass
```
Python做了下面的事情:
1. Foo里有`__metaclass__`属性吗?
1. 如果找到,则用`__metaclass__`中的定义在内存里创建一个`Foo`类对象(注意是类对象)
1. 如果没找到, 会到模块层去找(只有在创建的是没有任何继承的旧式类如此)
1. 如果全都没找到, 会使用父类`Bar`的元类(默认是`type`)去创建类对象.
注意了, 元类属性不能被子类继承, 父类的元类(Bar.__class__)是`type`的可以被继承. 如果`Bar`是用了`type`的`__metaclass__`属性, 而不是`type.__new__`属性创建的, 子类不会继承它的行为.
现在的问题是, `__metaclass__`里能做什么?
答案当然是创建类的事情啦...
然后怎么创建类呢,`type`或者它的子类或者用了它的东西.
#自定义元类