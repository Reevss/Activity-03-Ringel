class pokemonEv():
    def singleStatsFunction(stat_type,basestat,lvl,iv,ev,stat,nature):
        if stat_type == 'hp':
            d = (2 * basestat[0] + iv[0] + (ev[0]/4)) * (lvl/100)
            ev_needed = (((((stat/nature[0]) - d) * 400) / lvl) / 4) + 4
        if stat_type == 'attack':
            d = (2 * basestat[1] + iv[1] + (ev[1]/4)) * (lvl/100)
            ev_needed = (((((stat/nature[1]) - d) * 400) / lvl) / 4) + 4
        if stat_type == 'defense':
            d = (2 * basestat[2] + iv[2] + (ev[2]/4)) * (lvl/100)
            ev_needed = (((((stat/nature[2]) - d) * 400) / lvl) / 4) + 4
        if stat_type == 'special attack':
            d = (2 * basestat[3] + iv[3] + (ev[3]/4)) * (lvl/100)
            ev_needed = (((((stat/nature[3]) - d) * 400) / lvl) / 4) + 4
        if stat_type == 'special defense':
            d = (2 * basestat[4] + iv[4] + (ev[4]/4)) * (lvl/100)
            ev_needed = (((((stat/nature[4]) - d) * 400) / lvl) / 4) + 4
        if stat_type == 'speed':
            d = (2 * basestat[5] + iv[5] + (ev[5]/4)) * (lvl/100)
            ev_needed = (((((stat/nature[5]) - d) * 400) / lvl) / 4) + 4
        
        return ev_needed
    
    def allStatsFunction(lvl,base,ivcal,evcal,add_stat,nature):
        ev_needed = [0,0,0,0,0,0]
        for x in range(len(ev_needed)):
            d = (2 * base[x] + ivcal[x] + (evcal[x]/4)) * (lvl/100)
            ev_needed[x] = (((((add_stat[x]/nature[x]) - d) * 400) / lvl) / 4) + 4
            x = x + 1

        return ev_needed