import grpc
import my_service_pb2
import my_service_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = my_service_pb2_grpc.MyServiceStub(channel)

        def generate_messages():
            while True:
                msg = input("Enter a message to send to the server (or 'q' to quit): ")
                if msg.lower() == "q":
                    break
                yield my_service_pb2.Message(message=msg)
            # responses.cancel()

        # Call the RPC
        responses = stub.MyRpc(generate_messages())
        # m1 = my_service_pb2.Message(message="msg 1")
        # m2 = my_service_pb2.Message(message="msg 2")
        # requests = iter([m1, m2])
        # responses = stub.MyRpc(requests)

        try:
            for response in responses:
                print(f"Received from server: {response.message}")
        except grpc.RpcError as e:
            print(f"RPC Error: {e}")


if __name__ == "__main__":
    run()
