d = input('Wpisz słowo, którego nie rozumiesz')
meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            'ROFL': 'odpowiedź na żart',
            'SHEESH': 'lekka dezaprobata',
            'CREEPY' : 'straszny, złowieszczy',
            'AGGRO' : 'stać się agresywnym/zły'
            }
if d in meme_dict.keys():
    print(meme_dict[d])
else:
    print('nie mamy jeszcze tego słowa')
