#include <iostream>
#include <zmq.hpp>

#include <unistd.h>


int main(int argc, char const *argv[])
{
    zmq::context_t context(2);
    zmq::socket_t socket(context, zmq::socket_type::rep);

    socket.bind("tcp://*:4444");

    while (true) {
        zmq::message_t message;
        auto result = socket.recv(message, zmq::recv_flags::none);
        if (result) {
            std::cout << "received: " << result.value() << "\n";
            sleep(1);
            zmq::message_t replay(5);
            memcpy(replay.data(), "hello", 5);
            socket.send(replay, zmq::send_flags::none);
        }
    }


    return 0;
}
