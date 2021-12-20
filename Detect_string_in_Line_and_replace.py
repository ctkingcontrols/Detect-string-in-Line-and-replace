import os.path

ae = '13'


for sg in range(800):
    new_lines = []

    str_sg = str(sg)
    if os.path.exists(f'{sg}.txt'):
        with open(f'{str_sg}.txt', encoding='utf8') as f:
            for line in f:
                if ('Direction' in line):
                    if line[18] ==  ']':
                        newline = line[:32] + f' NOT SafetyOutput.EmergencyCircuitOk.SG{str_sg} OR NOT SafetyOutput.EmergencyCircuityOk.AE{ae};'
                        line = newline
                    elif line[19] ==  ']':
                        newline = line[:33] + f' NOT SafetyOutput.EmergencyCircuitOk.SG{str_sg} OR NOT SafetyOutput.EmergencyCircuityOk.AE{ae};'
                        line = newline
                    else:
                        newline = line[:34] + f' NOT SafetyOutput.EmergencyCircuitOk.SG{str_sg} OR NOT SafetyOutput.EmergencyCircuityOk.AE{ae};'
                        line = newline
                new_lines.append(line)


        with open(f'output{str_sg}.txt', 'w') as f:
            for line in new_lines:
                f.write(f'{line}')
                f.write('\n')
