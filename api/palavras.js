const palavras = [
  'casa', 'jardim', 'montanha', 'oceano', 'estrela', 'floresta', 'cidade', 'campo',
  'ponte', 'caminho', 'aventura', 'sonho', 'liberdade', 'alegria', 'amizade', 'coragem',
  'esperança', 'sabedoria', 'natureza', 'harmonia', 'beleza', 'simplicidade', 'energia',
  'criatividade', 'descoberta', 'transformação', 'equilíbrio', 'prosperidade', 'gratidão',
  'inovação', 'inspiração', 'paixão', 'determinação', 'confiança', 'serenidade', 'felicidade',
  'Brasil', 'violão', 'saudade', 'caipirinha', 'futebol', 'praia', 'carnaval', 'açaí'
];

function palavraAleatoria() {
  const indice = Math.floor(Math.random() * palavras.length);
  return palavras[indice];
}

module.exports = { palavraAleatoria };