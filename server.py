import grpc
import logging
from concurrent import futures
import my_service_pb2
import my_service_pb2_grpc

LOG_FORMATS = '|%(asctime)s -[%(levelname)s] (%(threadName)-10s) (%(name)s)| %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMATS)

class MyServiceServicer(my_service_pb2_grpc.MyServiceServicer):

    def MyRpc(self, request_iterator, context):
        logging.info(f" ===== RPC - started  =====")

        def on_rpc_done():
            logging.info(f"RPC finished 4 - callback")

        context.add_callback(on_rpc_done)

        try:
            for message in request_iterator:
                logging.info(f"Received message from client: {message.message}")
        except grpc.RpcError as e:
            logging.info(f"RPC finished 2 - except")
            logging.debug((f"RPC Error: {e}"))
        finally:
            logging.info(f"RPC finished 3 - finally")

        logging.info(f"RPC finished 1 - regular")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Server started. Listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
