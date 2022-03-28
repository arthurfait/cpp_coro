#include <iostream>
#include <zmq.hpp>

int main(int argc, char const *argv[])
{
    zmq::context_t context(1);
    zmq::socket_t socket(context, zmq::socket_type::req);

    std::cout << "Connect ...\n";
    socket.connect("tcp://localhost:4444");

    std::cout << "Connected\n";

    for (int i = 0; i < 10; i++) {
        zmq::message_t request(5);
        memcpy(request.data(), "Ping!", 5);
        std::cout << "Send ping\n";
        socket.send(request, zmq::send_flags::none);

        zmq::message_t reply;
        auto result = socket.recv(reply, zmq::recv_flags::none);
        if (result) {
            std::cout << "got " << reply.to_string() << "\n";
        }
    }

    return 0;
}
