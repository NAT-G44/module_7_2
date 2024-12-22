def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as f:
        for i, line in enumerate(strings, start=1):
            byte_position = f.tell()
            f.write(line + '\\n')
            strings_positions[(i, byte_position)] = line
    return strings_positions

file_name = 'output.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.']
result = custom_write(file_name, strings)
print(result)