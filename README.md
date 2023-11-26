# Reconhecimento de Padrões em Marcas e Sinais usados em Animais
Este repositório abriga uma implementação de backend e frontend para um algoritmo de reconhecimento de imagens, projetado especialmente para identificar e comparar marcas e sinais utilizados em animais.

**Trabalho Prático de Desenvolvimento de Solução utilizando OpenCV - 2023/2**

Este repositório contém a implementação desenvolvida no âmbito do Trabalho Prático da disciplina CCC264 – Processamento Digital de Imagens, ministrada pelo Prof. Dr. Rafael Rieder e Prof. Mestre Mateus Eugênio Cole no segundo semestre de 2023 na UPF (Universidade de Passo Fundo).

**Objetivo:**
O objetivo deste trabalho é utilizar técnicas de pré-processamento, processamento e visão computacional, utilizando a biblioteca OpenCV. A solução proposta visa comparar imagens de marcas e sinais utilizados na identificação de animais.

**Funcionamento:**
A aplicação recebe uma imagem de entrada e realiza as seguintes etapas de pré-processamento:
```python
query_image = resize_fixed.redimensionar_imagem(query_image)  # Redimensiona a imagem para 128x128
query_image = gama.corrigir_gama(query_image, 1.5)  # Correção de gama em 1,5
query_image = medianBlur.mediana(query_image)  # Remoção de ruído (Espacial Mediana) em 1
query_image = equalizeHist.equalizacao_histograma(query_image)  # Equalização de Histograma
query_image = threshold.binarizacao(query_image)  # Binarização (Equalização do histograma) 128 à 255
query_image = gaussianBlur.gaussiano(query_image)  # Gaussiano (Anti-Aliasing) 5 por 5
```
A aplicação então utiliza algoritmos como SIFT, FLANN, HOG, euclidean_distances e cosine_similarity para comparar a imagem de entrada com uma lista de imagens pré-definida.

**Como Usar:**
Para comparar uma imagem de consulta com a lista de imagens, utilize a função `compare_images(query_image, image_list)`. Certifique-se de ter as bibliotecas necessárias instaladas: 
```python
pip install scikit-image
pip install scikit-learn
pip install opencv-python
pip install numpy
pip install django
```
**Instruções de Execução:**

1. Após instalar as bibliotecas necessárias, navegue até o diretório do projeto no terminal.

2. Execute o seguinte comando para iniciar o servidor local:
   ```bash
   python manage.py runserver
   ```
3. O projeto estará rodando em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

4. Acesse o front-end projetado para a aplicação em: [http://127.0.0.1:8000/myapp/image_upload/](http://127.0.0.1:8000/myapp/image_upload/)

5. Para limpar a tela, acesse: [http://127.0.0.1:8000/myapp/clear_results/](http://127.0.0.1:8000/myapp/clear_results/)

6. Para encerrar a aplicação, utilize o atalho **Ctrl + C** no terminal.

Certifique-se de manter o terminal aberto enquanto estiver usando a aplicação localmente. Se houver alguma dúvida ou problema durante a execução, sinta-se à vontade para entrar em contato para obter ajuda.

**Explicação do Código:**
O código realiza o pré-processamento da imagem de consulta e das imagens da lista. Em seguida, utiliza o descritor SIFT para extrair keypoints e descritores. A correspondência de características é feita usando o algoritmo FlannBasedMatcher. O código também calcula a similaridade utilizando a razão de correspondências boas e a distância euclidiana, incorporando características do descritor HOG (Histogram of Oriented Gradients) para a análise.

A função retorna uma lista ordenada de correspondências, contendo informações como: o nome da imagem, extensão, índice (referente ao diretório), caminho, similaridade Flann, similaridade percentual Flann, índice euclidiano, distância euclidiana, similaridade cosseno, OOE (Original Order Euclidean) e OOC (Original Order Cosine).

**Contribuidores:**
- Pedro Marcelo Roso Manica, 173722@upf.br | pedromarcelo9000@hotmail.com
- Victor Carneiro Cole, 183176@upf.br

**Licença:**
Este projeto está sob a licença GNU General Public License v3.0.
