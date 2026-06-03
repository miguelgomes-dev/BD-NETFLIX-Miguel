-- ========================================
-- ÍNDICES PARA OTIMIZAR PERFORMANCE
-- ========================================

-- Índice 1: Busca de obras por gênero (OPERAÇÃO CRÍTICA)
-- Usado constantemente no menu do usuário
CREATE INDEX idx_generoobra_idgenero ON GeneroObra(IDGenero);

-- Índice 2: Listar perfis de uma conta
CREATE INDEX idx_perfil_idconta ON Perfil(IDConta);

-- Índice 3: Listar temporadas de uma série
CREATE INDEX idx_temporada_idserie ON Temporada(IDSerie);

-- Índice 4: Buscar conta pelo email (autenticação)
CREATE INDEX idx_conta_email ON Conta(Email);

-- Índice 5: Composite index para buscas de obras por gênero
CREATE INDEX idx_generoobra_composite ON GeneroObra(IDGenero, IDObra);

-- ========================================
-- QUERY CRÍTICA PARA APRESENTAÇÃO
-- ========================================
-- Esta query demonstra a operação mais frequente:
-- Listar todas as obras de um gênero com seus detalhes

-- Versão SEM índice (plano antigo):
-- SELECT DISTINCT o.IDObra, o.Titulo, o.Sinopse, o.ClassEtaria, o.TipoObra
-- FROM Obra o
-- INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
-- WHERE go.IDGenero = 1
-- ORDER BY o.Titulo;

-- Versão COM índice (plano otimizado):
SELECT DISTINCT 
    o.IDObra, 
    o.Titulo, 
    o.Sinopse, 
    o.ClassEtaria, 
    o.TipoObra,
    (CASE 
        WHEN f.IDFilme IS NOT NULL THEN f.DuracaoMinutos || ' min'
        WHEN s.IDSerie IS NOT NULL THEN s.QtdTemporadas || ' temporada(s)'
        ELSE 'N/A'
    END) AS duracao_ou_temporadas
FROM Obra o
INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
LEFT JOIN Filme f ON o.IDObra = f.IDObra
LEFT JOIN Serie s ON o.IDObra = s.IDObra
WHERE go.IDGenero = 1
ORDER BY o.Titulo;

-- ========================================
-- QUERY PARA VERIFICAR DESEMPENHO
-- Use EXPLAIN ANALYZE antes e depois de criar os índices
-- ========================================

-- Teste 1: Buscar obras de um gênero (com EXPLAIN)
EXPLAIN ANALYZE
SELECT DISTINCT o.IDObra, o.Titulo, o.ClassEtaria
FROM Obra o
INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
WHERE go.IDGenero = 1
ORDER BY o.Titulo;

-- Teste 2: Listar todos os perfis de uma conta
EXPLAIN ANALYZE
SELECT IDPerfil, Nome, Avatar 
FROM Perfil 
WHERE IDConta = 1
ORDER BY Nome;

-- Teste 3: Query complexa - Contas com seus planos
EXPLAIN ANALYZE
SELECT 
    c.IDConta, 
    c.Email, 
    a.IDPlano,
    pl.Nome AS NomePlano,
    pl.Valor
FROM Conta c
LEFT JOIN Assinatura a ON c.IDConta = a.IDConta
LEFT JOIN Plano pl ON a.IDPlano = pl.IDPlano
WHERE c.IDConta > 0
ORDER BY c.IDConta;

-- ========================================
-- QUERIES ADICIONAIS PARA DEMONSTRAÇÃO
-- ========================================

-- Query 1: Contar obras por gênero (para relatório)
SELECT 
    g.IDGenero,
    g.NomeGenero,
    COUNT(DISTINCT go.IDObra) AS QuantidadeObras
FROM Genero g
LEFT JOIN GeneroObra go ON g.IDGenero = go.IDGenero
GROUP BY g.IDGenero, g.NomeGenero
ORDER BY QuantidadeObras DESC;

-- Query 2: Listar usuários e seus perfis
SELECT 
    c.IDConta,
    c.Email,
    COUNT(p.IDPerfil) AS QuantidadePerfis
FROM Conta c
LEFT JOIN Perfil p ON c.IDConta = p.IDConta
GROUP BY c.IDConta, c.Email
ORDER BY c.IDConta;

-- Query 3: Série com mais episódios
SELECT 
    o.Titulo,
    s.QtdTemporadas,
    COUNT(e.IDEpisodio) AS TotalEpisodios
FROM Obra o
INNER JOIN Serie s ON o.IDObra = s.IDObra
INNER JOIN Temporada t ON s.IDSerie = t.IDSerie
INNER JOIN Episodio e ON t.IDTemporada = e.IDTemporada
GROUP BY o.Titulo, s.QtdTemporadas
ORDER BY TotalEpisodios DESC;

-- Query 4: Obras agrupadas por classificação etária
SELECT 
    ClassEtaria,
    COUNT(*) AS Quantidade,
    COUNT(CASE WHEN TipoObra = 'Filme' THEN 1 END) AS Filmes,
    COUNT(CASE WHEN TipoObra = 'Série' THEN 1 END) AS Series
FROM Obra
GROUP BY ClassEtaria
ORDER BY ClassEtaria;
