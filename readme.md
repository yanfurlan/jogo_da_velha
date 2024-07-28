# Jogo da Velha em Python

Este é um simples jogo da velha (Tic-Tac-Toe) desenvolvido em Python utilizando a biblioteca `tkinter` para a interface gráfica.

## Funcionalidades

- Dois jogadores podem jogar alternadamente clicando nos botões para marcar suas jogadas.
- O jogo detecta e anuncia o vencedor ou se o jogo terminou em empate.
- Um botão de "Resetar" permite reiniciar o jogo a qualquer momento.

## Requisitos

- Python 3.x
- `tkinter` (normalmente incluído na instalação padrão do Python)

## Como Executar

1. Clone este repositório ou baixe os arquivos.

2. Execute o script `jogo_da_velha.py`:

    ```sh
    python jogo_da_velha.py
    ```

3. A interface gráfica do jogo será exibida. Os jogadores podem clicar nos botões para jogar.

## Estrutura do Código

- **check_winner(board)**: Função que verifica se há um vencedor no tabuleiro.
- **check_draw(board)**: Função que verifica se o jogo terminou em empate.
- **on_button_click(row, col)**: Função chamada quando um botão é clicado. Atualiza o tabuleiro e verifica o estado do jogo.
- **reset_board()**: Função que reseta o tabuleiro para o estado inicial.

## Interface Gráfica

A interface gráfica é criada utilizando a biblioteca `tkinter`, com um layout simples que contém um tabuleiro de 3x3 e um botão para resetar o jogo.

## Capturas de Tela

![Screenshot 1](screenshot_1.png)
![Screenshot 2](screenshot_2.png)

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

