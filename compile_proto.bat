del "my_service_pb2.py"
del "my_service_pb2_grpc.py"
python.exe -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. my_service.proto
