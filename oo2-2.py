class PartyMember:
    hp: int = 30
    name: str = "村民"

    # 設定類別專屬方法
    # 第一個參數通常是物件自己, 會用 self 來代替
    def take_damage(self, damage: int) -> None:
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

print("-"*30)

# 以簡易購物車為情境
class Cart:
    # 屬性
    ip = "172.22.33.56"
    total_money = 0

    # -> None 回傳型別是 None = 沒有回傳
    def add_to_cart(self, money: int) -> None:
        print(f"  來自 {self.ip}，加入購物車 {money} 元")
        self.total_money += money

m_no1 = Cart()
m_no1.ip = "172.22.33.1"
m_no2 = Cart()
m_no2.ip = "172.22.33.2"
m_no1.add_to_cart(50)
m_no1.add_to_cart(90)
m_no1.add_to_cart(1250)
m_no2.add_to_cart(648)
m_no2.add_to_cart(1350)
m_no2.add_to_cart(652)


print(f"來自 {m_no1.ip}，消費金額是 {m_no1.total_money} 元")
print(f"來自 {m_no2.ip}，消費金額是 {m_no2.total_money} 元")