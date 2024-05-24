# string-art

## Build

```bash
mkdir build 
cd build 
cmake -D CMAKE_CXX_COMPILER=icpc .. && make -j 1
```

## Idea

- input from python 
    - get nail positions 
    - get grayscaled, fine-grained image 
        - one pixel the with of the string 
    - get number of strings
- algorithm 
    ```
    for i in num_strings:
        for j in all_strings:
            gain[j] = gain_function(input_img, j)
        accepted_j = max(gain)
        input_img = substract_line(input_img, j)
    
    pin_sequence = connect_all_strings()
    return pin_sequence
    ```
    ```
    def gain_function(input_img, j):
        gain = 0
        for i in pixel_under_line:
            gain += pixel_gray_value[i]
        return gain 
    ```
    lines in algorithm: infinitely small
    pixel_with: with of lines in real world 
    
