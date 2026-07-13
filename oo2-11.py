# 購物車情境
class Cart:
    # 在類別下，不是在建構子中，定義的變數就是類別變數
    # 類別變數是所有實體共用
    # 因此由其中一個實體修改，其他的實體的類別變數也會跟著改變
    cart: list = []

    def __init__(self, name: str):
        self.name = name
        # self.cart = [] 
        # # 目前類別變數 cart  應該是要做成實例變數較恰當
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