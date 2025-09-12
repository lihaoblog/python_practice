# 改写元类，先继承元类，修改他的new函数
#返回的时候要返回其父类type，看一下一行怎么写for循环
class UpperMetaClass(type):
    def __new__(cls,class_name,class_parent,class_attr):
        new_attr=dict((k,v) if k.startswith('__') else (k.upper(),v) for k,v in class_attr.items())
        return super().__new__(cls,class_name,class_parent,new_attr)



# 这里不再用type元类而是我自己用
class person(object,metaclass=UpperMetaClass):
    __age=33
    name='li'

if __name__=='__main__':
    p=person()
    print(p.NAME)
    print(hasattr(person,'__age'))
    print(person._PERSON__AGE)
    print(person.__dict__)  #展示所有属性，这里的私有属性名字变了


