cmake_minimum_required(VERSION 3.20)
project(cpp_learning_coach LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(cpp_learning_coach src/main.cpp)
target_compile_options(cpp_learning_coach PRIVATE -Wall -Wextra -Wpedantic)
