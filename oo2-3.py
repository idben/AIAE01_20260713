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
