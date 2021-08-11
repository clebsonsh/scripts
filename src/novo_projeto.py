import os
import sys
from src.models.projeto import Projeto
from src.models.configuracao_projeto import ConfiguracaoProjeto

def gerarArquiteturaDDD(nome): 
    
     os.mkdir('Domain')
     os.mkdir('Infra')
     os.mkdir('Test')

     projetos = []
     projetos.append(ConfiguracaoProjeto("Domain",nome,"Domain","classlib"))     
     projetos.append(ConfiguracaoProjeto("Domain.Service",nome,"Domain.Service","classlib")) 
     projetos.append(ConfiguracaoProjeto("Infra.Data",nome,"Infra.Data","classlib"))
     projetos.append(ConfiguracaoProjeto("Infra.CorssCutting",nome,"Infra.CorssCutting","classlib"))
     projetos.append(ConfiguracaoProjeto("Test",nome,"Test","msTest"))
     projetos.append(ConfiguracaoProjeto("UI.MVC",nome,"UI.MVC","msTest"))
     projetos.append(ConfiguracaoProjeto("Api",nome,"Api","webapi"))
     
     for projeto in projetos:
        projeto.gerar();

def configurarProjeto(nome, diretorio, usuario, tipo, arquitetura):

    projeto = Projeto(nome,diretorio,tipo,arquitetura,usuario)
    projeto.gerarSolucao()    
    
    if projeto.arquitetura == 1:
       gerarArquiteturaDDD(nome)


def gerarNovoProjeto():
    os.system('cls' if os.name == 'nt' else 'clear')

    nome = input("Escolha o Nome para Solução: ")    
    diretorio = input("Escolha o diretório: ")     
    usuario = input("Informe Usuário do GitHub para Preparar o git (opcional): ")    
    tipo = input("Escolha O Tipo de Projeto \n"
        "( 1 ) MVC \n"
        "( 2 ) API \n"
        "( 3 ) MVC + API \n"
        "( 4 ) ANGULAR + API \n"
        "( 5 ) VUEJS + API \n"
        "Escolha: "
        )

    arquitetura = input("Arquitetura\n"
    "( 1 ) Driven Domain Design")  

    confirma = input("GERADOR DE PROJETOS"
                "\n Solution" , nome,
                "\n Path" , diretorio,
                "\n Git" , usuario,
                 "\n Tipo" , tipo,
                "\n ",
                "\n Confirma os dados?: \n"
                "( 0 ) Não \n"
                "( 1 ) Sim \n"    
                "Confirmação: "
                )  

    if confirma == "1" :     
       configurarProjeto(nome, diretorio, usuario, tipo, arquitetura)
    