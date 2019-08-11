# -*- coding: UTF-8 -*-
import socket

print("程序开始")
print("等待连接....")
#   创建套接字
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   设置IP和端口
host = socket.gethostname()
port = 23336
# #   bind绑定该端口
mySocket.bind((host, port))
# #   监听
mySocket.listen(10)

#   创建套接字
mySocket_pc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   设置IP和端口
host_pc = socket.gethostname()
port_pc = 23337
#   bind绑定该端口
mySocket_pc.bind((host_pc, port_pc))
#   监听
mySocket_pc.listen(10)

# 一起等
client, address = mySocket.accept()
client_pc, address_pc = mySocket_pc.accept()

# 输出确认一下两个设备都连接上
print("Pi连接")
print("IP is %s" % address[0])
print("port is %d\n" % address[1])
print("Pc连接")
print("IP is %s" % address_pc[0])
print("port is %d\n" % address_pc[1])

# 把最开始的树莓派累计的数据给清空
msg = client.recv(1024)

while True :
    try :
        try :
            # 确认连接
            client.send("cheakout")
            msg = client.recv(1024)
            wxx = msg
            print(wxx)
            if "over" in wxx :
                raise IOError
        except IOError :
            # 　如果Pi掉线了就等Pi连接回来先
            mySocket.listen(10)
            print("Pi等待连接....")
            client, address = mySocket.accept()
            print("Pi重新连接")
            # msg = client.recv(1024)

        print("----------------------读取:", msg)
        print("读取完成")

        try :
            client_pc.send(msg)
            wxx = client_pc.recv(1024)
            print(wxx)
            if "over" in wxx :
                raise IOError
        except IOError :
            # 如果Pc掉线了就等Pc连接回来先
            mySocket_pc.listen(10)
            print("Pc等待连接....")
            client_pc, address_pc = mySocket_pc.accept()
            print("Pc重新连接")
	            # 吐掉垃圾

            # msg = client.recv(1024)
        else :
            
            print("----------------------发送:", msg)
            print("发送完成")

    # 这里是为了能够我们手动退出的时候让程序把端口给关闭
    except KeyboardInterrupt :
        mySocket.shutdown(2)
        mySocket.close()
        mySocket_pc.shutdown(2)
        mySocket_pc.close()
        break

print("over")
