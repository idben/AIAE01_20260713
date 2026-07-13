class PartyMember:
    # 建構子
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp

hero = PartyMember("勇者", 30, 10)
mage = PartyMember("魔法使", 18, 24)

print(hero.name)
print(mage.mp)