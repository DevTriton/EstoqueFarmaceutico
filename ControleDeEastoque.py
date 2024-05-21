import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='estoque_farmaceutico',
)   

class estoque:
    def __init__(self, id_estoque = 0):
        self.id_estoque = id_estoque
        self.opcao = 0

    def cadastrar_medicamento(self):

        nome=input("digite o nome do medicamento: ").upper()
        fabricante=input("digite o fabricante: ").upper()
        dose=input("digite a dose Ex: 5mg: ").upper()
        tarja=int(input("digite a tarja 1-Sem tarja 2-Tarja vermelha 3-Tarja preta 4-Tarja amarela: "))
        qtd_comprimidos=int(input("digite a quantidade de comprimidos: "))
        data=input("digite a data Ex: 2023-11-14 ANO-MÊS-DIA: ")
        data = datetime.strptime(data, "%Y-%m-%d")
        databr=data.strftime("%Y-%m-%d")
        valor = float(input("digite o valor Ex: 4.50: "))
        descricao = input("digite a descricao do remedio: ")
        qtd_remedios = int(input("digite a quantidade de caixas a serem cadastradas: "))

        cursor = conexao.cursor()
        cursor.execute("INSERT INTO REMEDIOS (NOME, FABRICANTE, DOSE, TARJA, QTD_COMPRIMIDOS, DATA, VALOR, DESCRICAO, QTD_REMEDIOS) VALUES ('"+nome+"', '"+fabricante+"', '"+dose+"',  "+str(tarja)+", "+str(qtd_comprimidos)+", '"+databr+"', "+str(valor)+", '"+descricao+"', "+str(qtd_remedios)+" ); ")
        conexao.commit()
        conexao.close()
        print("feito")

    def imprimir(self):

        print("----------------------------------------")
        cursor = conexao.cursor()
        cursor.execute("select NOME, FABRICANTE, DOSE, TARJA, QTD_COMPRIMIDOS, DATA, VALOR, DESCRICAO, QTD_REMEDIOS from REMEDIOS;")
        retorno = cursor.fetchall()
        lista = []
        for linha in retorno:
            lista.append(linha[:])
            index = len(lista) - 1
            print(lista[index])
        conexao.commit()
        conexao.close()  
        print("----------------------------------------")

    def remover(self):       
        op=int(input("digite o ID do medicamento que deseja apagar: "))
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM REMEDIOS where ID_REMEDIO = '"+str(op)+"';")
        conexao.commit()
        conexao.close()

    def atualizar(self):
        op=int(input("digite o ID do medicamento que deseja alterar"))
        op1=int(input("Oque voce deseja alterar? 1-nome 2-fabricante 3-dose 4-tarja 5-quantidade de comprimidos 6-data 7-valor 8-descrição 9-quantidade de caixas 10-sair"))
        cursor = conexao.cursor()
        while op1!=10:
        
            match op1:
                case 1:
                    nome=input("digite o nome do medicamento: ").upper()
                    cursor.execute("UPDATE REMEDIOS SET NOME = "'+nome+'" WHERE ID_REMEDIO = "+str(op)+" ;")
                case 2:    
                    fabricante=input("digite o fabricante: ").upper()
                    cursor.execute("UPDATE REMEDIOS SET FABRICANTE = "'+fabricante+'" WHERE ID_REMEDIO = "+str(op)+" ;")
                case 3:    
                    dose=input("digite a dose Ex: 5mg: ").upper()
                    cursor.execute("UPDATE REMEDIOS SET DOSE = "'+dose+'" WHERE ID_REMEDIO = "+str(op)+" ;")
                case 4:
                    tarja=int(input("digite a tarja 1-Sem tarja 2-Tarja vermelha 3-Tarja preta 4-Tarja amarela: "))
                    cursor.execute("UPDATE REMEDIOS SET TARJA = "+str(tarja)+" WHERE ID_REMEDIO = "+str(op)+" ;")
                case 5: 
                    qtd_comprimidos=int(input("digite a quantidade de comprimidos: "))
                    cursor.execute("UPDATE REMEDIOS SET QTD_COMPRIMIDOS = "+str(qtd_comprimidos)+" WHERE ID_REMEDIO = "+str(op)+" ;")
                case 6: 
                    data=input("digite a data Ex: 2023-11-14 ANO-MÊS-DIA: ")           
                    data = datetime.strptime(data, "%Y-%m-%d")
                    databr=data.strftime("%Y-%m-%d")
                    cursor.execute("UPDATE REMEDIOS SET DATA = "+str(data)+" WHERE ID_REMEDIO = "+str(op)+" ;")
                case 7: 
                    valor = float(input("digite o valor Ex: 4.50: "))
                    cursor.execute("UPDATE REMEDIOS SET VALOR = "+str(valor)+" WHERE ID_REMEDIO = "+str(op)+" ;")
                case 8:
                    descricao = input("digite a descricao do remedio: ")
                    cursor.execute("UPDATE REMEDIOS SET DESCRICAO = "+str(descricao)+" WHERE ID_REMEDIO = "+str(op)+" ;")
                case 9:
                    qtd_remedios = int(input("digite a quantidade de caixas a serem cadastradas: "))
                    cursor.execute("UPDATE REMEDIOS SET QTD_REMEDIOS = "+str(qtd_remedios)+" WHERE ID_REMEDIO = "+str(op)+" ;")
                case 10:
                    break         

    def menu_rem(self):
        print("|############################################################|")
        print("|                           Menu                             |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar Remédio")
        print("2) Imprimir lista Remédios")
        print("3) excluir um Remédio")
        print("4) atualizar um Remédio")
        print("5) Sair")
        self.opcao=int(input("Digite a opção que deseja executar: "))
        while self.opcao<1 or self.opcao>5:
            self.opcao=int(input("Digite a opção que deseja executar: "))

    def executar_rem(self):    
        while self.opcao != 5:
                self.menu_rem() 
                
                if self.opcao==1:
                    self.cadastrar_medicamento()
                elif self.opcao==2:
                    self.imprimir()
                elif self.opcao==3:
                    self.remover()
                elif self.opcao==4:
                    self.atualizar()          
                elif self.opcao==5:
                    break   
                             

objeto1 = estoque()
objeto1.executar_rem()