# Genius Robot

# Speak method should return polite response to hi query
# if query is changed then then should return "I don't know"
# if the query contains key word sum and two integers should return the sum

import re


class Robot:
    def __init__(self):
        print("Robot Initialized")

    def speak(self, query):
        print("ROBOT speaking: ")
        if query == 'hi robot':
            return 'hi human'
        if 'sum' in query:
            print("ROBOT is summing up")
            values = re.findall('[0-9]{1,5}', query)
            print("ROBOT found numbers ::", values)
            numbers_as_float = [float(number) for number in values]
            sum_of_numbers = sum(numbers_as_float)
            print("ROBOT calculated the sum as ::", sum_of_numbers)
            return sum_of_numbers
        return "I don't know"


r = Robot()
print(r.speak('what is the sum of 10, 3333 and 2'))


#
# CHECK REGEX   :::::  numbers = re.findall(r'\b\d+\b', query) ##
