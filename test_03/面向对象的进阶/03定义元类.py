# 元类修改类
# 定义一个新的元类，将type元类的字典修改了，以后返回只能按照我给的元类修改后的属性,把属性名改大写
def UpperMetaClass(class_name,class_parent,class_attr):
    new_attr={}
    for k,v in class_attr.items():    # 字典的列表展示
        if not k.startswith('__'):   # 开始函数
            new_attr[k.upper()]=v
        else:
            new_attr[k]=v
    return type(class_name,class_parent,new_attr)

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


