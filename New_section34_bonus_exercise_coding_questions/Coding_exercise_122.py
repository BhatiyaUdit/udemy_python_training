# Genius Robot and its Mind

# Speak method should return polite response to hi query
# if query is changed then then should return "I don't know"
# if the query contains key word sum and two integers should return the sum
#
# Separation of concerns for Mind and Robot

import re


class Mind:
    def __init__(self):
        print("MIND initialized")

    def think(self, query):
        print("MIND started thinking query :: ", query)
        if 'sum' in query:
            print("MIND is summing up")
            values = re.findall(r'\b\d+\b', query)
            print("MIND found numbers ::", values)
            numbers_as_float = [float(number) for number in values]
            sum_of_numbers = sum(numbers_as_float)
            print("MIND calculated the sum as ::", sum_of_numbers)
            return sum_of_numbers


class Robot:
    def __init__(self):
        print("Robot Initialized")
        self.mind = Mind()

    def speak(self, query):
        print("ROBOT speaking: ")
        if query == 'hi robot':
            return 'hi human'
        return "I don't know"

    def print_out(self, query):
        print("ROBOT starting to print")
        print(self.mind.think(query))

    def write_down(self, query):
        print("ROBOT started to write down")
        information = self.mind.think(query)
        with open('./files10/information.txt', 'w') as info_file:
            info_file.write(str(information))



r = Robot()
print(r.speak('what is the sum of 10, 3333 and 2'))
print(r.print_out('what is the sum of 10, 3333 and 2'))
print(r.write_down('what is the sum of 10, 3333 and 2'))

#
# CHECK REGEX   :::::  numbers = re.findall(r'\b\d+\b', query) ##
