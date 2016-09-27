print 'Welcome Riven Mains!'
print '''General Tips: Trades in lane near bushes to minimize minion damage.
FoB is for extended trades.
TLD is for short trades.
Grasp is for matchups you are not comfortable with.'''

champ=raw_input('Who are you laning against: ')

champions = {
    'kayle': 'tld',
    'swain': 'fob',
    'pantheon': 'tld',
    'karthus': 'tld',
    'singed': 'fob',
    'urgot': 'tld',
    'malphite': 'fob',
    'sion': 'fob',
    'akali': 'fob',
    'mordekaiser': 'fob',
    'rengar': 'fob',
    'jax': 'tld',
    'teemo': 'tld',
    'kennen': 'tld',
    'jarvaniv': 'fob',
    'yasuo': 'fob',
    'kled': 'fob',
    'poppy': 'fob',
    'illaoi': 'tld',
    'tryndamere': 'ss',
    'irelia': 'tld',
    'jayce': 'tld',
    'nautilis': 'fob',
    'rumble': 'fob',
    'darius': 'fob',
    'rammus': 'fob',
    'renekton': 'tld',
    'heimerdinger': 'tld',
    'olaf': 'ss',
    'graves': 'tld',
    'fiora': 'fob',
    'maokai': 'fob',
    'garen': 'fob',
    'trundle': 'tld',
    'aatrox': 'tld',
    'gangplank': 'tld',
    'drmundo': 'fob',
    'nasus': 'fob',
    'volibear': 'fob',
    'xin zhao': 'fob',
    'gnar': 'tld',
    'lissandra': 'tld',
    'ekko': 'fob',
    'tahm kench': 'tld',
    'chogath': 'fob',
    'shen': 'fob',
    'vladimir': 'tld',
    'yorick': 'fob',
    'ryze':  'tld',
    'quinn': 'dodge',
    'galio': 'fob',
    'wukong': 'tld',
}

def masteries(champ):
    for x in champions:
        if champ == x:
            print champions[champ]
            if champ == 'aatrox':
                print 'Lane: Save R2 for his revive. Force him out of lane early.'
                print 'Skill Tip: Q3 and W can interrupt his disengage.'
            if champ == 'akali':
                print 'Lane: Always have a pink ward on you.  Punish her early game.  When she shrouds use your AoE skils or drop pink.'
            if champ == 'alistar':
                print 'rush tiamat and push him to tower to deny farm.'
            if champ == 'yasuo':
                print 'Lane: Start dorans shield and rush ninja tabi.  Dont trade before lvl 3'
                print 'Skill Tip: Q3 and W can cancel Yasuo Q damage!'
            if champ == 'sion':
                print 'Skill Tip: Good match up to practice Rivens Q dancing mechanic. You can Q dance to dodge his Q!'
            if champ == 'tryndamere':
                print 'Trades: Proc SS and walk away.'
                print 'Skill Tip: Good match up to practice your burst combos.  E-AA-W-Q and then walk away or all in an walk away with stormraiders keystone.  Pro tip from 1Adrianaires1 match up series.'
            if champ == 'renekton':
                print 'Trades: Let his be the aggressor. You can win trades if he blows his cds first'
            if champ == 'illaoi':
                print 'Skill Tip: Good match up to practice Q dancing through.'
            if champ == 'heimerdinger':
                print 'Lane: Play passive and farm under tower. Tell jungler to gank often as lane will be pushed.'


if __name__ == '__main__':
    print masteries(champ)