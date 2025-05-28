import re

def normalizaHoras(ficText, ficNorm):
    estructura = [
        # Formato dos puntos 
        (re.compile(r'(\d{1,2}):(\d{1,2})'), lambda m: f'{int(m.group(1)):02}:{int(m.group(2)):02}'),

        # Formato h y m 
        (re.compile(r'(\d{1,2})h(\d{1,2})m'), lambda m: f'{int(m.group(1)):02}:{int(m.group(2)):02}'),

    	# Formato h 
        (re.compile(r'(\d{1,2})(?:h| de la (mañana|tarde))'), 
         lambda m: f'{(int(m.group(1)) + 12) if m.group(2) == "tarde" and int(m.group(1)) < 12 else (0 if m.group(1) == "12" and m.group(2) == "mañana" else int(m.group(1))):02}:00'),

        # Formato y cuarto (opcional de la mañana/tarde)
        (re.compile(r'(\d{1,2}) y cuarto(?: de la (mañana|tarde))?'), 
         lambda m: f'{(int(m.group(1)) + 12) if m.group(2) == "tarde" and int(m.group(1)) < 12 else int(m.group(1)):02}:15'),

        # Formato y media (opcional de la mañana/tarde)
        (re.compile(r'(\d{1,2}) y media(?: de la (mañana|tarde))?'), 
         lambda m: f'{(int(m.group(1)) + 12) if m.group(2) == "tarde" and int(m.group(1)) < 12 else int(m.group(1)):02}:30'),

        # Formato menos cuarto (opcional de la mañana/tarde)
        (re.compile(r'(\d{1,2}) menos cuarto(?: de la (mañana|tarde))?'), 
         lambda m: f'{(int(m.group(1)) - 1 + 12) if m.group(2) == "tarde" and int(m.group(1)) < 12 else int(m.group(1)) - 1:02}:45'),

        # Formato en punto (opcional de la mañana/tarde)
        (re.compile(r'(\d{1,2}) en punto(?: de la (mañana|tarde))?'),
         lambda m: f'{(int(m.group(1)) + 12) if m.group(2) == "tarde" and int(m.group(1)) < 12 else int(m.group(1)):02}:00'),

        # 12 de la noche → 00:00
        (re.compile(r'12 de la noche'), lambda m: '00:00'),
    ]

    with open(ficText, 'r') as input, open(ficNorm, 'w') as output:
        for line in input: 
            for x, reemplece in estructura:
                line = x.sub(reemplece, line)
            output.write(line)

normalizaHoras('horas.txt', 'horasNorm.txt')  # Ejemplo de uso