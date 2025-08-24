
import socket
import tkinter as tk
from tkinter import scrolledtext


def create_server_socket(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")
    return server_socket

def accept_client_connection(server_socket):
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    return client_socket, client_address
def create_server_ui():
    window = tk.Tk()
    window.title("Server Chat")
    chat_display = scrolledtext.ScrolledText(window, width=50, height=20, wrap=tk.WORD)
    chat_display.grid(row=0, column=0, padx=10, pady=10)
    chat_display.config(state="disabled")
    message_input = tk.Entry(window, width=50)
    message_input.grid(row=1, column=0, padx=10, pady=10)
    def send_message():
        message = message_input.get()
        if message:
            chat_display.config(state="normal")
            chat_display.insert(tk.END, f"Server: { message }\n")
            chat_display.config(state="disabled")
            message_input.delete(0, tk.END)
    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.grid(row=1, column=1, padx=10, pady=10)
    return window, chat_display, message_input
def start_server(host='127.0.0.1', port=12345):
    server_socket= create_server_socket(host, port)

    window, chat_display, message_input = create_server_ui()

    client_socket, _ = accept_client_connection(server_socket)

    def receive_messages():
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                chat_display.config(state="normal")
                chat_display.insert(tk.END, f"Client: { message }\n")
                chat_display.config(state="disabled")

    import threading
    threading.Thread(target=receive_messages, daemon=True).start()

    window.mainloop()

if __name__ == '__main__':
    start_server()