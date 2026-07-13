Pokemon = dict[str, int]


def fight_pokemon(pokemon_one: Pokemon, pokemon_two: Pokemon) -> str:
    # pokemon_one_dps = pokemon_one["damage"] * pokemon_one["attacks_per_second"]
    # pokemon_two_dps = pokemon_two["damage"] * pokemon_two["attacks_per_second"]
    # 使用設計好用來取得總傷害的 function，取得 dps
    # 讓相同的程式碼不到處複製貼上
    pokemon_one_dps = get_pokemon_dps(pokemon_one["damage"], pokemon_one["attacks_per_second"])
    pokemon_two_dps = get_pokemon_dps(pokemon_two["damage"], pokemon_two["attacks_per_second"])
    if pokemon_one_dps > pokemon_two_dps:
        return "pokemon 1 wins"
    if pokemon_two_dps > pokemon_one_dps:
        return "pokemon 2 wins"
    return "both faint"


# 設計一個取得總傷害的 function
def get_pokemon_dps(damage, attacks_per_second):
    return damage * attacks_per_second