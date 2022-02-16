user_input = input("Please enter three numbers separated by a comma: ")
string_token = user_input.split(", ")

int_tokens = []
for i in string_token:
    int_tokens.append(int(i))

a, b, c = int_tokens

result = a + b - c

print(result)