#!/usr/bin/env python3
"""
Script de teste da interface Netflix
Demonstra: CREATE, READ e DELETE
"""

from conexao_db import ConexaoDB

def teste_conexao():
    """Testa a conexão com o banco"""
    print("=" * 60)
    print("🔍 TESTE 1: Conectar ao Banco de Dados")
    print("=" * 60)
    
    db = ConexaoDB()
    if db.conectar():
        print("✅ Conexão estabelecida!")
        
        # Listar tabelas
        tabelas = db.buscar_todos("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name
        """)
        
        print(f"\n📊 Total de tabelas: {len(tabelas)}")
        print("Tabelas disponíveis:")
        for tabela in tabelas:
            print(f"  • {tabela[0]}")
        
        db.desconectar()
        return True
    return False

def teste_indices():
    """Verifica se os índices foram criados"""
    print("\n" + "=" * 60)
    print("🔍 TESTE 2: Verificar Índices Criados")
    print("=" * 60)
    
    db = ConexaoDB()
    if db.conectar():
        indices = db.buscar_todos("""
            SELECT indexname, tablename
            FROM pg_indexes
            WHERE schemaname = 'public' AND indexname LIKE 'idx_%'
            ORDER BY tablename, indexname
        """)
        
        print(f"\n✅ Total de índices: {len(indices)}\n")
        for nome_idx, tabela in indices:
            print(f"  • {nome_idx:40} → {tabela}")
        
        db.desconectar()
        return True
    return False

def teste_leitura_dados():
    """Testa leitura de dados"""
    print("\n" + "=" * 60)
    print("🔍 TESTE 3: Leitura de Dados")
    print("=" * 60)
    
    db = ConexaoDB()
    if db.conectar():
        # Contar contas
        contas = db.buscar_um("SELECT COUNT(*) FROM Conta")
        print(f"\n📧 Total de contas: {contas[0]}")
        
        # Listar planos
        planos = db.buscar_todos("SELECT IDPlano, Nome, Valor FROM Plano ORDER BY Valor")
        print(f"\n💳 Planos disponíveis ({len(planos)}):")
        for id_plano, nome, valor in planos:
            print(f"  • {nome}: R$ {valor:.2f}")
        
        # Contar gêneros
        generos = db.buscar_todos("SELECT IDGenero, NomeGenero FROM Genero ORDER BY NomeGenero")
        print(f"\n📂 Gêneros disponíveis ({len(generos)}):")
        for id_gen, nome_gen in generos:
            print(f"  • {nome_gen}")
        
        # Listar obras por gênero (usando o índice!)
        print("\n🎬 Obras de FANTASIA (usando índice idx_generoobra_idgenero):")
        obras_fantasia = db.buscar_todos("""
            SELECT DISTINCT o.Titulo, o.TipoObra
            FROM Obra o
            INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
            WHERE go.IDGenero = 1
            ORDER BY o.Titulo
        """)
        for titulo, tipo in obras_fantasia:
            print(f"  • {titulo} ({tipo})")
        
        db.desconectar()
        return True
    return False

def teste_operacoes_crud():
    """Testa CREATE, READ, DELETE"""
    print("\n" + "=" * 60)
    print("🔍 TESTE 4: Operações CRUD (Simulação)")
    print("=" * 60)
    
    db = ConexaoDB()
    if db.conectar():
        # CREATE - Criar uma conta de teste
        print("\n📝 Criando conta de teste...")
        email_teste = "teste@exemplo.com"
        
        # Verificar se já existe
        existe = db.buscar_um("SELECT IDConta FROM Conta WHERE Email = %s", (email_teste,))
        if existe:
            print(f"ℹ️  Conta {email_teste} já existe (ID: {existe[0]})")
            id_conta = existe[0]
        else:
            db.executar(
                "INSERT INTO Conta (Email, Senha, IDEndereco) VALUES (%s, %s, %s)",
                (email_teste, "senha123", 1)
            )
            id_conta = db.obter_ultimo_id()
            print(f"✅ Conta criada! ID: {id_conta}")
        
        # READ - Ler dados da conta
        print(f"\n📖 Lendo conta ID {id_conta}...")
        conta = db.buscar_um(
            "SELECT Email, IDEndereco FROM Conta WHERE IDConta = %s",
            (id_conta,)
        )
        if conta:
            email, id_endereco = conta
            print(f"  Email: {email}")
            print(f"  Endereço ID: {id_endereco}")
        
        # CREATE - Criar perfil
        print(f"\n📝 Criando perfil para conta {id_conta}...")
        nome_perfil = "Perfil Teste"
        db.executar(
            "INSERT INTO Perfil (Nome, Avatar, IDConta) VALUES (%s, %s, %s)",
            (nome_perfil, "Red_3", id_conta)
        )
        id_perfil = db.obter_ultimo_id()
        print(f"✅ Perfil criado! ID: {id_perfil}")
        
        # READ - Listar perfis
        print(f"\n📖 Listando perfis da conta {id_conta}...")
        perfis = db.buscar_todos(
            "SELECT IDPerfil, Nome, Avatar FROM Perfil WHERE IDConta = %s",
            (id_conta,)
        )
        for id_p, nome_p, avatar_p in perfis:
            print(f"  • {nome_p} (Avatar: {avatar_p}) - ID: {id_p}")
        
        # DELETE - Deletar perfil
        print(f"\n🗑️  Deletando perfil {id_perfil}...")
        db.executar("DELETE FROM Perfil WHERE IDPerfil = %s", (id_perfil,))
        print(f"✅ Perfil deletado!")
        
        # Verificar
        perfis_restantes = db.buscar_todos(
            "SELECT IDPerfil FROM Perfil WHERE IDConta = %s",
            (id_conta,)
        )
        print(f"Perfis restantes na conta: {len(perfis_restantes)}")
        
        db.desconectar()
        return True
    return False

def teste_performance():
    """Testa performance da query com índice"""
    print("\n" + "=" * 60)
    print("🔍 TESTE 5: Performance com Índice")
    print("=" * 60)
    
    db = ConexaoDB()
    if db.conectar():
        print("\n⚡ Executando query otimizada (com índice):\n")
        print("SELECT DISTINCT o.IDObra, o.Titulo")
        print("FROM Obra o")
        print("INNER JOIN GeneroObra go ON o.IDObra = go.IDObra")
        print("WHERE go.IDGenero = 1")
        print("ORDER BY o.Titulo;\n")
        
        resultado = db.buscar_todos("""
            EXPLAIN ANALYZE
            SELECT DISTINCT o.IDObra, o.Titulo
            FROM Obra o
            INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
            WHERE go.IDGenero = 1
            ORDER BY o.Titulo
        """)
        
        print("Plano de Execução:")
        for linha in resultado:
            print(f"  {linha[0]}")
        
        db.desconectar()
        return True
    return False

def main():
    """Executa todos os testes"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + "🎬 TESTE DA INTERFACE NETFLIX".center(58) + "║")
    print("╚" + "=" * 58 + "╝")
    
    testes = [
        ("Conexão ao Banco", teste_conexao),
        ("Verificar Índices", teste_indices),
        ("Leitura de Dados", teste_leitura_dados),
        ("Operações CRUD", teste_operacoes_crud),
        ("Performance", teste_performance),
    ]
    
    resultados = []
    for nome, funcao_teste in testes:
        try:
            resultado = funcao_teste()
            resultados.append((nome, "✅ OK" if resultado else "❌ FALHOU"))
        except Exception as e:
            print(f"\n❌ Erro em {nome}: {e}")
            resultados.append((nome, f"❌ ERRO: {str(e)[:40]}"))
    
    # Resumo
    print("\n" + "=" * 60)
    print("📋 RESUMO DOS TESTES")
    print("=" * 60)
    for nome, resultado in resultados:
        print(f"{nome:.<45} {resultado}")
    
    print("\n✅ Todos os testes concluídos!\n")

if __name__ == "__main__":
    main()
