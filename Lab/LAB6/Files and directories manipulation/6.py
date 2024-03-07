import os

path = "C:\\Users\\Admin\\Desktop\\pp2\\PY\\LAB6\\Files and directories manipulation"
    
for letter in range(ord('A'), ord('Z') + 1):
    file_name = f"{chr(letter)}.txt"
    file_path = os.path.join(path, file_name)
        
    open(file_path, 'x')

print ("Files were successfuly created!")