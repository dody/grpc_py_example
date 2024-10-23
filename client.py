import grpc
import my_service_pb2
import my_service_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = my_service_pb2_grpc.MyServiceStub(channel)

        def generate_messages():
            while True:
                msg = input("Enter a message to send to the server (or 'q' to quit, 'c' to cancel rpc): ")
                if msg.lower() == "q":
                    break
                if msg.lower() == "c":
                    responses.cancel()

                yield my_service_pb2.Message(message=msg)

        # Call the RPC
        responses = stub.MyRpc(generate_messages())

        try:
            for response in responses:
                print(f"Received from server: {response.message}")
        except grpc.RpcError as e:
            print(f"RPC Error: {e}")


if __name__ == "__main__":
    run()
