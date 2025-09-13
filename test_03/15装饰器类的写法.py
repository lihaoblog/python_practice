class login():
    def __init__(self,func):
        self.func=func

    def __call__(self,*args,**kwargs):
        print('6666')
        return self.func(*args,**kwargs)


@login
def comment():
    print('9898')



if __name__=='__main__':
    comment()
    # print(comment.__name__)  #装饰器类是没有名字函数的，切记

