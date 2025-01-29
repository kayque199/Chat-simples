#Tela Inicial
    #Titulo: Chat casal
    #Botão: iniciar conversa 
        #Assim que clicar no botão:
        # Abrir uma janela(popup)/modal/alerta
            #Titulo: Seja bem vindo(a) ou bem vinde 
            #Caixa de texto: Escreva seu nome no chat
            #Botão: Entrar no chat 
                # Clicar no botão:
                    #Sumir com titulo 
                    #Sumir com o botão iniciar chat 
                    #Fechar o alerta
                        #carregar o chat
                        #carregar o campo de enviar mensagem: Digite seu nome
                            #Botão enviar 
                            #quando clicar no botão enviar 
                            #A mensagem sera enviada 
                            # E limpara a caixa de mensagem

#Usarei a biblioteca FLET, ela permitira que com o mesmo codigo seja crado site, programa e APP. 
# Além de criar tanto o back END quanto o front END

#importa o flet
import flet as ft


#Criar uma função principal para o aplicativo
def meu_chat(pagina_inicial):
    #titulo:
    titulo = ft.Text("chatCasal")

    #Primeiro criar a variavel que sera executada no tunel de comunicação
    def enviar_mensagem_tunel_de_comunicacao(mensagem):
        texto = ft.Text(mensagem)
        campo_conversa.controls.append(texto)
        pagina_inicial.update()

    #Segundo Criar o tunel
    pagina_inicial.pubsub.subscribe(enviar_mensagem_tunel_de_comunicacao)



    def enviar_msg(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina_inicial.pubsub.send_all(mensagem)
        enviar_mensagem.value = "" # Serve para limpar a caixa de enviar mensagem
      

        pagina_inicial.update()

    enviar_mensagem = ft.TextField(label="digite aqui sua mensagem" , on_submit= enviar_msg) #on_submit serve para que seja enviado com enter
    botao_enviar = ft.ElevatedButton("Enviar" , on_click= enviar_msg)

    linha_enviar = ft.Row ([enviar_mensagem, botao_enviar])
    campo_conversa = ft.Column()

    def entrar_chat(evento):
        alerta.open = False # O botão "entrar no chat" fechara o alert
        pagina_inicial.remove(titulo) #para remover o botão "iniciar"
        pagina_inicial.remove(botao) #Para remover o botão
        pagina_inicial.add(linha_enviar)
        pagina_inicial.add(campo_conversa)

        #Avisar quando o usuario entrar no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina_inicial.pubsub.send_all(mensagem)


        pagina_inicial.update()


    #criar alerta
    titulo_alerta = ft.Text("bem vindo ao ChatCasal")
    caixa_nome = ft.TextField (label= "digite o seu nome")
    botao_alerta = ft.ElevatedButton("Entrar no chat", on_click= entrar_chat)

    alerta = ft.AlertDialog(title= titulo_alerta, content= caixa_nome, 
                            actions= [botao_alerta]) # O actions serve para criar botão, precisa ir em colchetes pois as ações estão em plural e o colchetes serve como lista
    

    #botao
    def abrir_alerta(evento): #sempre associar um "on_click no botão, é necessario que no def atribuido, seja colocado um evento"
        pagina_inicial.dialog = alerta
        alerta.open = True #A pagina só podera ter um alerta por vez, não podendo exibir varios ao mesmo tempo 
        pagina_inicial.update() #Sempre que editar algo na pagina, sempre se deve acrescentar um pagina.update()
        

    
    #atribuições do botão
    botao = ft.ElevatedButton("Iniciar conversa" , on_click= abrir_alerta)
    pagina_inicial.add(botao)
    pagina_inicial.add(titulo)

    #Encerrar programa 
    #Ainda sendo trabalhado


#Executar essa função com o flet
ft.app(meu_chat , view=ft.WEB_BROWSER) 
