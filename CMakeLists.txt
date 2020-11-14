# CMakeLists.txt
cmake_minimum_required(VERSION 3.17)
set (CMAKE_TOOLCHAIN_FILE "/home/parin/Documents/vcpkg/scripts/buildsystems/vcpkg.cmake")
set (CMAKE_CXX_STANDARD 17)

project(project4)
find_package(gRPC CONFIG REQUIRED)
find_package(Protobuf CONFIG REQUIRED)
find_package(Threads REQUIRED)

add_subdirectory(external)
add_subdirectory(src)
add_subdirectory(test)
