# merge data of three file in folder to one file together.txt

import glob

files = glob.glob('./files8/*.txt')

print(files)

for file in files:
    with open(file) as read_file:
        data = read_file.read()

    with open('./files8/together.txt', 'a+') as write_file:
        write_file.read()
        write_file.write(data)
        write_file.write("\n")

        import glob

# text_files = glob.glob("file*.txt")
# print(text_files)
# with open('together.txt', 'w') as outfile:
#     for text_file in text_files:
#         with open(text_file) as infile:
#             for line in infile:
#                 outfile.write(line + "\n")
