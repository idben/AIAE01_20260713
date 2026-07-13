class PartyMember:
    name = "村民"
    agility: int = 12
    armor_weight: int = 3

    def get_turn_speed(self) -> int:
        return self.agility - self.armor_weight
    
    def action(self) -> str:
        # 取得 turn_speed，組合出以下句子
        # XXXX 先攻 / XXXX 後攻 / XXXX 防禦
        # >= 10     /  0~10 / < 0
        action_str = "防禦"
        turn_speed = self.get_turn_speed()
        if turn_speed >= 10:
            action_str = "先攻"
        elif 0 <= turn_speed < 10:
            action_str = "後攻"
        return f"{self.name} {action_str}"


hero = PartyMember()
hero.name = "勇者"
hero.agility = 20
hero.armor_weight = 5
tank = PartyMember()
tank.name = "重騎士"
tank.agility = 5
tank.armor_weight = 10

print(hero.action())
print(tank.action())


print("-"*30)

# 購物車情境
# [
#     {"name": "雞蛋", "price": 7, "amount": 8}
# ]

class Cart:
    name: str = "機器 unknow"
    cart: list = []

    def add_to_cart(self, name, price, amount) -> None:
        # .add_to_cart("雞蛋", 7, 8) # 預計的使用方式
        self.cart.append({
            "name": name,
            "price": price,
            "amount": amount,
        })

    def get_sum(self) -> int:
        total_money = 0

        for item in self.cart:
            total_money += item["price"] * item["amount"]

        return total_money

cart1 = Cart()
cart1.name = "Ben iPad"
cart1.add_to_cart("牛肉調理包", 258, 1)
cart1.add_to_cart("B 群", 899, 2)
cart1.add_to_cart("乾麵", 358, 3)

print(cart1.cart)
print(f"{cart1.name} 消費總金額是 {cart1.get_sum()}")