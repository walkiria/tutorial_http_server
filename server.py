import http.server
import socketserver


# Instale o hpptserver: pip3 install httpserver


#a web server is a process that listens to incoming requests on specific TCP address.

#TCP address is identified by an ip address and a port number.

#a web server also needs to be told how to handle incoming requests



PORT = 8080  # porta em que o servidor vai rodar
Handler = http.server.SimpleHTTPRequestHandler  # manipulador de solicitações http


#An instance of TCPServer describes a server that uses the TCP protocol to
# send and receive messages (http is an application layer protocol on top of TCP).

#To instantiate a TCP Server, we need two things:

#1- The TCP address (IP address and a port number)

#2- The handler

httpd =socketserver.TCPServer(("", PORT), Handler)   #
#with socketserver.TCPServer(("", PORT), Handler) as httpd:
print("serving at port", PORT)

#serve_forever is a method on the TCPServer instance
# that starts the server and begins listening and responding to incoming requests.
httpd.serve_forever()