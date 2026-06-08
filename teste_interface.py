#!/usr/bin/env python3
"""
Script de teste da interface Netflix
Demonstra: CREATE, READ e DELETE
"""

from conexao_db import ConexaoDB

def teste_performance():
    """Testa e compara visualmente a performance da query SEM e COM índice"""
    
    db = ConexaoDB()
    if not db.conectar():
        return False
        
    query_alvo = """
        SELECT o.IDObra, o.Titulo
        FROM Obra o
        INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
        WHERE go.IDGenero = 5
    """
    
    try:
        db.executar("DROP INDEX IF EXISTS idx_generoobra_idgenero;")

        linhas_sem = db.buscar_todos(f"EXPLAIN ANALYZE {query_alvo}")
        
        tempo_sem = 0.0
        busca_sem = "Seq Scan"
        for linha in linhas_sem:
            texto = linha[0]
            if "Execution Time:" in texto:
                tempo_sem = float(texto.split(":")[1].replace("ms", "").strip())
            if "Scan" in texto and "go" in texto:
                busca_sem = texto.strip().split(" on ")[0]

        db.executar("CREATE INDEX idx_generoobra_idgenero ON GeneroObra(IDGenero);")
        
        linhas_com = db.buscar_todos(f"EXPLAIN ANALYZE {query_alvo}")
        
        tempo_com = 0.0
        busca_com = "Index Scan"
        for linha in linhas_com:
            texto = linha[0]
            if "Execution Time:" in texto:
                tempo_com = float(texto.split(":")[1].replace("ms", "").strip())
            if "Scan" in texto and "go" in texto:
                busca_com = texto.strip().split(" on ")[0]

        print("-" * 60)
        
        max_tempo = max(tempo_sem, tempo_com, 0.001)
        tam_max_barra = 30
        
        barra_sem = "█" * int((tempo_sem / max_tempo) * tam_max_barra)
        barra_com = "█" * int((tempo_com / max_tempo) * tam_max_barra)
        if not barra_com and tempo_com > 0: barra_com = "▏"

        print(f"🔴 SEM ÍNDICE ({busca_sem}):")
        print(f"   [{barra_sem:<30}] {tempo_sem:.3f} ms")
        print()
        print(f"🟢 COM ÍNDICE ({busca_com}):")
        print(f"   [{barra_com:<30}] {tempo_com:.3f} ms")
        print("-" * 60)
        
        melhoria = (tempo_sem - tempo_com) / tempo_sem * 100
        vezes = tempo_sem / tempo_com
        print(f"O banco de dados foi {vezes:.1f}x mais rápido usando o índice.")

    except Exception as e:
        print(f"❌ Erro ao medir performance: {e}")
        db.executar("CREATE INDEX IF NOT EXISTS idx_generoobra_idgenero ON GeneroObra(IDGenero);")
        return False
    finally:
        db.desconectar()
        
    return True

def main():
    
    testes = [
        ("Performance", teste_performance),
    ]
    
    resultados = []
    for nome, funcao_teste in testes:
        resultado = funcao_teste()
        resultados.append((nome, "✅ OK" if resultado else "❌ FALHOU"))

if __name__ == "__main__":
    main()
