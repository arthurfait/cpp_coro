cmake_minimum_required(VERSION 3.22)

project(coro)

# set(CMAKE_CXX_STANDARD_REQUIRED 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_subdirectory("cap_n_proto")
add_subdirectory("flatbuffers/cpp")
add_subdirectory("zmq")


set_source_files_properties(main.cpp PROPERTIES COMPILE_OPTIONS "-fcoroutines;-std=c++20")
add_executable(${PROJECT_NAME} main.cpp)

set_source_files_properties(nloman.cpp PROPERTIES COMPILE_OPTIONS "-std=c++11")
add_executable(json nloman.cpp)




