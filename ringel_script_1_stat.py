class pokemonStats():
    def hp_statsfunction(lvl,hp,iv,ev):
        total_hp = (((2 * hp + iv[0] + (ev[0]/4)) * lvl) / 100) + lvl + 10
        return total_hp
    def other_statsfunction(atk,defense,spAtk,spDef,spd,iv,ev,lvl,nature):
        str = [atk,defense,spAtk,spDef,spd,]
        x = 0
        for x in range(len(str)):
            str[x] = (((((2 * str[x] + iv[x+1] + (ev[x+1]/4)) * lvl) / 100) + 5)) * nature[x+1]
            x = x + 1    
        return str
