cidade = str(input('em qual cidade você mora: ')).lower().strip()
if cidade[:5].upper() == 'SANTO':
    print(f'{cidade} tem santo no nome')
else:
    print(f'{cidade} não tem santo')
if cidade[:3].upper() == 'SAO':
    print(f'{cidade} tem sao no nome')
else:
    print(f'{cidade} não tem sao no nome')

