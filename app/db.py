# db.py

# password in plain text is "1q2w3e4r"


userz = {
    'nra': {
        'name':'nra',
        'rol':'admin',
        'password':'pbkdf2:sha256:150000$odpBdApk$edcb7f9a952e4330db6b624dfe67c552c533863e72f0e3162a3db4302a335470'
        },
    'acpv': {
        'name':'acpv',
        'rol':'user',
        'password':'pbkdf2:sha256:150000$odpBdApk$edcb7f9a952e4330db6b624dfe67c552c533863e72f0e3162a3db4302a335470'
        }
}

netz = [
    { 'id': 1, 'network': '1.0.0.0/8', 'comment': 'bla' },
    { 'id': 2, 'network': '2.0.0.0/8', 'comment': 'blabla' },
    { 'id': 3, 'network': '3.0.0.0/8', 'comment': 'blablabla' },
]

sitez = [
    { 'id': 1, 'site': 'RED', 'comment': 'bla' },
    { 'id': 2, 'site': 'BLUE', 'comment': 'blabla' },
    { 'id': 3, 'site': 'GREEN', 'comment': 'blablabla' },
]