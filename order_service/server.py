from concurrent import futures
import grpc

import order_pb2
import order_pb2_grpc

import order_to_user

class OrderService(order_pb2_grpc.OrderServiceServicer):
    def GetOrder(self, request, context):
        print("REACHED - order server")
        # Simulate order db
        order = {
            1: {"name": "TV", "price": 10000},
            2: {"name": "Shirt", "price": 800},
            3: {"name": "Chair", "price": 2000}
        }
        user = order_to_user.get_user(request.user_id)
        print("REACHED - after user call")
        order = order.get(request.order_id, {"name": "Unknown product", "price": 0})
        return order_pb2.OrderResponse(
            order_id = request.order_id,
            product = order["name"],
            quantity = request.quantity,
            price = request.quantity * order["price"],
            user_name = user.name,
            user_email = user.email
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('localhost:50052')
    print("Order service running on port 50052")
    server.start()
    server.wait_for_termination()
    
if __name__ == "__main__":
    serve()