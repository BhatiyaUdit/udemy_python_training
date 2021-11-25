# Polite Robot

# Speak method should return polite response to hi query


class Robot:
    def __init__(self):
        print("Robot Initialized")

    def speak(self, query):
        print("ROBOT Speaking: ")
        if query == 'hi robot':
            return 'hi human'


r = Robot()
print(r.speak('hi robot'))