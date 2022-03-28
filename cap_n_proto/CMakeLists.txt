project(cap_n_proto_test)

find_package(PkgConfig)

find_package(PkgConfig)
pkg_check_modules(CAPNP REQUIRED capnp)

add_executable(${PROJECT_NAME} main.cpp api.capnp.c++)
target_link_libraries(${PROJECT_NAME} ${CAPNP_LIBRARIES})