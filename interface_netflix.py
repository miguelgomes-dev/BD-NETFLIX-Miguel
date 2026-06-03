from conexao_db import ConexaoDB
import re
import os

class InterfaceNetflix:
    """Interface interativa para o sistema Netflix"""
    
    def __init__(self):
        self.db = ConexaoDB()
        self.conta_atual = None
        self.perfil_atual = None
    
    def limpar_tela(self):
        """Limpa a tela do console"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def validar_email(self, email):
        """Valida formato de email"""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None
    
    def validar_senha(self, senha):
        """Valida senha (mínimo 6 caracteres)"""
        return len(senha) >= 6
    
    def menu_principal(self):
        """Menu inicial do sistema"""
        self.limpar_tela()
        print("=" * 60)
        print("🎬 BEM-VINDO AO NETFLIX - SISTEMA DE GERENCIAMENTO".center(60))
        print("=" * 60)
        print("\nEscolha uma opção:")
        print("1. Criar Conta")
        print("2. Sair")
        print("-" * 60)
        
        opcao = input("Digite sua escolha (1-2): ").strip()
        
        if opcao == "1":
            self.criar_conta()
        elif opcao == "2":
            print("\n👋 Até logo!")
            return False
        else:
            print("❌ Opção inválida!")
            input("Pressione ENTER para continuar...")
            return True
        
        return True
    
    def criar_conta(self):
        """Criar nova conta Netflix"""
        self.limpar_tela()
        print("=" * 60)
        print("➕ CRIAR NOVA CONTA NETFLIX".center(60))
        print("=" * 60)
        
        # Coletar email
        while True:
            email = input("\n📧 Email: ").strip()
            if not self.validar_email(email):
                print("❌ Email inválido! Tente novamente.")
                continue
            
            # Verificar se email já existe
            resultado = self.db.buscar_um("SELECT IDConta FROM Conta WHERE Email = %s", (email,))
            if resultado:
                print("❌ Este email já está registrado!")
                continue
            break
        
        # Coletar senha
        while True:
            senha = input("🔑 Senha (mínimo 6 caracteres): ").strip()
            if not self.validar_senha(senha):
                print("❌ Senha deve ter no mínimo 6 caracteres!")
                continue
            break
        
        # Coletar endereço
        self.listar_enderecos()
        while True:
            try:
                id_endereco = int(input("\n🏠 Digite o ID do endereço desejado: ").strip())
                resultado = self.db.buscar_um("SELECT IDEndereco FROM Endereco WHERE IDEndereco = %s", (id_endereco,))
                if not resultado:
                    print("❌ Endereço não encontrado!")
                    continue
                break
            except ValueError:
                print("❌ ID inválido!")
        
        # Coletar plano
        self.listar_planos()
        while True:
            try:
                id_plano = int(input("\n💳 Digite o ID do plano desejado: ").strip())
                resultado = self.db.buscar_um("SELECT IDPlano FROM Plano WHERE IDPlano = %s", (id_plano,))
                if not resultado:
                    print("❌ Plano não encontrado!")
                    continue
                break
            except ValueError:
                print("❌ ID inválido!")
        
        # Inserir conta
        try:
            self.db.executar(
                "INSERT INTO Conta (Email, Senha, IDEndereco) VALUES (%s, %s, %s)",
                (email, senha, id_endereco)
            )
            self.conta_atual = self.db.obter_ultimo_id()
            
            # Inserir assinatura
            self.db.executar(
                "INSERT INTO Assinatura (IDConta, IDPlano) VALUES (%s, %s)",
                (self.conta_atual, id_plano)
            )
            
            print(f"\n✅ Conta criada com sucesso! ID: {self.conta_atual}")
            input("Pressione ENTER para continuar...")
            
            self.criar_perfil()
        
        except Exception as e:
            print(f"❌ Erro ao criar conta: {e}")
            input("Pressione ENTER para continuar...")
    
    def listar_enderecos(self):
        """Exibe todos os endereços disponíveis"""
        print("\n🏠 ENDEREÇOS DISPONÍVEIS:")
        print("-" * 60)
        enderecos = self.db.buscar_todos("SELECT IDEndereco, Pais, Estado, Cidade FROM Endereco ORDER BY IDEndereco")
        
        if not enderecos:
            print("❌ Nenhum endereço disponível!")
            return
        
        for id_end, pais, estado, cidade in enderecos:
            print(f"ID: {id_end} | {cidade}, {estado} - {pais}")
    
    def listar_planos(self):
        """Exibe todos os planos disponíveis"""
        print("\n💳 PLANOS DISPONÍVEIS:")
        print("-" * 60)
        planos = self.db.buscar_todos("SELECT IDPlano, Nome, Valor, Beneficios FROM Plano ORDER BY IDPlano")
        
        if not planos:
            print("❌ Nenhum plano disponível!")
            return
        
        for id_plano, nome, valor, beneficios in planos:
            print(f"\nID: {id_plano} | {nome}")
            print(f"   R$ {valor:.2f}/mês")
            print(f"   {beneficios}")
    
    def criar_perfil(self):
        """Criar novo perfil na conta"""
        while True:
            self.limpar_tela()
            print("=" * 60)
            print("➕ CRIAR NOVO PERFIL".center(60))
            print("=" * 60)
            
            nome = input("\n👤 Nome do perfil: ").strip()
            if not nome:
                print("❌ Nome não pode estar vazio!")
                input("Pressione ENTER para continuar...")
                continue
            
            self.listar_avatares()
            avatar = input("\n🎨 Digite o código do avatar desejado: ").strip()
            
            try:
                self.db.executar(
                    "INSERT INTO Perfil (Nome, Avatar, IDConta) VALUES (%s, %s, %s)",
                    (nome, avatar, self.conta_atual)
                )
                self.perfil_atual = self.db.obter_ultimo_id()
                print(f"\n✅ Perfil '{nome}' criado com sucesso!")
                input("Pressione ENTER para continuar...")
                
                self.menu_pos_conta()
                break
            
            except Exception as e:
                print(f"❌ Erro ao criar perfil: {e}")
                input("Pressione ENTER para continuar...")
    
    def listar_avatares(self):
        """Exibe avatares disponíveis"""
        print("\n🎨 AVATARES DISPONÍVEIS:")
        print("-" * 60)
        avatares = [
            "Red_3", "Cavaleiro_2", "Dragao_5", "Princesa_1", 
            "Green_4", "Divertidamente_3", "Marvel_2"
        ]
        for avatar in avatares:
            print(f"  • {avatar}")
    
    def menu_pos_conta(self):
        """Menu após criar conta e perfil"""
        while True:
            self.limpar_tela()
            print("=" * 60)
            print(f"🎬 MENU PRINCIPAL - Perfil: {self.perfil_atual}".center(60))
            print("=" * 60)
            print("\n1. Ver Filmes e Séries")
            print("2. Deletar Perfil")
            print("3. Deletar Conta")
            print("4. Sair")
            print("-" * 60)
            
            opcao = input("Digite sua escolha (1-4): ").strip()
            
            if opcao == "1":
                self.visualizar_obras()
            elif opcao == "2":
                if self.deletar_perfil():
                    break
            elif opcao == "3":
                if self.deletar_conta():
                    return False
            elif opcao == "4":
                print("\n👋 Até logo!")
                return False
            else:
                print("❌ Opção inválida!")
                input("Pressione ENTER para continuar...")
    
    def visualizar_obras(self):
        """Visualizar filmes e séries disponíveis"""
        self.limpar_tela()
        print("=" * 60)
        print("🎬 CATÁLOGO DE FILMES E SÉRIES".center(60))
        print("=" * 60)
        
        # Listar gêneros
        print("\n📂 GÊNEROS DISPONÍVEIS:")
        print("-" * 60)
        generos = self.db.buscar_todos("SELECT IDGenero, NomeGenero FROM Genero ORDER BY IDGenero")
        
        for id_genero, nome_genero in generos:
            print(f"{id_genero}. {nome_genero}")
        
        try:
            id_genero = int(input("\nDigite o ID do gênero desejado: ").strip())
            
            # Buscar obras do gênero (com ÍNDICE otimizado)
            query = """
                SELECT DISTINCT o.IDObra, o.Titulo, o.ClassEtaria, o.TipoObra
                FROM Obra o
                INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
                WHERE go.IDGenero = %s
                ORDER BY o.Titulo
            """
            obras = self.db.buscar_todos(query, (id_genero,))
            
            if not obras:
                print("❌ Nenhuma obra encontrada neste gênero!")
                input("Pressione ENTER para continuar...")
                return
            
            print("\n🎬 OBRAS ENCONTRADAS:")
            print("-" * 60)
            for id_obra, titulo, classe_etaria, tipo_obra in obras:
                print(f"\n📽️  {titulo}")
                print(f"   Tipo: {tipo_obra} | Classificação: {classe_etaria}+")
                self.mostrar_detalhes_obra(id_obra, tipo_obra)
            
            input("\nPressione ENTER para voltar...")
        
        except ValueError:
            print("❌ ID inválido!")
            input("Pressione ENTER para continuar...")
    
    def mostrar_detalhes_obra(self, id_obra, tipo_obra):
        """Mostra detalhes de uma obra"""
        if tipo_obra == "Filme":
            filme = self.db.buscar_um(
                "SELECT DuracaoMinutos, AnoLancamento FROM Filme WHERE IDObra = %s",
                (id_obra,)
            )
            if filme:
                duracao, ano = filme
                print(f"   ⏱️  Duração: {duracao} minutos | Lançamento: {ano}")
        
        elif tipo_obra == "Série":
            serie = self.db.buscar_um(
                "SELECT QtdTemporadas FROM Serie WHERE IDObra = %s",
                (id_obra,)
            )
            if serie:
                qtd_temp = serie[0]
                print(f"   📺 Temporadas: {qtd_temp}")
    
    def deletar_perfil(self):
        """Deletar perfil atual"""
        self.limpar_tela()
        print("=" * 60)
        print("❌ DELETAR PERFIL".center(60))
        print("=" * 60)
        
        print(f"\n⚠️  Tem certeza que deseja deletar o perfil ID {self.perfil_atual}?")
        confirmacao = input("Digite 'SIM' para confirmar: ").strip().upper()
        
        if confirmacao == "SIM":
            try:
                self.db.executar(
                    "DELETE FROM Perfil WHERE IDPerfil = %s",
                    (self.perfil_atual,)
                )
                print("✅ Perfil deletado com sucesso!")
                
                # Listar perfis restantes
                perfis = self.db.buscar_todos(
                    "SELECT IDPerfil, Nome FROM Perfil WHERE IDConta = %s",
                    (self.conta_atual,)
                )
                
                if perfis:
                    print("\n📋 PERFIS RESTANTES:")
                    for id_perfil, nome in perfis:
                        print(f"  • ID: {id_perfil} | Nome: {nome}")
                    
                    try:
                        novo_id = int(input("\nEscolha outro perfil (ID): ").strip())
                        resultado = self.db.buscar_um(
                            "SELECT IDPerfil FROM Perfil WHERE IDPerfil = %s AND IDConta = %s",
                            (novo_id, self.conta_atual)
                        )
                        if resultado:
                            self.perfil_atual = novo_id
                            return False
                        else:
                            print("❌ Perfil inválido!")
                    except ValueError:
                        print("❌ ID inválido!")
                    
                    return False
                else:
                    print("❌ Nenhum perfil restante! Voltando ao menu principal...")
                    return True
            
            except Exception as e:
                print(f"❌ Erro ao deletar perfil: {e}")
                input("Pressione ENTER para continuar...")
                return False
        else:
            print("❌ Operação cancelada!")
            input("Pressione ENTER para continuar...")
            return False
    
    def deletar_conta(self):
        """Deletar conta e todas as suas relações"""
        self.limpar_tela()
        print("=" * 60)
        print("❌ DELETAR CONTA".center(60))
        print("=" * 60)
        
        print(f"\n⚠️  ⚠️  ⚠️  ATENÇÃO! Isto deletará a conta e TODOS os perfis!")
        print(f"ID da Conta: {self.conta_atual}")
        confirmacao = input("\nDigite 'DELETAR TUDO' para confirmar: ").strip().upper()
        
        if confirmacao == "DELETAR TUDO":
            try:
                # Deletar todos os perfis primeiro
                self.db.executar(
                    "DELETE FROM Perfil WHERE IDConta = %s",
                    (self.conta_atual,)
                )
                
                # Deletar assinatura
                self.db.executar(
                    "DELETE FROM Assinatura WHERE IDConta = %s",
                    (self.conta_atual,)
                )
                
                # Deletar conta
                self.db.executar(
                    "DELETE FROM Conta WHERE IDConta = %s",
                    (self.conta_atual,)
                )
                
                print("✅ Conta deletada com sucesso!")
                print("\n👋 Voltando ao menu principal...")
                input("Pressione ENTER para continuar...")
                
                return True
            
            except Exception as e:
                print(f"❌ Erro ao deletar conta: {e}")
                input("Pressione ENTER para continuar...")
                return False
        else:
            print("❌ Operação cancelada!")
            input("Pressione ENTER para continuar...")
            return False
    
    def executar(self):
        """Inicia a aplicação"""
        if not self.db.conectar():
            print("❌ Não foi possível conectar ao banco de dados!")
            return
        
        try:
            continuar = True
            while continuar:
                continuar = self.menu_principal()
        finally:
            self.db.desconectar()


def main():
    """Função principal"""
    interface = InterfaceNetflix()
    interface.executar()


if __name__ == "__main__":
    main()
