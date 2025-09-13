# 客户端不需要bind端口号啥的没只需要创接口，发文件和管端口
import socket
# 创建一个udp接口

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
    send_msg=input('发给服务器信息')
    if send_msg=='quit':
        client_socket.sendto(send_msg.encode('utf-8'), ('10.6.163.21', 6666))
        break
    client_socket.sendto(send_msg.encode('utf-8'),('10.6.163.21',6666))

    #接受服务器给的信息
    msg,addr=client_socket.recvfrom(1024)
    print(f'接收到服务器msg:{msg.decode("utf-8")},ip is {addr[0]}，端口号：{addr[1]}')

client_socket.close()
