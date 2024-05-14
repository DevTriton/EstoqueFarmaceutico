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
        cursor.close()
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
            conexao.close()  
            print("----------------------------------------")


        

    def menu_rem(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar Remédio")
        print("2) Imprimir lista Remédios")
        print("3) excluir um Remédio")
        print("4) atualizar um Remédio")
        print("5) Sair")
        self.opcao=int(input("digite a opção que deseja fazer: "))

    def executar_rem(self):    
        while self.opcao != 5:
                self.menu_rem() 
                
                if self.opcao==1:
                    self.cadastrar_medicamento()
                elif self.opcao==2:
                    self.imprimir()
                elif self.opcao==3:
                    self.Remover()
                elif self.opcao==4:
                    self.atualizar()          
                elif self.opcao==5:
                    break   
                             

objeto1 = estoque()
objeto1.executar_rem()