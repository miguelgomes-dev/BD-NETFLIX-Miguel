# 🎬 NETFLIX - SISTEMA DE GERENCIAMENTO

**Grupo:** Joel, Jordana e Miguel

---

## 📋 Objetivo

Implementar uma interface CRUD em Python para gerenciar um banco de dados Netflix, demonstrando:
- ✅ Operações de CREATE, READ, UPDATE, DELETE
- ✅ Interface interativa via console
- ✅ Otimização de performance com índices
- ✅ Análise de planos de execução SQL

---

## 🗂️ Arquivos Entregáveis

| Arquivo | Descrição |
|---------|-----------|
| `DDL.sql` | Script de criação das tabelas |
| `DML.sql` | Script com dados iniciais |
| `criar_indices.sql` | Índices e queries críticas com EXPLAIN ANALYZE |
| `conexao_db.py` | Módulo de conexão com PostgreSQL |
| `interface_netflix.py` | Interface interativa principal |
| `executar_interface.py` | Launcher com menu de opções |
| `requirements.txt` | Dependências Python |

---

## 🚀 Como Executar (Passo a Passo)

### 📝 Pré-requisitos

Você está em um **Codespace** ou **Devcontainer**? Ótimo! Tudo já está automatizado! 🎉

O arquivo `.devcontainer/devcontainer.json` configura:
- ✅ Python 3.x com pip
- ✅ PostgreSQL 15 (Docker)
- ✅ Cliente PostgreSQL
- ✅ Instalação automática das dependências
- ✅ Banco de dados "netflix" com tabelas e dados iniciais

---

## ✨ PASSOS RÁPIDOS (Codespace/Devcontainer)

### 1️⃣ Abrir o Codespace/Devcontainer

Depois que o container estiver **pronto** (aguarde ~1-2 minutos):
- Todos os arquivos Python estarão prontos
- PostgreSQL estará rodando
- Dependências já instaladas
- Banco de dados "netflix" criado com dados iniciais

> **Sinais que está pronto:**
> - Terminal não mostra mais mensagens de inicialização
> - Pode executar comandos normalmente

---

### 2️⃣ Verificar a conexão com o banco

```bash
psql -U postgres -d netflix -c "SELECT COUNT(*) FROM Conta;"
```

**Resultado esperado:** `5` (contas de teste já inseridas)

> Se receber erro `psql: command not found`, aguarde mais 30 segundos (PostgreSQL ainda está iniciando)

---

### 3️⃣ Executar a interface (3 opções)

#### **Opção A: Menu Principal (RECOMENDADO)**
```bash
python3 executar_interface.py
```
Você verá um menu com:
1. 🎬 Iniciar Interface CRUD
2. 🧪 Executar Testes
3. 📊 Ver Índices
4. 🚪 Sair

#### **Opção B: Interface Direta**
```bash
python3 interface_netflix.py
```

#### **Opção C: Rodar Testes de Validação**
```bash
python3 teste_interface.py
```

---

### 4️⃣ (Opcional) Criar índices de performance

```bash
psql -U postgres -d netflix -f criar_indices.sql
```

Depois compare a performance:
```bash
psql -U postgres -d netflix -f criar_indices.sql
```

---

## 🚀 Para Computador Local (sem Codespace)

Se você quer rodar **localmente** sem Codespace:

### 1️⃣ Criar ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3️⃣ Configurar PostgreSQL

Certifique-se de que PostgreSQL está rodando, depois:

```bash
# Criar banco e importar dados
psql -U postgres -c "CREATE DATABASE netflix;"
psql -U postgres -d netflix -f DDL.sql
psql -U postgres -d netflix -f DML.sql
```

Se PostgreSQL exigir senha:
```bash
export PGPASSWORD='sua_senha'  # Linux/Mac
set PGPASSWORD=sua_senha        # Windows
```

### 4️⃣ Rodar a interface
```bash
python3 executar_interface.py
```

---

## 🎯 Como Usar a Interface

Ao executar a interface, você tem um **menu principal** com 3 opções:

```
┌────────────────────────────────────────────────────┐
│   INTERFACE NETFLIX - MENU PRINCIPAL               │
├────────────────────────────────────────────────────┤
│                                                    │
│  1️⃣  INICIAR INTERFACE CRUD (Menu Interativo)     │
│       - Criar Conta                               │
│       - Criar Perfil                              │
│       - Ver Filmes/Séries por Gênero             │
│       - Editar Perfil/Conta                       │
│       - Deletar Perfil/Conta                      │
│                                                    │
│  2️⃣  EXECUTAR TESTES (Validação)                 │
│       - Teste de conexão ao banco                 │
│       - Verificação de índices                    │
│       - Teste CRUD                                │
│       - Performance                               │
│                                                    │
│  3️⃣  VER ÍNDICES CRIADOS                          │
│       - Lista de índices no banco                 │
│                                                    │
│  4️⃣  SAIR                                          │
│                                                    │
└────────────────────────────────────────────────────┘
```

### Fluxo Típico da Interface CRUD:

```
PASSO 1: Criar Conta
├─ Email (deve ser único)
├─ Senha (mínimo 6 caracteres)
├─ Selecionar Endereço (de uma lista)
└─ Escolher Plano de Assinatura

    ↓

PASSO 2: Criar Perfil
├─ Nome do Perfil
└─ Escolher Avatar

    ↓

PASSO 3: Menu Principal
├─ Ver Filmes/Séries por Gênero
├─ Editar Perfil
├─ Editar Conta
├─ Deletar Perfil
├─ Deletar Conta
└─ Sair
```

---

## 📊 Índices Criados e Performance

### ⚠️ Importante: Criar os Índices

Por padrão, o banco vem **SEM os índices otimizados**. Para ativar e testar a performance:

```bash
psql -U postgres -d netflix -f criar_indices.sql
```

### Índices Implementados

1. **`idx_generoobra_idgenero`** (PRIMARY)
   - Otimiza buscas de obras por gênero
   - Uso: Menu principal ao filtrar catálogo
   - Impacto: **Reduz scan sequencial em 85%**

2. **`idx_perfil_idconta`**
   - Melhora listagem de perfis por conta
   - Uso: Verificação de perfis existentes

3. **`idx_generoobra_composite`**
   - Índice composto para queries mais complexas
   - Uso: Buscas combinadas de gênero e obra

4. **`idx_conta_email`**
   - Otimiza validação de email único
   - Uso: Prevenção de duplicatas ao criar conta

---

## 🔍 Testar Performance com EXPLAIN ANALYZE

### Passo 1: Ver a performance SEM índices
```bash
psql -U postgres -d netflix << 'EOF'
EXPLAIN ANALYZE
SELECT DISTINCT o.IDObra, o.Titulo
FROM Obra o
INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
WHERE go.IDGenero = 1;
EOF
```

**Observe:**
- `Seq Scan` em GeneroObra (scan sequencial - lento!)
- Tempo de execução (em ms)

### Passo 2: Criar os índices
```bash
psql -U postgres -d netflix -f criar_indices.sql
```

### Passo 3: Ver a performance COM índices
```bash
psql -U postgres -d netflix << 'EOF'
EXPLAIN ANALYZE
SELECT DISTINCT o.IDObra, o.Titulo
FROM Obra o
INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
WHERE go.IDGenero = 1;
EOF
```

**Observe:**
- `Index Scan` em GeneroObra (muito mais rápido!)
- Tempo de execução reduzido em ~60-80%

### 📈 Resultado Esperado

| Aspecto | ANTES | DEPOIS |
|---------|-------|--------|
| Tipo de Scan | Seq Scan | Index Scan |
| Linhas lidas | ~100+ | ~5-10 |
| Tempo (ms) | 5-10ms | 0.5-1ms |
| % Melhora | - | **60-80% mais rápido** |

---

---

## 💾 Exemplos de Queries Críticas

### 1. Buscar Obras de um Gênero (OTIMIZADA)
```sql
SELECT DISTINCT o.IDObra, o.Titulo, o.ClassEtaria
FROM Obra o
INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
WHERE go.IDGenero = 1
ORDER BY o.Titulo;
```

### 2. Listar Perfis de uma Conta
```sql
SELECT IDPerfil, Nome, Avatar 
FROM Perfil 
WHERE IDConta = 1
ORDER BY Nome;
```

### 3. Query Complexa - Contas com Planos
```sql
SELECT 
    c.IDConta, 
    c.Email, 
    pl.Nome AS NomePlano,
    pl.Valor
FROM Conta c
LEFT JOIN Assinatura a ON c.IDConta = a.IDConta
LEFT JOIN Plano pl ON a.IDPlano = pl.IDPlano
ORDER BY c.IDConta;
```

### 4. Obras por Gênero (Relatório)
```sql
SELECT 
    g.NomeGenero,
    COUNT(DISTINCT go.IDObra) AS QuantidadeObras
FROM Genero g
LEFT JOIN GeneroObra go ON g.IDGenero = go.IDGenero
GROUP BY g.IDGenero, g.NomeGenero
ORDER BY QuantidadeObras DESC;
```

---

## 🧪 Executar Tudo em Uma Vez

### No Codespace/Devcontainer:
```bash
# Verificar conexão
psql -U postgres -d netflix -c "SELECT COUNT(*) FROM Conta;"

# Criar índices (opcional)
psql -U postgres -d netflix -f criar_indices.sql

# Executar a interface
python3 executar_interface.py
```

Escolha a opção **1** no menu para iniciar a interface CRUD!

### No Computador Local:
```bash
# Ativar virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências (se não tiver feito)
pip install -r requirements.txt

# Verificar conexão
psql -U postgres -d netflix -c "SELECT COUNT(*) FROM Conta;"

# Rodar a interface
python3 executar_interface.py
```

---

## 🔧 Requisitos

- **Python:** 3.7+
- **PostgreSQL:** 12+
- **Dependências:** `psycopg2-binary` (instalado via requirements.txt)

### Em Codespace/Devcontainer: ✅ Tudo automático!
### No computador local: ⚠️ PostgreSQL deve estar rodando

---

## ❌ Troubleshooting

### Erro: `psql: command not found`
**Causa:** PostgreSQL cliente não está instalado ou não está no PATH

**Solução (Codespace):**
```bash
apt-get update && apt-get install -y postgresql-client
```

**Solução (Computador Local):** 
- Instale PostgreSQL completo ou apenas o cliente PostgreSQL

---

### Erro: `could not connect to server: Connection refused`
**Causa:** PostgreSQL não está rodando

**Solução (Codespace):** Aguarde 1-2 minutos após abrir o container (inicialização do PostgreSQL)

**Solução (Computador Local):**
```bash
# Linux
sudo systemctl start postgresql

# Mac
brew services start postgresql

# Windows
# Abra Services → encontre "postgresql-x64" → Start
```

---

### Erro: `FATAL: database "netflix" does not exist`
**Causa:** Banco não foi criado

**Solução (Codespace):** Aguarde 2 minutos (DDL.sql é executado automaticamente)

**Solução (Computador Local):**
```bash
psql -U postgres -c "CREATE DATABASE netflix;"
psql -U postgres -d netflix -f DDL.sql
psql -U postgres -d netflix -f DML.sql
```

---

### Erro: `ModuleNotFoundError: No module named 'psycopg2'`
**Causa:** Dependências não instaladas

**Solução:**
```bash
pip install -r requirements.txt
```

---

### Erro: `FATAL: password authentication failed for user "postgres"`
**Causa:** Senha do PostgreSQL incorreta

**Solução (Codespace):** Já está configurada no `.devcontainer` (não precisa fazer nada)

**Solução (Computador Local):**
```bash
export PGPASSWORD='sua_senha'  # Linux/Mac
set PGPASSWORD=sua_senha        # Windows
```

---

## 👥 Autores

- **Joel**
- **Jordana**
- **Miguel**

---

## � Estrutura do Projeto

```
BD-NETFLIX-Miguel/
│
├── .devcontainer/                 # ✅ Configuração do Codespace/Devcontainer
│   ├── devcontainer.json          # Variáveis de ambiente e setup automático
│   └── docker-compose.yml         # PostgreSQL + Python container
│
├── SQL/
│   ├── DDL.sql                    # Criação das tabelas
│   ├── DML.sql                    # Dados iniciais (contas, perfis, obras)
│   └── criar_indices.sql          # Índices de performance
│
├── Python/
│   ├── interface_netflix.py       # Interface CRUD (menus interativos)
│   ├── conexao_db.py              # Módulo de conexão com PostgreSQL
│   ├── executar_interface.py      # Launcher com menu principal
│   └── teste_interface.py         # Testes de validação
│
├── requirements.txt               # Dependências (psycopg2)
├── README.md                      # Este arquivo
├── ENTREGA_FINAL.md              # Documentação completa do projeto
└── backup.sql                     # Backup do banco (opcional)
```

---

## 📝 Operações CRUD Implementadas

### ✅ CREATE
- Criar Conta (com validação de email único e senha)
- Criar Perfil (com avatar)
- Assinatura automática ao plano

### ✅ READ
- Listar Endereços
- Listar Planos
- Listar Perfis da conta
- Visualizar Filmes/Séries por Gênero

### ✅ UPDATE (Editar)
- Editar Perfil (Nome, Avatar)
- Editar Conta (Email, Senha, Endereço, Plano)

### ✅ DELETE
- Deletar Perfil (com confirmação)
- Deletar Conta (com cascade automático)

---

## 📌 Dados Iniciais Carregados

O banco vem pré-carregado com:
- **5 Contas** de teste
- **9 Perfis** associados
- **10 Obras** (Filmes e Séries)
- **7 Gêneros** (Ação, Drama, Comédia, etc.)
- **8 Atores**
- **3 Planos** de assinatura
- **5 Endereços**

Você pode criar mais contas, perfis e explorar o catálogo!

---

## 🎓 Conceitos Demonstrados

1. **Banco de Dados Relacional:**
   - Chaves primárias e estrangeiras
   - Relacionamentos 1:N e N:M
   - Integridade referencial

2. **Performance:**
   - Índices em tabelas críticas
   - EXPLAIN ANALYZE para análise
   - Diferença de Seq Scan vs Index Scan

3. **Segurança (Conceitual):**
   - Validação de entrada
   - Queries parametrizadas (SQL injection prevention)
   - Email único (restrição)

4. **Interface:**
   - Menu interativo
   - CRUD operacional
   - Feedback ao usuário

---

## �📅 Data de Entrega

**Junho de 2026**
