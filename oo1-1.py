def remove_fainted_party_member(party_hp: list[int]) -> list[int]:
    h: list[int] = []
    for p in party_hp:
        if p > 0:
            h.append(p)
    return h

members_hp = [100, 60, 0]
result = remove_fainted_party_member(members_hp)
print(result)