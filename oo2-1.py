class PartyMember:
    kind: str = "human"
    hp: int = 20
    mp: int = 8
    level: int = 1


# hero = {
#     "kind": "human",
#     "name": "Ben",
#     "hp": 20,
#     "mp": 8,
#     "level": 1
# }

hero = PartyMember()
# hero["hp"] = 20

mage = {
    "kind": "human",
    "name": "Mary",
    "hp": 30,
    "mp": 50,
    "level": 5
}

print(hero)
print(mage)