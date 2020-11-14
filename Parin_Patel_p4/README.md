#AOS Project 4

#Parin Patel

## Build Tools / Requirement
    - GCC 7.4 and above
    - [`vcpkg`](https://github.com/microsoft/vcpkg) - Package Manager for C/C++ libraries
    - [`protobuf`](https://github.com/protocolbuffers/protobuf/blob/master/src/README.md) - Google Protocol Buffers
    - [`gRPC`](https://github.com/grpc/grpc/blob/master/src/cpp/README.md) - Google's RPC framework
    - C++ version 17 .

For development :

-- cmake version 3.17.2
-- grpc version --> v1.31.1
-- The C compiler identification is GNU 9.3.0
-- The CXX compiler identification is GNU 9.3.0

** Even though version used for development is much higher , it does provide check and validation for gcc 7 and above.**



## Build Instructions
  1. Make sure you're using cmake 3.10+.
  2. Create and change into your build directory: `mkdir build; cd build`
  3. Remember to change the path to your vcpkg toolchain file in the line 6 of project4/CMakeLists.txt: `set (CMAKE_TOOLCHAIN_FILE "/path/to/vcpkg/scripts/buildsystems/vcpkg.cmake")`
  3. Run `cmake` as follows:   `cmake ..`
  4. Run `make`.
  6. Two binaries would be created under the `build/bin` directory: `mrdemo` and `mr_worker`.
  7. Symbolic link to `project4/test/config.ini` is installed as `build/bin/config.ini`


```
parin@parin-VirtualBox:[Thu Nov 12 20:57:50]:~/CLionProjects/AOS/aos4/cmake-build-debug/bin:[project4 !x?+]$ tree
.
├── config.ini -> /home/parin/CLionProjects/AOS/aos4/test/config.ini
├── data.patch
├── mrdemo
├── mr_worker

2 directories, 4 files

```
## Run Instructions
  1. Clear the files if any in the `output`/, `temp/` and/or `intermediate/` directory.
  2. Start all the worker processes (e.g. for 2 workers): `./mr_worker localhost:50051 & ./mr_worker localhost:50052;`
  3. Then start your main map reduce process: `./mrdemo config.ini`
  4. Once the ./mrdemo finishes, kill all the worker proccesses you started.
  5. Check output directory to see if you have the correct results(obviously once you have done the proper implementation of your library).


## Notes

- Sorting is done using standard `map` datastructure , which consider all `uppercase` char inlower order then `Lowercase` chars.
- line breaks are supposed for unix line breaks `\n`.


## References

1. [Asynchronous-API tutorial – gRPC](https://grpc.io/docs/languages/cpp/async/)
2. https://isocpp.org/files/papers/n3563.pdf
3. [grpc/greeter_async_server.cc at v1.32.0 · grpc/grpc · GitHub](https://github.com/grpc/grpc/blob/v1.32.0/examples/cpp/helloworld/greeter_async_server.cc)
4. [cplusplus.com - The C++ Resources Network](http://www.cplusplus.com/)
5. [cppreference.com](https://en.cppreference.com/)
6. [c++ - terminate called recursively - Stack Overflow](https://stackoverflow.com/questions/12347981/terminate-called-recursively)
7. https://research.google/pubs/pub62.pdf
8. https://grpc.github.io/grpc/cpp/md_doc_environment_variables.html
9. https://developer.lsst.io/cpp/api-docs.html