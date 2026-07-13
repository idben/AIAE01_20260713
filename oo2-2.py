class PartyMember:
    hp: int = 30
    name: str = "村民"

    # 設定類別專屬方法
    # 第一個參數通常是物件自己, 會用 self 來代替
    def take_damage(self, damage: int):
        print(f"{self.name} 角色受到的傷害是: {damage}")
        self.hp -= damage
        

hero = PartyMember()
hero.name = "勇者"
man2 = PartyMember()
print(f"{hero.name} 角色的生命值是: {hero.hp}")
print(f"{man2.name} 角色的生命值是: {man2.hp}")
hero.take_damage(10)
man2.take_damage(1)
print(f"{hero.name} 角色的生命值是: {hero.hp}")
print(f"{man2.name} 角色的生命值是: {man2.hp}")