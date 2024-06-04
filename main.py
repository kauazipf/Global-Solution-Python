# Código principal

from usuario import Usuario
from autenticacao import fazer_login
from validacao import validar_documento, validar_senha
from cadastro import cadastrar_usuario
from menu import menu_principal, menu_logado
from cadastroArtigos import cadastrar_artigos, exibir_artigos

# Código de execução do projeto
def main():
    usuario = None

    while True:
        opcao = menu_principal()
        if opcao == '1':
            usuario = cadastrar_usuario()
            print("Usuário cadastrado com sucesso!")
        elif opcao == '2':
            if usuario and usuario.esta_logado:
                print("Usuário já está logado.")
            else:
                if not usuario:
                    print("Nenhum usuário cadastrado. Por favor, cadastre um usuário primeiro.")
                else:
                    login = input("Digite o email, nome de usuário ou documentos: ")
                    password = input("Digite a senha: ")
                    fazer_login(usuario, login, password)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

        while usuario and usuario.esta_logado:
            opcao_logado = menu_logado()

            if opcao_logado == '1':
                print("Opção principais causas da poluição oceanica \n")
                print("Mudanças Climáticas")
                print("\t As mudanças climáticas afetam o planeta como um todo e, claro, os oceanos não estão imunes. Os impactos nas águas oceânicas estão ligados principalmente ao aquecimento global e à emissão em excesso de gases de efeito estufa (GEE). “Os oceanos fazem uma troca de calor e gases com a atmosfera. Então, uma atmosfera mais quente significa um oceano mais quente, e isso impacta negativamente uma série de organismos e ecossistemas marinhos”, explica Angelo Fraga Bernardino, oceanógrafo, ecologista marinho e Explorador da National Geographic. \n")
                print(f"\t Segundo o boletim O oceano, nosso clima e tempo de 2021, da Organização Meteorológica Mundial (OMM), feito como uma contribuição oficial à Década do Oceano, da ONU, os oceanos absorvem mais de 90% do excesso de calor no sistema climático da Terra e mais de um quarto do CO2 emitido anualmente pela produção humana. \n")
                print("\t “Até 2100, o oceano terá absorvido duas a quatro vezes mais calor do que nos últimos 50 anos se o aumento da temperatura média global for limitado à 2ºC. Se for maior, ele pode absorver de quatro até sete vezes mais”, alerta o boletim. \n")
                print("\tEssa relação de troca de calor entre o oceano e a atmosfera é benéfica para o equilíbrio da temperatura e, segundo Bernardino, é um dos motivos do aquecimento global não estar ainda pior. Porém, quanto mais quente as águas marinhas ficam, essa troca para de mitigar o calor da atmosfera e passa a aumentá-lo. “É uma troca de energia entre a atmosfera, as águas marinhas superficiais e as águas mais profundas, que recebem calor pelas correntes, explica Bernardino. Se tem muita energia, chega uma hora que não é mais possível distribuir igualmente, e o oceano acaba liberando ainda mais calor. \n\n\n")
                
                print("Pesca Insustentável")
                print("\t Além das alterações químicas no oceano, os humanos ainda ameaçam os animais marinhos de outras maneiras. Uma delas é a pesca insustentável que diminui as populações de peixes e ameaça a sobrevivência de espécies. Um relatório de Pesca e Aquicultura da Organização para Agricultura e Alimentação da ONU (FAO) elenca como pesca insustentável:  \n")
                print("\t • Sobrepesca, que é a superexploração de peixes além dos limites biológicos sustentáveis; \n")
                print("\t • Pesca destrutiva, que é o uso de práticas ou equipamentos que prejudicam um ecossistema; \n")
                print("\t • Pesca irregular, que pode se referir à pesca ilegal, não declarada ou não regulamentada. \n")
                print(f"\t Também de acordo o documento, essas práticas são a causa direta da mortalidade excessiva de alguns peixes, como o atum, e também de espécies não alvo, como toninhas e algumas tartarugas marinhas. Segundo estimativas da própria FAO, cerca de 34% de todos os estoques de peixes marinhos são superexplorados. Isso representaria o triplo desde o início do monitoramento em 1974. \n")
                print("\t Outro problema da pesca inadequada são os estoques de comida e fonte de renda de comunidades. Três bilhões de pessoas sobrevivem por conta dos oceanos e, muitas delas, contam com o pescado como fonte primária de proteína, diz Adriana Lippi, oceanógrafa e conselheira da Liga das Mulheres pelo Oceano. Então, manter os estoques pesqueiros saudáveis é muito importante para boa parte da população global. \n\n\n")
                
                print("Poluição Marinha")
                print(f"\t Um relatório publicado em 2021 pelo Programa das Nações Unidas para o Meio Ambiente (Pnuma) mostra que o plástico é a maior, mais prejudicial e mais persistente parte dos resíduos humanos que acabam no mar, representando 85% do total.  \n")
                print("\t O material poluidor também foi detectado em todos os oceanos do planeta. O estudo Panorama dos oceanos, mares e recursos marinhos na América Latina e no Caribe, de fevereiro de 2022, produzido pela Comissão Econômica para a América Latina e o Caribe, relata que microplásticos (sobras do processo de decomposição dos plásticos) chegaram a oceanos profundos, fossas submarinas, no gelo do mar profundo e do mar Ártico e até a lugares. \n")
                print("\t “Sabemos que quase não existem mais ecossistemas livres de plástico. Os cientistas encontraram microplásticos no topo das montanhas mais altas, no sangue humano e em lugares super remotos, como as profundezas do Mar Antártico”, diz Cristian Lagger, ecologista marinho, pesquisador do Laboratório de Ecologia Marinha do Instituto de Diversidade e Ecologitão remotos como a região da Patagônia, entre a Argentina e o Chile.  \n")
                print("\tEntre os impactos da poluição por plásticos nos ambientes marinhos estão efeitos letais e subletais em diversos animais, desde baleias, focas, tartarugas, aves e peixes, até invertebrados e corais. O relatório do Pnuma registra que os plásticos atingem os animais ao se emaranhar a eles, podendo causar lesões, afogamento, asfixia, privação de oxigênio, estresse fisiológico, dano toxicológico, entre outros estragos.\n")
                
            elif opcao_logado == '2':
                print("Opção cadastrar artigos selecionada. \n")
                cadastrar_artigos()
                
            elif opcao_logado == '3':
                print("Opção exibir artigos cadastrados selecionada. \n")
                exibir_artigos()
                print("")
            elif opcao_logado == '4':
                print("Opção Participantes selecionada. \n")
                print("\n\tKauã Fermino Zipf \t RM-558957")
                print("\n\tCaetano Matos Penefiel \t RM-557984")
                print("\n\tVictor Egidio Lira \t RM-556653")
            elif opcao_logado == '5':
                usuario.fazer_logout()
                usuario = None
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    main()