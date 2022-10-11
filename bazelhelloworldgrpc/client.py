# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:39:08 2020

@author: User
"""

from __future__ import print_function
import greeter_pb2_grpc
import greeter_pb2
import grpc

def hello(n):    
   print("[client:hello]") 
   res = stub.hello(greeter_pb2.Name(name = n))
   print(res.msg)
   
   
if __name__ == "__main__":
    
    print("[client:main]") 
    channel = grpc.insecure_channel('localhost:%d' % 7000)
    stub  = greeter_pb2_grpc.GreeterStub(channel) 
    
    hello("Irina")