def to_camel_case(input_str):
    words = input_str.split()
    camel_case_words = [word.capitalize() for word in words]
    camel_case_str = ''.join(camel_case_words)


    return camel_case_str


input_string = "camel case word"
result = to_camel_case(input_string)
print(result)
