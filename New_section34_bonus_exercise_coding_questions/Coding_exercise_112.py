# Print out all the questions in file2

questions = []
with open("./files10/file2.txt") as file:
    lines = file.read()
    print(lines)
    start = 0
    end = 0
    while True:
        end = lines.find("?", end + 1)
        start = lines.rfind(".", start, end + 1)
        question = lines[start + 1:end + 1]
        start = end + 1
        if question.strip():
            questions.append(question.strip())
        if end == -1:
            break

print(questions)

# # More elegant solution check regular expressions
import re

with open("./files10/file2.txt") as file:
    content = file.read()
    print(re.findall("[A-Z][a-z ',]*\?", content))
