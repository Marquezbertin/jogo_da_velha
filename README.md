# jogo_da_velha
Bem-vindo ao jogo da velha implementado em Python! Este é um jogo clássico para dois jogadores, onde cada jogador alterna jogadas para preencher um tabuleiro 3x3 com seus símbolos (X ou O). O primeiro jogador a completar uma linha, coluna ou diagonal com seu símbolo ganha o jogo. Se todas as posições do tabuleiro forem preenchidas e ninguém ganhar, o jogo termina em empate.

## Requisitos
Python 3.7 ou superior.

## Como Jogar
* Clone este repositório ou baixe o arquivo Python contendo o jogo da velha.
* Execute o arquivo Python em seu terminal ou ambiente de desenvolvimento integrado (IDE) preferido.
* Os jogadores serão solicitados a inserir seus nomes.
* O jogo começa com o jogador X fazendo a primeira jogada.
* Cada jogador, na sua vez, será solicitado a escolher uma linha e uma coluna (de 0 a 2) para fazer sua jogada.
* O tabuleiro será exibido após cada jogada, para que os jogadores possam acompanhar o progresso do jogo.
* O jogo continua até que um jogador ganhe ou que o tabuleiro esteja cheio, resultando em um empate.

## Código
O código consiste em várias funções principais:

* criar_tabuleiro(): Cria um tabuleiro 3x3 vazio.
* imprimir_tabuleiro(tabuleiro): Imprime o tabuleiro no console.
* verificar_vitoria(tabuleiro, jogador): Verifica se o jogador atual venceu o jogo.
* fazer_jogada(tabuleiro, jogador, nome_jogador): Permite que um jogador faça uma jogada.
* jogo_da_velha(): Função principal para rodar o jogo da velha.
  
## Exemplo de Uso
Aqui está um exemplo de como executar o jogo da velha:

shell
Copy code: 
python jogo_da_velha.py

## Instruções Adicionais
Insira a linha e coluna escolhidas para sua jogada quando for solicitado.
Siga as instruções do console para jogar e acompanhar o progresso do jogo.

## Contribuições
Este é um projeto básico de exemplo para jogar jogo da velha em Python. Sinta-se à vontade para fazer melhorias e ajustes no código conforme necessário.

Licença
Este projeto está licenciado sob a licença MIT. 