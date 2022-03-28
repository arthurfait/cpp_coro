
#include "api.capnp.h"
#include <capnp/message.h>
#include <capnp/serialize-packed.h>

#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include <iostream>

std::ostream& operator<<(std::ostream& os, const capnp::MessageSize& ms)
{
    os << "Size[wordCount: " << ms.wordCount << '/' << "capCount: " << ms.capCount << "]";
    return os;
}

int main(int argc, char const* argv[])
{
    if (argc > 1 && strncmp("read", argv[1], 4) == 0) {
        int fd = open("data.bin", O_RDONLY);
        if (fd != -1) {
            ::capnp::PackedFdMessageReader pfmr(fd);
            TimeTs::Reader reader = pfmr.getRoot<TimeTs>();
            std::cout << "Size: " << reader.totalSize()
                << "\n";
            std::cout << "TsTime: " << reader.getTsTime()
                << "\n";
            std::cout << "PresentationTime: " << reader.getPresentationTime()
                << "\n";
            std::cout << "SourceId: " << reader.getSourceId()
                << "\n";

            close(fd);
        }

    } else {
        ::capnp::MallocMessageBuilder mmb;
        TimeTs::Builder bob = mmb.initRoot<TimeTs>();
        bob.setPresentationTime(23);
        bob.setTsTime(24);
        bob.setSourceId(1);

        int fd = open("data.bin", O_WRONLY | O_CREAT | O_TRUNC, 0600);
        if (fd != -1) {
            ::capnp::writePackedMessageToFd(fd, mmb);
            close(fd);
        }
    }
    return 0;
}
