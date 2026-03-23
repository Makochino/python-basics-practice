regular_dict = {'horse': 1,
                'cat': 2,
                'nigger': 0,}

inverted = {value: key for key, value in regular_dict.items()}

print(inverted)