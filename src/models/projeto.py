import os
import sys

class Projeto:
     def __init__(self, nome,diretorio,tipo,arquitetura,usuario):
        self.nome = nome
        self.diretorio = diretorio
        self.tipo = tipo
        self.arquitetura = arquitetura
        self.usuario = usuario
        os.chdir(diretorio)

     def gerarSolucao(self):
       comando = 'dotnet new sln -o '+ self.nome
       os.system(comando)   
       print("Solução "+self.nome+" Gerada!")
       os.chdir(self.nome)