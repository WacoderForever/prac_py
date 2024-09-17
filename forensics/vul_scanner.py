import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('41.89.96.40',80))  
    ans=s.recv(1024)
    print(ans.decode())
except socket.error as e:
    if e.errno == 113:  
        print("No route to host. Please check the network settings or server availability.")
    else:
        print(f"An error occurred: {e}")
finally:
    s.close()


