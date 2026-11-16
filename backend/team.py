from member import Member

class Team:
    def __init__(self,name):
        self.name=name
        self.members=[]
    
    def add_member(self,member):
        self.members.append(member)
    
    def get_member_count(self):
        return len(self.members)

    def is_within_capacity(self,max_members):
        return self.get_member_count()<=max_members

    def has_facilitator(self,required_level):
        return self.count_facilitators(required_level)>=1

    def count_facilitators(self,required_level):
        canfacilis=[]
        for member in self.members:
            can_facilitate=member.can_facilitate(required_level)
            if can_facilitate:
                canfacilis.append(member)
        return len(canfacilis)


member1=Member("田中",2,5)
member2=Member("佐藤",5,2)
member3=Member("鈴木",3,4)
member4=Member("山本",4,3)
member5=Member("高橋",5,5)

team_a=Team("A")
team_b=Team("B")

team_a.add_member(member1)
team_a.add_member(member2)
team_a.add_member(member3)
team_b.add_member(member4)
team_b.add_member(member5)

teams=[team_a,team_b]

for team in teams:
    print(f"{team.name}")
    print("メンバー:",end="")
    for names in team.members:
        print(f"{names.name} ",end="")
    print()
    print(f"人数:{team.get_member_count()}人")
    print(f"進行役:{team.count_facilitators(4)}人")
    print(f"人数{team.is_within_capacity(3)}")
    print(f"人数が2人以下{team.is_within_capacity(2)}")
    print(f"進行能力{team.has_facilitator(4)}")
    print(f"進行能力6人以上{team.has_facilitator(6)}")