
INSERT INTO Endereco (Pais, Estado, Cidade) VALUES 
('Brasil', 'São Paulo', 'São Paulo'),
('Brasil', 'Rio de Janeiro', 'Niterói'),
('Portugal', 'Lisboa', 'Lisboa'),
('Brasil', 'Minas Gerais', 'Belo Horizonte'),
('Canadá', 'Ontário', 'Toronto');

INSERT INTO Genero (NomeGenero) VALUES 
('Fantasia'),
('Aventura'),
('Comédia'),
('Ação'),
('Drama'),
('Ficção Científica'),
('Suspense');

INSERT INTO Obra (Titulo, Sinopse, ClassEtaria, TipoObra) VALUES 
('Como Treinar o Seu Dragão', 'Soluço é um jovem viking que não tem capacidade para lutar contra os dragões, como é a tradição local. Sua vida muda quando ele ajuda um dragão que lhe mostra toda a verdade. Juntos, eles tentam provar que dragões e humanos podem ser amigos.', '10', 'Filme'),
('Interestelar', 'As reservas naturais da Terra estão chegando ao fim e um grupo de astronautas recebe a missão de verificar possíveis planetas para receberem a população mundial, possibilitando a continuação da espécie. Cooper é chamado para liderar o grupo e aceita a missão sabendo que pode nunca mais ver os filhos. Ao lado de Brand, Jenkins e Doyle, ele seguirá em busca de um novo lar.', '10', 'Filme'),
('Breaking Bad', 'narra a transformação de Walter White (Bryan Cranston), um professor de química frustrado e com câncer terminal, em um impiedoso produtor de metanfetamina. Para garantir o futuro financeiro de sua família, ele se alia ao ex-aluno Jesse Pinkman (Aaron Paul), mergulhando no perigoso mundo do crime em Albuquerque.', '16', 'Série'),
('Jogos Vorazes', 'Na região antigamente conhecida como América do Norte, a Capital de Panem controla 12 distritos e os força a escolher um garoto e uma garota, conhecidos como tributos, para competir em um evento anual televisionado. Todos os cidadãos assistem aos temidos jogos, no qual os jovens lutam até a morte, de modo que apenas um saia vitorioso. A jovem Katniss Everdeen, do Distrito 12, confia na habilidade de caça e na destreza com o arco, além dos instintos aguçados, nesta competição mortal.', '14', 'Filme'),
('Maze Runner', 'Em um futuro apocalíptico, o jovem Thomas é escolhido para enfrentar o sistema. Ele acorda num escuro elevador em movimento e não consegue se lembrar nem de seu nome. Na comunidade isolada em que foi abandonado, Thomas conhece outros garotos que passaram pela mesma situação. Para conseguir escapar, ele precisa descobrir os sombrios segredos guardados in sua mente e correr muito.', '14', 'Filme'),
('Better Call Saul', 'Advogado trapaceiro Jimmy McGill transforma-se no icônico e polêmico Saul.', '14', 'Série'),
('The Mandalorian', 'Caçador de recompensas protege criança misteriosa em uma galáxia perigosa.', '12', 'Série'),
('The Boys', 'Vigilantes enfrentam super-heróis corruptos que abusam de seus poderes especiais.', '18', 'Série'),
('Okja', 'Menina luta para salvar criatura gigante de uma corporação cruel.', '10', 'Filme'),
('Revolution', 'Sobreviventes buscam respostas em mundo onde toda eletricidade parou misteriosamente.', '10', 'Série');

INSERT INTO Ator (Nome, Nacionalidade) VALUES 
('Mason Thames', 'Americano'),
('Nico Parker', 'Britânica'),
('Matthew McConaughey', 'Americano'),
('Wes Bentley', 'Americano'),
('Bryan Cranston', 'Americano'),
('Giancarlo Esposito', 'Americano'),
('Jennifer Lawrence', 'Americano'),
('Dylan OBrien', 'Americano');

INSERT INTO Catalogo DEFAULT VALUES;
INSERT INTO Catalogo DEFAULT VALUES;
INSERT INTO Catalogo DEFAULT VALUES;
INSERT INTO Catalogo DEFAULT VALUES;
INSERT INTO Catalogo DEFAULT VALUES;

INSERT INTO Plano (Nome, Valor, DuracaoMeses, Beneficios) VALUES 
('Padrão com anuncios', 20.90, 1, 'Veja filme em qualidade FHD com anuncios!'),
('Padrão', 44.90, 1 , 'Veja filmes em qualidade FHD!'),    
('Premium', 59.90, 1, 'Veja filmes em qualidade UHD e com HDR!');

INSERT INTO Conta (Email, Senha, IDEndereco) VALUES 
('ana@gmail.com', 'Ana123', 1),
('bruno@gmail.com', 'Bruno321', 2),
('caio@gmail.com', '0C_20', 3),
('diana@gmail.com', 'Diana951', 4),
('edna@gmail.com', 'Edna123', 5);

INSERT INTO Perfil (Nome, Avatar, IDConta) VALUES 
('Ana', 'Red_3', 1),
('Bruno', 'Cavaleiro_2', 2),
('Caio', 'Dragao_5', 3),
('Diana', 'Princesa_1', 4),
('Edna', 'Green_4', 5),
('Fernando', 'Red_3', 4),
('Visitas', 'Divertidamente_3', 2),
('Maria', 'Princesa_1', 3),
('Gabriel', 'Marvel_2', 2);

INSERT INTO GeneroObra (IDGenero, IDObra) VALUES 
(1, 1), (2, 1), (3, 1),
(6, 2), (5, 2),
(5, 3), (7, 3),
(4, 4), (6, 4),
(4, 5), (7, 5),
(3, 6),
(4, 7),
(2, 8),
(7, 9),
(5, 10);

INSERT INTO Filme (DuracaoMinutos, AnoLancamento, IDObra) VALUES 
(125, 2025, 1),
(169, 2014, 2),
(144, 2012, 4),
(113, 2014, 5),
(120, 2017, 9);

INSERT INTO Serie (QtdTemporadas, IDObra) VALUES 
(5, 3),
(1, 6),
(1, 7),
(1, 8),
(1, 10);

INSERT INTO Temporada (NumTemporada, QtdEpisodios, AnoLancamento, IDSerie) VALUES 
(1, 2, 2008, 1),
(2, 2, 2009, 1),
(3, 2, 2010, 1),
(4, 2, 2011, 1),
(5, 2, 2012, 1),
(1, 1, 2015, 2),
(1, 1, 2019, 3),
(1, 1, 2019, 4),
(1, 1, 2012, 5);

INSERT INTO Episodio (IDTemporada, Titulo, DuracaoMinutos, Sinopse) VALUES 
(1, 'Piloto', 58, ' Professor com câncer começa a fabricar metanfetamina no deserto.'), 
(1, 'O Gato está no Saco...', 48, 'Walt e Jesse lidam com dois traficantes no porão.'),
(2, 'Sete Trinta e Sete', 47, 'Tuco sequestra Walt e Jesse após o negócio falhar.'),
(2, 'Na Grelha', 47, 'Walt e Jesse tentam escapar da casa do tio de Tuco.'),
(3, 'No Más', 47, 'Walt lida com o divórcio enquanto Skyler descobre segredos.'),
(3, 'Cavalo sem Nome', 47, 'Walt tenta se reconciliar com a família após o acidente.'),
(4, 'Estilete', 47, 'Gus mata um capanga brutalmente para enviar um aviso.'),
(4, 'Trinta e Oito Cano Curto', 47, 'Walt compra uma arma ilegal para tentar matar Gus.'),
(5, 'Viver Livre ou Morrer', 43, 'Walt usa um superímã para destruir provas da polícia.'),
(5, 'Madrigal', 47, 'Mike e Walt formam uma nova parceria para o tráfico.'),
(6, 'Uno', 50, 'Advogado trapaceiro Jimmy McGill transforma-se no icônico e polêmico Saul.'),
(7, 'The Mandalorian', 40, 'Caçador de recompensas protege criança misteriosa em uma galáxia perigosa.'),
(8, 'The Name of The Game', 55, 'Vigilantes enfrentam super-heróis corruptos que abusam de seus poderes especiais.'),
(9, 'Piloto', 42, 'Sobreviventes buscam respostas em mundo onde toda eletricidade parou misteriosamente.');

INSERT INTO Elenco (IDObra) VALUES 
(1), (2), (3), (4), (5), (6), (7), (8), (9), (10);

INSERT INTO AtoreElenco (NomePersonagem, IDElenco, IDAtor) VALUES 
('Soluço', 1, 1),
('Astrid', 1, 2),
('Cooper', 2, 3),
('Doyle', 2, 4),
('Walter White', 3, 5),
('Gus Fring', 3, 6),
('Katniss Everdeen', 4, 7),
('Seneca Crane', 4, 4),
('Thomas', 5, 8),
('Jorge', 5, 6),
('Gus Fring', 6, 6),
('Moff Gideon', 7, 6),
('Stan Edgar', 8, 6),
('Frank Dawson', 9, 6),
('Tom Neville', 10, 6);

INSERT INTO Historico (DataHora, IDPerfil, IDObra) VALUES 
('2026-03-25 08:45:12', 7, 4),
('2026-03-30 10:00:05', 8, 5),
('2026-04-01 15:20:33', 8, 2),
('2026-04-03 23:59:59', 2, 1),
('2026-04-04 09:12:11', 2, 3),
('2026-04-05 18:05:42', 6, 2),
('2026-04-05 22:15:08', 4, 4),
('2026-04-06 12:30:00', 6, 4),
('2026-04-06 14:40:00', 5, 2),
('2026-04-06 14:44:52', 3, 2);

INSERT INTO ObraCatalogo (IDObra, IDCatalogo) VALUES 
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
(2, 2), (3, 2), (4, 2), (5, 2),
(2, 3), (4, 3),
(1, 4),
(1, 5), (3, 5), (5, 5),
(6, 1), (7, 1), (8, 1), (9, 1), (10, 1);

INSERT INTO PerfilCatalogo (IDCatalogo, IDPerfil) VALUES 
(1, 1),
(5, 2),
(1, 3),
(3, 4),
(1, 5),
(3, 6),
(1, 7),
(2, 8),
(1, 9);

INSERT INTO Assinatura (DataInicio, DataFim, IDPlano, IDConta) VALUES 
('2025-10-01', '2025-11-01', 1, 1),
('2025-11-01', '2025-12-01', 2, 1),
('2025-12-01', '2026-01-01', 3, 1),
('2026-02-01', '2026-03-01', 3, 1),
('2026-03-03', '2026-04-03', 2, 2),
('2026-03-15', '2026-04-15', 2, 3),
('2026-04-01', '2026-05-01', 3, 1),
('2026-04-01', '2026-05-01', 1, 4),
('2026-04-02', '2026-05-02', 2, 5),
('2026-04-04', '2026-05-04', 1, 2);