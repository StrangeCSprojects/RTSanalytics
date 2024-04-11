nested_list = [[["unit type", "unit name"], 10], 1]

# Updated list comprehension to handle the deeper nested structure
result_commands = [((tuple(inner_list[0][0]), inner_list[0][1]), inner_list[1]) for inner_list in [nested_list]]

print(result_commands)
