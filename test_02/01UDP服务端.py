#实现客户端和服务器端的即时聊天 自己的ip  10.6.163.21  这是图书馆的A类网络

import socket

# 创建一个UDP的socket对象
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


# bind绑定ip地址和端口号，这里自己随便给了个端口号，一般6000之后就没人用了
# IP：10.6.163.21自己的主机ip（动态的），表示其他主机都可以与当前服务端通信，给空值也是这个效果，绑定所有主机。
#     127.0.0.1这个是本机的测试ip只有自己主机能访问，客户端设置在自己主机上可访问
server_socket.bind(('10.6.163.21',6666))

while True:
    # recvfrom表示接受的数据大小，返回的是信息和地址。所以要用一个两个变量来接，且地址有ip和端口，所以是个列表
    # recvfrom是一个阻塞函数，必须等对方发消息才执行下一句，否则一直阻塞等待
    msg,addr=server_socket.recvfrom(1024)
    #退出，收到客户端发起quit就退出去
    if msg == 'quit':
        break

    # 对方传过来的编码，我们需要转过来，用decode和encode正对应，转回来字符串，此外因为f‘’外面有单引号所以里面双引号，以免冲突
    print(f'msg:{msg.decode("utf-8")},ip is {addr[0]}，端口号：{addr[1]}')

    #服务器向客户端发信息
    send_client=input('输入要给客户端发的信息')
    #sendto发送的不能是字符串，只能是字节，所以要用encode转
    #sendto需要两个参数，一个是编码，一个是对方ip和端口号
    server_socket.sendto(send_client.encode('utf-8'),addr)
server_socket.close()


