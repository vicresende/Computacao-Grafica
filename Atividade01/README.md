# Atividade 01 - 09/10

Na atividade 01, foi seguido o tutorial _"Ray Tracing in One Weekend"_ até a Seção 2. Estes passos incluíram o desenvolvimento de um código em _`python`_ que irá criar uma imagem e seu arquivo no formato _`.ppm`_.
O arquivo _`ativ1.py`_ foi executado através do comando _`python ativ1.py`_, e a imagem foi criada e carregada no computador.
Após as implementações iniciais, o código foi complementado criando uma classe própria para salvar imagens, assim como funções para a criação de imagens específicas.

# Gerador de Imagens
Este é um projeto simples que gera imagens em formato PPM e PNG. O projeto inclui uma classe chamada `ImageSaver` que permite salvar imagens nos formatos PPM e PNG e três funções para gerar diferentes tipos de imagens: degradê, círculo e quadrado, sendo possível personalizar essas funções para criar imagens com cores e tamanhos diferentes.

## Como Funciona

1. Clone este repositório para sua máquina local.

2. Abra o arquivo `ativ1.py` em um editor de código.

3. Você pode personalizar a largura (`width`) e altura (`height`) das imagens e as cores nas funções de geração de imagens (degradê, círculo e quadrado).

4. Execute o script `ativ1.py` usando o Python:

   ```bash
   python ativ1.py

5. As imagens geradas serão salvas no diretório atual nos formatos PPM e PNG com nomes como `gradient.ppm`, `gradient.png`, `circle.ppm`, `circle.png`, `square.ppm` e `square.png`.

## Requisitos

- Python 3.x
- NumPy (biblioteca para computação numérica, instalável via `pip install numpy`)
- Pillow (biblioteca para manipulação de imagens, instalável via `pip install Pillow`)

## Output Esperado

Após executar o script `ativ1.py`, você encontrará as imagens geradas nos formatos PPM e PNG no diretório atual. É possível visualizar essas imagens usando qualquer visualizador de imagens ou ferramenta de edição de imagem que suporte esses formatos.

## Personalização

Você pode personalizar as imagens geradas ajustando os parâmetros nas funções `generate_gradient`, `generate_circle` e `generate_square` no arquivo `ativ1.py`. Você pode alterar as cores, tamanhos e outros atributos conforme suas preferências.
