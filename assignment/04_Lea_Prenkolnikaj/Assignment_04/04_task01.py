#Task 01: Lambda functions

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use the filter function and a lambda function to retain only the even values
output_array = list(filter(lambda x: x % 2 == 0, input_array))

# Print the input array and the filtered output array
print("Input array:", input_array)
print("Output array:", output_array)
