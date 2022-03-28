find_package(PkgConfig)
pkg_check_modules(ZMQ REQUIRED libzmq)

project(zmq_server_test)
add_executable(${PROJECT_NAME} zmq_server.cpp)
target_include_directories(${PROJECT_NAME} PRIVATE ${ZMQ_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} ${ZMQ_LIBRARIES})

project(zmq_server_client)
add_executable(${PROJECT_NAME} zmq_client.cpp)
target_include_directories(${PROJECT_NAME} PRIVATE ${ZMQ_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} ${ZMQ_LIBRARIES})