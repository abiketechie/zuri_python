class Student:
    
    def __init__(self, name, age, tracks, score):
        if not type(name) is str:
            print(TypeError("Only Strings are allowed"))
        else:
            self.name = name
        if not type(age) is int:
            print(TypeError("Only integers are allowed"))
        else:
            self.age = age
            self.tracks = tracks
            self.score = score

    def change_name(self, name):
        if not type(name) is str:
            print(TypeError("Only Strings are allowed"))
        else: 
            self.name = name
            print(self.name)

    def change_age(self, age):
        if not type(age) is int:
            print(TypeError("Only integers are allowed"))
        else:
            self.age = age
            print(self.age)

    def add_track(self, tracks):
        self.tracks.append(tracks)
        print(self.tracks)

    def get_score(self):
        print(f"Student score is {self.score}")

    

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
