class Student:
    score_name = ["英文", "數學", "國文"]

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.scores = [0] * len(self.score_name)
    
    def add_score(self, score: int, name: str):
        # add_score(90, "國文")
        # self.scores.append(score)
        # self.scores[num] = score
        index = self.score_name.index(name)
        print(f"index = {index}")
        self.scores[index] = score

st01 = Student(1, "小明")
st02 = Student(1, "小華")
st03 = Student(1, "小佀")

st01.add_score(100, "國文")
st01.add_score(80, "英文")
st01.add_score(90, "數學")
print(st01.scores)

st03.add_score(10, "國文")
st03.add_score(10, "英文")
st03.add_score(0, "數學")
print(st03.scores)