cmake_minimum_required(VERSION 3.1)


project(stringart VERSION 1.0 
                  DESCRIPTION "C++ library to build fancy strin art." 
                  LANGUAGES CXX) 

set(CMAKE_CXX_FLAGS "-O2 -ip -fp-model precise -no-multibyte-chars -fopenmp")  

find_package(OpenMP)
                  
# build as library 
#add_library(stringart SHARED src/main.cpp)            

# build as executable

add_executable(stringart src/main.cpp)            

if(OpenMP_CXX_FOUND)
    target_link_libraries(stringart PUBLIC OpenMP::OpenMP_CXX)
endif()