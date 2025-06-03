import os

project_root = r"C:\Users\lunta\Desktop\arbolesCDMX\arbolescdmx"
for dirpath, dirnames, filenames in os.walk(project_root):
    for fname in filenames:
        if fname.endswith(".py"):
            print(f"Checking file: {fname}")
            fpath = os.path.join(dirpath, fname)
            with open(fpath, "rb") as f:
                data = f.read()
            if b"\x00" in data:
                print(f"Null byte found in: {fpath}")

            
        
