load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@rules_proto_grpc//python:defs.bzl", "python_grpc_library")
load("@rules_proto//proto:defs.bzl", "proto_library")

py_library(
    name = 'greetings',
    srcs = ['greetings.py'],        
)

py_binary(
    name = 'greeter',
	srcs = ['greeter.py'],
    deps = [':greetings',
            ':greeter_service_grpc'],
)

py_binary(
    name = 'client',
	srcs = ['client.py'],
    deps = [':greeter_service_grpc']
)

proto_library (
  name = 'greeter_service_proto',
  srcs = ['greeter.proto'],
  deps = ['@com_google_protobuf//:any_proto'],     
)

python_grpc_library(
  name = 'greeter_service_grpc',
  deps = ['greeter_service_proto']
)
