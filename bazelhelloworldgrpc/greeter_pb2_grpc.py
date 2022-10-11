# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import greeter_pb2 as greeter__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.hello = channel.unary_unary(
        '/Greeter/hello',
        request_serializer=greeter__pb2.Name.SerializeToString,
        response_deserializer=greeter__pb2.GreetingsMsg.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def hello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'hello': grpc.unary_unary_rpc_method_handler(
          servicer.hello,
          request_deserializer=greeter__pb2.Name.FromString,
          response_serializer=greeter__pb2.GreetingsMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
