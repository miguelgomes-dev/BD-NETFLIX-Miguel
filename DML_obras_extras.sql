INSERT INTO Genero (NomeGenero)
SELECT 'Gênero Especial ' || i 
FROM generate_series(1, 1000) as i;

INSERT INTO Obra (Titulo, Sinopse, ClassEtaria, TipoObra)
SELECT 
    'Nova Obra ' || i,
    'Sinopse da nova obra número ' || i,
    (ARRAY['Livre', '12', '14', '16', '18'])[floor(random() * 5 + 1)],
    (ARRAY['Filme', 'Série'])[floor(random() * 2 + 1)]
FROM generate_series(1, 1000000) as i;

INSERT INTO GeneroObra (IDGenero, IDObra)
SELECT 
    (i % 1000) + 1,
    i
FROM generate_series(1, 1000000) as i;