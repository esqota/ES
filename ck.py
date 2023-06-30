import os
i = 0
for filename in os.listdir():
    if filename.endswith('.ass'):
        ass_file = filename
        ts_file = os.path.splitext(ass_file)[0] + '.ts'
        if not os.path.isfile(ts_file):
            print(f"Warning: {ts_file} does not exist for {ass_file}")
        i=i+1

print(str(i)+" finished")