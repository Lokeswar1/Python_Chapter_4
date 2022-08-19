def list_to_str(spam):
    output_str = '\''
    for i in range(len(spam)):
        if i<(len(spam)-2):
            output_str = output_str + str(spam[i]) + ', '
        elif i<(len(spam)-1):
            output_str = output_str + str(spam[i]) + ' and '
        else:
            output_str = output_str + str(spam[i]) + "'"
    return output_str

spam = ['apples', 'bananas', 'tofu', 'cats']
list1 = ["abc", 34, True, 40, "male"]
output = list_to_str(list1)
print(output)
