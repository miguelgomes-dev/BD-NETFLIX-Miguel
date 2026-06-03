#!/usr/bin/env python3
"""
Instrução de Inicialização da Interface Netflix
Execute este script para começar a usar a interface
"""

import subprocess
import sys
import os

def print_banner():
    """Exibe banner inicial"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + "🎬 INTERFACE NETFLIX - SISTEMA DE GERENCIAMENTO DE CONTAS".center(78) + "║")
    print("║" + "Grupo: Joel, Jordana e Miguel".center(78) + "║")
    print("╚" + "=" * 78 + "╝")
    print()

def check_dependencies():
    """Verifica se todas as dependências estão instaladas"""
    print("🔍 Verificando dependências...")
    
    try:
        import psycopg2
        print("  ✅ psycopg2 instalado")
        return True
    except ImportError:
        print("  ❌ psycopg2 não instalado!")
        print("\n📦 Instale as dependências:")
        print("   pip install -r requirements.txt")
        return False

def check_virtual_env():
    """Verifica se está em um virtual environment"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("  ✅ Virtual environment ativo")
        return True
    else:
        print("  ⚠️  Virtual environment NÃO ativo!")
        print("\n💡 Para ativar:")
        print("   source venv/bin/activate  # Linux/Mac")
        print("   venv\\Scripts\\activate     # Windows")
        return False

def main():
    """Função principal"""
    print_banner()
    
    # Verificar dependências
    print("=" * 80)
    print("📋 PRÉ-REQUISITOS")
    print("=" * 80)
    
    if not check_virtual_env():
        print("\n⚠️  Continuando mesmo sem virtual environment...")
    
    if not check_dependencies():
        sys.exit(1)
    
    print("\n✅ Todos os pré-requisitos OK!")
    
    # Menu de opções
    print("\n" + "=" * 80)
    print("📌 MENU DE OPÇÕES")
    print("=" * 80)
    print("\n1. Iniciar Interface CRUD (Menu Interativo)")
    print("2. Executar Testes de Conexão e Performance")
    print("3. Ver Índices Criados no Banco")
    print("4. Sair")
    print()
    
    opcao = input("Escolha uma opção (1-4): ").strip()
    
    if opcao == "1":
        print("\n🚀 Iniciando Interface Netflix...\n")
        try:
            import interface_netflix
            interface = interface_netflix.InterfaceNetflix()
            interface.executar()
        except Exception as e:
            print(f"\n❌ Erro ao iniciar interface: {e}")
            sys.exit(1)
    
    elif opcao == "2":
        print("\n🧪 Executando testes...\n")
        try:
            import teste_interface
            teste_interface.main()
        except Exception as e:
            print(f"\n❌ Erro ao executar testes: {e}")
            sys.exit(1)
    
    elif opcao == "3":
        print("\n📊 Índices no Banco de Dados:\n")
        try:
            from conexao_db import ConexaoDB
            db = ConexaoDB()
            if db.conectar():
                indices = db.buscar_todos("""
                    SELECT indexname, tablename, indexdef
                    FROM pg_indexes
                    WHERE schemaname = 'public' AND indexname LIKE 'idx_%'
                    ORDER BY tablename, indexname
                """)
                
                for idx_name, table_name, idx_def in indices:
                    print(f"📌 {idx_name}")
                    print(f"   Tabela: {table_name}")
                    print(f"   Definição: {idx_def}\n")
                
                db.desconectar()
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    elif opcao == "4":
        print("\n👋 Até logo!\n")
        sys.exit(0)
    
    else:
        print("❌ Opção inválida!")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interface encerrada pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
