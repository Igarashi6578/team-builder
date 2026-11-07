class Member:
    def __init__(self,name,brightness,facilitation):
        self.name=name
        self.brightness=brightness
        self.facilitation=facilitation

    def introduce(self):
        return f"{self.name}:明るさ{self.brightness},進行能力{self.facilitation}"
    
    def can_facilitate(self,required_level):
        return self.facilitation>=required_level


def find_member(members,name):
    for member in members:
        if member.name==name:
            return member
    return None

def filter_by_brightness(members,min_brightness):
    result2=[]
    for member in members:
        if member.brightness>=min_brightness:
            result2.append(member)
    return result2

def filter_facilitators(members,required_level):
    result3=[]
    for member in members:
        if member.can_facilitate(required_level):
            result3.append(member)
    return result3


member_list=[
    Member("田中",2,5),
    Member("佐藤",5,2),
    Member("鈴木",3,4),
    Member("山本",4,3),
    Member("高橋",5,5)
]

for member in member_list:
    print(member.introduce())
    if member.can_facilitate(4):
        print("回せる")
    else:
        print("回せない")

suzuki=find_member(member_list,"鈴木")
if suzuki is not None:
    print(suzuki.name)
else:
    print("メンバーが見つかりません")
lights=filter_by_brightness(member_list,4)
for light in lights:
    print(light.name,end="")
print()
facilies=filter_facilitators(member_list,4)
for facily in facilies:
    print(facily.name)