palavras = [
    'casa', 'jardim', 'montanha', 'oceano', 'estrela', 'floresta', 'cidade', 'campo',
    'ponte', 'caminho', 'aventura', 'sonho', 'liberdade', 'alegria', 'amizade', 'coragem',
    'esperança', 'sabedoria', 'natureza', 'harmonia', 'beleza', 'simplicidade', 'energia',
    'criatividade', 'descoberta', 'transformação', 'equilíbrio', 'prosperidade', 'gratidão',
    'inovação', 'inspiração', 'paixão', 'determinação', 'confiança', 'serenidade', 'felicidade',
    'Brasil', 'violão', 'saudade', 'caipirinha', 'futebol', 'praia', 'carnaval', 'açaí'
]

import random

def palavra_aleatoria():
    return random.choice(palavras)