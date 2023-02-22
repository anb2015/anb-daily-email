from random import choice

adjectives = ['infinite', 'ponderous', 'prodigious', 'monumental', 'vast', 'unfathomed', 'ponderous', 'heroic',
              'colossal', 'pyramidal', 'astronomical', 'astronomic', 'stratospheric', 'cosmic', 'galactic', 'mighty',
              'strong', 'bold', 'fort', 'steer', 'steeve', 'valiant', 'stalwart', 'strengthful', 'stout', 'pithy',
              'mighted', 'strengthy', 'Tarzanesque', 'Tarzan-like']

staff = ['agents', 'attendants', 'clerks', 'laborers', 'members', 'operators', 'representatives', 'staff members',
         'workers', 'apprentices', 'assistants', 'cogs', 'hands', 'jobholders', 'salespersons', 'company persons',
         'craftspersons', 'desk jockeys', 'hired guns', 'hired hands', 'wage earners', 'working stiffs']

# gpt sourced list
industries = ["Industries", "Enterprises", "Manufacturing", "Works", "Incorporated", "Holdings", "International", "Corporation", "Group", "Ventures"]

# gpt sourced list
entity = ["LLC", "Ltd.", "Inc.", "Corp.", "PLC", "GmbH", "AG", "S.p.A.", "Co.", "LLP"]

described_staff = f"{choice(adjectives)} {choice(staff)} at ANB {choice(industries)}, {choice(entity)}"
