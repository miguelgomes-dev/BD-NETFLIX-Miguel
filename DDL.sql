CREATE TABLE Endereco (
    IDEndereco SERIAL PRIMARY KEY,
    Pais VARCHAR(100) NOT NULL,
    Estado VARCHAR(100) NOT NULL,
    Cidade VARCHAR(100) NOT NULL
);

CREATE TABLE Genero (
    IDGenero SERIAL PRIMARY KEY,
    NomeGenero VARCHAR(50) NOT NULL
);

CREATE TABLE Obra (
    IDObra SERIAL PRIMARY KEY,
    Titulo VARCHAR(250) NOT NULL,
    Sinopse TEXT,
    ClassEtaria VARCHAR(10),
    TipoObra VARCHAR(50)
);

CREATE TABLE Ator (
    IDAtor SERIAL PRIMARY KEY,
    Nome VARCHAR(150) NOT NULL,
    Nacionalidade VARCHAR(100)
);

CREATE TABLE Catalogo (
    IDCatalogo SERIAL PRIMARY KEY
);

CREATE TABLE Plano (
    IDPlano SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Valor NUMERIC(10, 2) NOT NULL,
    DuracaoMeses INT NOT NULL,
    Beneficios TEXT
);

CREATE TABLE Conta (
    IDConta SERIAL PRIMARY KEY,
    Email VARCHAR(200) UNIQUE NOT NULL,
    Senha VARCHAR(250) NOT NULL,
    IDEndereco INT NOT NULL,
    FOREIGN KEY (IDEndereco) REFERENCES Endereco(IDEndereco)
);

CREATE TABLE Perfil (
    IDPerfil SERIAL PRIMARY KEY,
    Nome VARCHAR(150) NOT NULL,
    Avatar VARCHAR(80),
    IDConta INT NOT NULL,
    FOREIGN KEY (IDConta) REFERENCES Conta(IDConta)
);

CREATE TABLE GeneroObra (
    IDGeneroObra SERIAL PRIMARY KEY,
    IDGenero INT NOT NULL,
    IDObra INT NOT NULL,
    FOREIGN KEY (IDGenero) REFERENCES Genero(IDGenero),
    FOREIGN KEY (IDObra) REFERENCES Obra(IDObra)
);

CREATE TABLE Filme (
    IDFilme SERIAL PRIMARY KEY,
    DuracaoMinutos INT NOT NULL,
    AnoLancamento INT,
    IDObra INT UNIQUE NOT NULL,
    FOREIGN KEY (IDObra) REFERENCES Obra(IDObra)
);

CREATE TABLE Serie (
    IDSerie SERIAL PRIMARY KEY,
    QtdTemporadas INT,
    IDObra INT UNIQUE NOT NULL,
    FOREIGN KEY (IDObra) REFERENCES Obra(IDObra)
);

CREATE TABLE Temporada (
    IDTemporada SERIAL PRIMARY KEY,
    NumTemporada INT NOT NULL,
    QtdEpisodios INT,
    AnoLancamento INT,
    IDSerie INT NOT NULL,
    FOREIGN KEY (IDSerie) REFERENCES Serie(IDSerie)
);

CREATE TABLE Episodio (
    IDEpisodio SERIAL PRIMARY KEY,
    IDTemporada INT NOT NULL,
    Titulo VARCHAR(250) NOT NULL,
    DuracaoMinutos INT NOT NULL,
    Sinopse TEXT,
    FOREIGN KEY (IDTemporada) REFERENCES Temporada(IDTemporada)
);

CREATE TABLE Elenco (
    IDElenco SERIAL PRIMARY KEY,
    IDObra INT NOT NULL,
    FOREIGN KEY (IDObra) REFERENCES Obra(IDObra)
);

CREATE TABLE AtoreElenco (
    IDAtoreElenco SERIAL PRIMARY KEY,
    NomePersonagem VARCHAR(150),
    IDElenco INT NOT NULL,
    IDAtor INT NOT NULL,
    FOREIGN KEY (IDElenco) REFERENCES Elenco(IDElenco),
    FOREIGN KEY (IDAtor) REFERENCES Ator(IDAtor)
);

CREATE TABLE Historico (
    IDHistorico SERIAL PRIMARY KEY,
    DataHora TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    IDPerfil INT NOT NULL,
    IDObra INT NOT NULL,
    FOREIGN KEY (IDPerfil) REFERENCES Perfil(IDPerfil),
    FOREIGN KEY (IDObra) REFERENCES Obra(IDObra)
);

CREATE TABLE ObraCatalogo (
    IDObraCatalogo SERIAL PRIMARY KEY,
    IDObra INT NOT NULL,
    IDCatalogo INT NOT NULL,
    FOREIGN KEY (IDObra) REFERENCES Obra(IDObra),
    FOREIGN KEY (IDCatalogo) REFERENCES Catalogo(IDCatalogo)
);

CREATE TABLE PerfilCatalogo (
    IDPerfilCatalogo SERIAL PRIMARY KEY,
    IDCatalogo INT NOT NULL,
    IDPerfil INT NOT NULL,
    FOREIGN KEY (IDCatalogo) REFERENCES Catalogo(IDCatalogo),
    FOREIGN KEY (IDPerfil) REFERENCES Perfil(IDPerfil)
);

CREATE TABLE Assinatura (
    IDAssinatura SERIAL PRIMARY KEY,
    DataInicio DATE NOT NULL,
    DataFim DATE,
    IDPlano INT NOT NULL,
    IDConta INT NOT NULL,
    FOREIGN KEY (IDPlano) REFERENCES Plano(IDPlano),
    FOREIGN KEY (IDConta) REFERENCES Conta(IDConta)
);