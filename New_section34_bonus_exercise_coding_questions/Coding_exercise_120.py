# Smart Robot

# Speak method should return polite response to hi query
# if query is changed then then should return "I don't know"

class Robot:
    def __init__(self):
        print("Robot Initialized")

    def speak(self, query):
        print("ROBOT Speaking: ")
        if query == 'hi robot':
            return 'hi human'
        return "I don't know"


r = Robot()
print(r.speak('hi robot'))