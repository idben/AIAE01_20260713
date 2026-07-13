def remove_fainted_party_member(party_hp):
    active_hps = []
    for hp in party_hp:
        if hp > 0:
            active_hps.append(hp)
    return active_hps

members_hp = [100, 60, 0]
result = remove_fainted_party_member(members_hp)
print(result)