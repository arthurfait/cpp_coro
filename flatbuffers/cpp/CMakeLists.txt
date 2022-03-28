project(flatbuffers_test)

find_package(Flatbuffers REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)
target_include_directories(${PROJECT_NAME} PRIVATE ${Flatbuffers_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} ${Flatbuffers_LIBRARIES})