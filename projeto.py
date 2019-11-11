"""
Código Cifra de substutuição
"""
# .lower() <- Transforma tudo digitado em letras MINUSCULAS
# \033[1;31m ...... \033[m <- Define cor vermelha
# \033[;1m ...... \033[m <- Define cor negrito

x = False
while not x:
    def recebe_opc():
        """
        Função que pergunta se o usuário quer criptografar ou
        decriptografar e garante que uma entrada válida foi recebida
        """

        while True:
            option = input("Você Deseja criptografar, 'c' ou descriptografar, 'd' uma mensagem? ").lower()
            if option == 'c' or option == 'criptografar' or option == 'descriptografar' or option == 'd':
                return option
            print("\033[1;31mEntrada inválida. Escolha entre ('criptografar', 'c') ou ('descriptografar', 'd')\033[m")

    def recebe_valor_chave():
        """
        Função que pede o valor da chave e aceita apenas a
        chave caso o valor desta esteja adequado.
        """

        ok = False
        valor = 0
        while True:
            chave = str(input("Digite um valor numérico para a chave: "))
            if chave.isnumeric():
                valor = int(chave)
                ok = True
            else:
                print("\033[1;31mERRO! Digite um número inteiro válido\033[m")
            if ok:
                break
        return valor


    def gera_msg_traduzida(modo, mensagem, chave):
        """
        Traduz a mensagem do usuário de modo conveniente
        """
        cripto = ''
        q = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Ç', 'ü',
             'é', 'â', 'ä', 'à', 'å', 'ç', 'ê', 'ë', 'è', 'ï', 'î', 'ì', 'Ä', 'Å', 'É', 'æ', 'Æ', 'ô',
             'ö', 'ò', 'û', 'ù', 'Ö', 'Ü', 'ø', '£', 'Ø', '×', 'ƒ', 'á', 'í', 'ó', 'ú', 'ñ', 'Ñ', 'ã',
             'Ã', '¤', 'Ð', 'Ê', 'Ë', 'È', 'i', 'Í', 'Î', 'Ï', 'Ì', 'Ó', 'ß', 'Ô', 'Ò', 'Õ', 'Õ', 'µ',
             'Þ', 'Þ', 'Ú', 'Û', 'Ù', 'ý', 'Ý', 'ð', 'ÿ', '!', '"', '#', '$', '%', '&', '(', ')', '*',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', ',', '-', '.', '/', ':', ';', '<',
             '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', 'ª', 'º', '¿', '®', '¬',
             '½', '¼', '«', '»', '¦', 'Á', 'Â', 'À', '©', '¢', '¥', '¯', '´', '±', '¾', '¶', '§',
             '÷', '°', '¨', '·', '¹', '³', '²', '¡', ' ']
        """Ultiliza uma lista com os principais caracteres para criptografar """
        """ Condição para criptografar"""
        if modo == 'c' or modo == 'criptografar':
            for i in mensagem:
                if i in q:
                    v = q.index(i)
                    cripto += q[(v + chave) % len(q)]
                else:
                    cripto += i  # Caso um caracter não esteja na lista ele adiciona
            print("Sua mensagem criptografada é:", cripto)
        """ Condição para descriptografar """
        if modo == 'd' or modo == 'descriptografar':
            for i in mensagem:
                if i in q:
                    v = q.index(i)
                    cripto += q[(v - chave) % len(q)]
                else:
                    cripto += i
            print("Sua mensagem descriptografada é:", cripto)
        return cripto

    def main():
        """
        Função principal do programa
        """
        print("\033[;1mCódigo de Criptografia e Descriptografia com principios de cifra de substituição\033[m")
        modo = recebe_opc()
        chave = recebe_valor_chave()
        mensagem = str(input("Digite a mensagem: "))
        gera_msg_traduzida(modo, mensagem, chave)

    main()
    s = str(input("Deseja executar o codigo novamente ? Digite Y para 'sim' ou N para 'não': ").upper())

    if s == "Y" or s == "SIM":
        x = False
    else:
        print("\033[1;31mEntrada inválida. Escolha entre ('sim', 'Y') ou ('não', 'N')\033[m")
