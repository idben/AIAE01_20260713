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
print("-"*30)

# 購物車情境
class Cart:
    cart: list = []

    def __init__(self, name: str):
        self.name = name

cart01 = Cart("Ben的iPad")
cart02 = Cart("Mary的iPhone")

print(cart01.name)
print(cart02.name)
print(cart01.cart)