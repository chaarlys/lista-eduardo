tam = 5 lista = {}
class hash: chave = None; livre = "L";
class Controle: def init(self, tam=8): self.tam = tam self.tabela = [hash() for _ in range(self.tam)]
def funcao_hashing(self, num): return num % self.tam
def mostrar_hash(self): for i in range(self.tam): if self.tabela[i].livre == "O": print(self.tabela[i].chave)
def inserir(self, pos, n): i = 0 while i < self.tam: if self.tabela[(pos+i) % self.tam].livre != "L" and self.tabela[(pos+i)%self.tam].livre != "R": i = i + 1 else: break print(i)
  if i < self.tam:
    self.tabela[(pos +i) % self.tam].chave = n
    self.tabela[(pos +i) % self.tam].livre = "O"

  else:
    print("Tabela está cheia")
def buscar(self, n): i = 0 pos = self.funcao_hashing(n) while i < self.tam and self.tabela[(pos+i)%self.tam].livre != 'L' and self.tabela[(pos+i)%self.tam].chave != n: i = i+1 if self.tabela[(pos+i)%self.tam].chave == n and self.tabela[(pos+i)%self.tam].livre != "R": return (pos+i) % self.tam else: return self.tam
def remover(self, n): posicao = self.buscar(n) if posicao < self.tam: self.tabela[posicao].livre = "R" else: print("Elemento não está presente")
def opcao1(self): n = int(input("Digite um Numero")) self.describ() pos = self.funcao_hashing(n) lista[pos]= self.describ() self.inserir(pos, n)
def opcao3(self): n = int(input("Digite um número: ")) self.remover(n)
def opcao6(self): n = int(input("Procurar Produto:") ) return self.buscar(n)
def opcao7(self): if lista is not None: print("\nEstoque:") return print(lista)
else:
  print("Estoque vazio")
  return 0
def menu(self): txt = """ Opções: 1 - Inserir Produtos 2 - Consultar todos os produtos cadastrados de um tipo; 3 - Excluir Produtos 4 - sair 6 - Estoque Digite a sua opção """ opcao = int(input(txt)) return opcao
def describ(self): txt = """ 1- Número: 2- Descriçao: 3- Tipo: 4- Mostra Tipos:[Alimento,Produtos,Higiene,Limpeza,Vestuário] 5 - Verificar cadastro 6 - Sair
    """
    ops=0
    dados = {}
    listaDI = [None for i in range(self.tam)]

    while ops != 5:
     cls = os.system('clear' if os.name == 'posix' else 'cls')
     print(txt)
     ops = int(input())
     if ops is 1:
         descrever  = int(input("Numero:"))
         dados[1] =  descrever

     if ops is 2:
         descrever  = input("Descrição:")
         dados[2] =  descrever

     if ops is 3:
         descrever  = input("Tipo:")
         dados[3] =  descrever

     if ops is 4:
         descrever  = input("Descrição:")
         dados[4] =  descrever

     if ops is 5:
        listaDI = dados
        print("Lista",listaDI)
        tl = input("Precione uma tecla para sair:")

     if ops is 6:
         cls = os.system('clear' if os.name == 'posix' else 'cls')
         return 0

    return listaDI
def main(self): opcoes = {1:self.opcao1, 2:self.mostrar_hash, 3:self.opcao3,6:self.opcao6} while True: opcao = self.menu() if opcao in opcoes: opcoesopcao
 else:
   if opcao == 4:
     break

   else:
      print("Opção inválida")
controle = Controle() controle.main()