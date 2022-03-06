#include <fstream>
#include <iomanip>
#include <iostream>
#include "json.hpp"



int main(int argc, char const *argv[])
{
    if(argc != 2)
    {
        std::cout << "Need an input file" << std::endl;
        return 0;
    }
    using json = nlohmann::json;
    json s = json::parse(std::fstream(argv[1]));

    std::cout << std::setw(4) << s << "\n\n";

    auto i = 0u;
    std::cout << "Array: " << std::boolalpha << s.is_array() << "\n";
    for(auto it : s)
    {
        std::cout << "Object: " << std::boolalpha << it.is_object() << "\n";
        std::cout << "Idx: " << i++ << "\n";
        std::cout << std::setw(4) << it << "\n";
    }
    return 0;
}
