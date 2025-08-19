file =open('lumbar.pdf','w')
file.write("This is a sample text for the lumbar file")
file.close()

file = open('lumbar.pdf', 'r')
content = file.read()
print(content)
file.close()

file=open('lumbar.pdf', 'a')
file.write("sneezing is good.\n")
file.close()

file = open('lumbar.pdf', 'r')
content = file.read()
print(content)
# Modify the content
rangi=content.upper()
print(rangi)
# Write the modified content back to the file
file = open('lumbar.pdf', 'w')
file.write(rangi)
file.close()
# Read the modified content
file = open('lumbar.pdf', 'r')
content = file.read()
print(content)
file.close()


print("File 'lumbar.pdf' has been created and modified successfully.")

try:
    with open('lumbar.pdf', 'r') as file:
        content = file.read()
        print("true")
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")