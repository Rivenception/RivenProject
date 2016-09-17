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

if __name__ == '__main__':
    print (champions[champ]) 
