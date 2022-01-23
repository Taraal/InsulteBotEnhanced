import json

output = []

with open('insultes.json', 'r') as f:
    data = json.load(f)

    for first_part in data['first_row']:
        for second_part in data['second_row']:
            for third_part in data['third_row']:
                output.append(first_part + second_part + third_part + " ")

lines_nb = len(output)
print(f"{lines_nb} lines created")
with open('insultes.txt', 'w+') as f:
    f.write(''.join(output))