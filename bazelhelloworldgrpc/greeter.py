# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:10:16 2020

@author: User
"""
import grpc
from concurrent import futures
import greeter_pb2_grpc
import greeter_pb2
import time


from greetings import greet

class Greeter(greeter_pb2_grpc.GreeterServicer): 
    
    def hello(self, request, context):
        response = greeter_pb2.GreetingsMsg() 
        greetings = greet(request.name)
        response.msg = greetings
        return response
    
    
def serve(port):  
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:%d' % port)
    server.start()
    print("Server is running")
    try:
      while True:
        time.sleep(2)
        print(".")
    except KeyboardInterrupt:
      server.stop(0)
      print("stopped")     


if __name__ == "__main__":
    serve(7000)