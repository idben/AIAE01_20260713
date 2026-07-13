# 購物車情境
class Cart:
    # 在類別下，不是在建構子中，定義的變數就是類別變數
    # 類別變數是所有實體共用
    # 因此由其中一個實體修改，其他的實體的類別變數也會跟著改變
    cart: list = []

    def __init__(self, name: str):
        self.name = name
        # self.cart = [] 
        # 目前類別變數 cart  應該是要做成實例變數較恰當
    def add_to_cart(self, name, price, amount) -> None:
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

cart01 = Cart("Ben的iPad")
cart02 = Cart("Mary的iPhone")

print(cart01.name)
print(cart02.name)

cart01.add_to_cart("青茶", 35, 2)

print(cart01.cart)
print(cart02.cart)
print("-"*30)


# 寶可夢情境
class Eevee:
    main_kind = "伊布"
    def __init__(self, kind: str):
        self.kind = kind

eevee01 = Eevee("未進化伊布")
eevee02 = Eevee("雷伊布")
eevee03 = Eevee("月亮伊布")

print(f"{eevee01.kind} 的初始種族是 {eevee01.main_kind}")
print(f"{eevee02.kind} 的初始種族是 {eevee02.main_kind}")
print(f"{eevee03.kind} 的初始種族是 {eevee03.main_kind}")