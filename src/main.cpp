#include <iostream>
#include <omp.h>

extern "C" double cmult(int int_param, double* float_param);


// cmult.c
double cmult(int int_param, double* float_param) {
    double return_value = int_param * float_param[1];
    printf("    In cmult : int: %d float %.1f returning  %.1f\n", int_param,
            float_param[1], return_value);
    return return_value;
}


// int main(){
//     
//     #pragma omp parallel
//     {
//         std::cout << "hello world" << std::endl;
//     }
// 
//     return 0;
// }