
import tkinter as tk
import socket as sk
# HOST = '127.0.0.1'
# PORT=2050
conn_socket=None
def conn_server():
    global conn_socket
    if conn_socket:
        conn_socket.close()
        name_con.config(text=" Disconnect", fg="black")
        conn_socket = None
        connect_button.config(text="Connect",bg="green")
    else:
        _host=input_host.get()
        _port=int(input_port.get())

        try:
            conn_socket= sk.socket(sk.AF_INET, sk.SOCK_STREAM)
            conn_socket.connect((_host, _port))
            name_con.config(text=f"Connecting", fg="green")
            connect_button.config(text="Disconnect",bg="red")
        except Exception as e:
            name_con.config(text=f"failed ", fg="red")

def send_all():
    global conn_socket
    text_send = str(input_A.get()+input_S.get()+input_B.get())
    conn_socket.sendall(text_send.encode())
    data = conn_socket.recv(1024)
    print(type(data))
    return_name.config(text=data)


root=tk.Tk()
root.geometry("250x300")
root.title("Server_calculator")

root.resizable(0,0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

#connect server
name_host=tk.Label(root,text="HOST",font="Roboto")
name_port=tk.Label(root,text="PORT",font="Roboto")
input_host=tk.Entry(root,font="Roboto")
input_port=tk.Entry(root,font="Roboto")
name_con=tk.Label(root,text=" Disconnect",fg= "black")
name_con.grid(column=0,row=2,sticky=tk.W,padx=5,pady=5)
name_port.grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)
input_port.grid(column=1,row=1,sticky=tk.E,padx=5,pady=5)
name_host.grid(column=0,row=0,sticky=tk.W,padx=5,pady=5)
input_host.grid(column=1,row=0,sticky=tk.E,padx=5,pady=5)
connect_button = tk.Button(root,font=("Roboto",12),fg="white", text="Connect",bg="green",command=conn_server) 
connect_button.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5) 

#send into
A_name = tk.Label(root,text="A",font="Roboto")
symbols_name = tk.Label(root,text="+ - * / ",font="Roboto")
B_name = tk.Label(root,text="B",font="Roboto")
A_name.grid(column=0,row=3,sticky=tk.W,padx=5,pady=5)
symbols_name.grid(column=0,row=4,sticky=tk.W,padx=5,pady=5)
B_name.grid(column=0,row=5,sticky=tk.W,padx=5,pady=5)

input_A = tk.Entry(root,font="Roboto",width=10)
input_S = tk.Entry(root,font="Roboto",width=5)
input_B = tk.Entry(root,font="Roboto",width=10)

input_A.grid(column=1,row=3,sticky=tk.W,padx=5,pady=5)
input_S.grid(column=1,row=4,sticky=tk.E,padx=5,pady=5)
input_B.grid(column=1,row=5,sticky=tk.W,padx=5,pady=5)
to_button = tk.Button(root,font=("Roboto",12),fg="white", text="=",bg="green",command=send_all)#command=send_all
to_button.grid(column=1,row=6,sticky=tk.EW,padx=5,pady=5)
#return
is_name = tk.Label(root,text="=",font="Roboto")
return_name = tk.Label(root,text="",font="Roboto")
is_name.grid(column=0,row=7,sticky=tk.EW,padx=5,pady=5)
return_name.grid(column=1,row=7,sticky=tk.EW,padx=5,pady=5)
root.mainloop()