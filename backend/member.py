class Member:
    def __init__(self,name,brightness,facilitation):
        self.name=name
        self.brightness=brightness
        self.facilitation=facilitation
    def introduce(self):
        return f"{self.name}:明るさ{self.brightness},進行能力{self.facilitation}"
    def can_facilitate(self,required_level):
        return self.facilitation>=required_level

member_list=[
    Member("田中",2,5),
    Member("佐藤",5,2),
    Member("鈴木",3,4)
]

for member in member_list:
    print(member.introduce())
    if member.can_facilitate(4):
        print("回せる")
    else:
        print("回せない")