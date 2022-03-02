# Ca-a-palavras
Rotina para criar caça-palavras - em Excel e Python


Para que comprar Caça-Palavras em bancas de jornal? Crie o seu próprio passatempo personalizado com suas palavras.


Basta listar as palavras a serem escondidas e rodar, com macros ativadas.

![](https://ideiasesquecidas.files.wordpress.com/2022/03/caca01.png)

É uma rotina relativamente simples, e um bom exercício é tentar reescrevê-la do zero.

O procedimento é:

– Ler as strings

– Para cada uma, sortear se a posição é horizontal ou vertical

– Pelo tamanho, verificar quais as posições iniciais onde a palavra “cabe”

– Sortear uma posição inicial

– Verificar se a palavra inteira coincide com outras palavras já postas e repetir até conseguir

– Preencher casas restantes com letras aleatórias

O “Modo debug” não preenche o restante com letras aleatórias, é só para conferir se a lógica funciona.

![](https://ideiasesquecidas.files.wordpress.com/2022/03/caca02.png)

É possível adaptar para deixar mais fácil e lúdico, para crianças: mudar a fonte, aumentar tamanho das células, cores, etc…

A cada vez que rodar, um resultado diferente vai ser gerado.

No exemplo a seguir, inseri um “BLUEBERRY” a mais.

![](https://ideiasesquecidas.files.wordpress.com/2022/03/caca03.png)


Outro exercício computacional é o inverso: a partir do caça-palavras, tentar descobrir onde está a palavra, a partir de uma lista – basta algumas varreduras com loop “for”.
