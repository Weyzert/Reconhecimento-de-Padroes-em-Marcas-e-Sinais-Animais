# Reconhecimento de Padrões em Marcas e Sinais usados em Animais
Este repositório abriga uma implementação de backend e frontend para um algoritmo de reconhecimento de imagens, projetado especialmente para comparar imagens de marcas e sinais utilizados na identificação de animais.

**Trabalho Prático de Desenvolvimento de Solução utilizando OpenCV - 2023/2**

Este repositório contém a implementação desenvolvida no âmbito do Trabalho Prático da disciplina CCC264 – Processamento Digital de Imagens, ministrada pelo Prof. Dr. Rafael Rieder e Prof. Mestre Mateus Eugênio Cole no segundo semestre de 2023 na UPF (Universidade de Passo Fundo).

**Objetivo:**
O objetivo deste trabalho é utilizar técnicas de pré-processamento, processamento e visão computacional, utilizando a biblioteca OpenCV. A solução proposta visa comparar imagens de marcas e sinais utilizados na identificação de animais.

---

## Contextualização do Problema
O desenvolvimento deste projeto é uma resposta à necessidade premente de aprimorar o processo de cadastro de marcas e sinais de animais, um aspecto vital na gestão do meio rural. Atualmente, esse cadastro envolve a digitalização da marca e do sinal dos animais, realizada por meio de scanners ou fotografias.

No momento do cadastro, o produtor rural enfrenta o desafio de entregar uma imagem legível, sem desfoques e com boa iluminação da marca/sinal utilizada para a identificação do animal sob sua posse. Esta etapa é crucial para garantir a precisão e confiabilidade do cadastro digital, já que a qualidade da imagem impacta diretamentena identificação correta dos animais.

Antigamente, esse processo de vinculação da marca/sinal do produtor rural, utilizado para identificar os animais em sua posse, era registrado manualmente em um livro. Entretanto, com a transição para a digitalização, surge a oportunidade de criar um algoritmo que auxilie a máquina pública durante o cadastro, garantindo que a marca/símbolo a ser registrada no sistema seja única e distinta das demais.

### Funcionamento:
A aplicação recebe uma imagem de entrada e realiza as seguintes etapas de pré-processamento:
```python
query_image = resize_fixed.redimensionar_imagem(query_image)  # Redimensiona a imagem para 128x128
query_image = gama.corrigir_gama(query_image, 1.5)  # Correção de gama em 1,5
query_image = medianBlur.mediana(query_image)  # Remoção de ruído (Espacial Mediana) em 1
query_image = equalizeHist.equalizacao_histograma(query_image)  # Equalização de Histograma
query_image = threshold.binarizacao(query_image)  # Binarização (Equalização do histograma) 128 à 255
query_image = gaussianBlur.gaussiano(query_image)  # Gaussiano (Anti-Aliasing) 5 por 5
```
A imagem de consulta `query_image`, bem como aquelas contidas na lista `image_list`, são processadas em escala de cinza, utilizando a `cv2.IMREAD_GRAYSCALE` para garantir consistência no tratamento das informações visuais.

A `image_list` é formada a partir das imagens contidas em `myapp/static/imagens`.

A aplicação então utiliza algoritmos como SIFT, FLANN, HOG, euclidean_distances e cosine_similarity para comparar a imagem de entrada com uma lista de imagens pré-definida.

**Como Usar:**
Para comparar uma imagem de consulta com a lista de imagens, utilize a função `compare_images(query_image, image_list)`. Certifique-se de ter as bibliotecas necessárias instaladas: 
```python
pip install scikit-image
pip install scikit-learn
pip install opencv-python
pip install numpy
pip install django
pip install scipy
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
O código realiza o pré-processamento da imagem de consulta e das imagens da lista. Em seguida, utiliza o descritor SIFT para extrair keypoints e descritores. A correspondência de características é feita usando o algoritmo FlannBasedMatcher. O código também calcula a similaridade utilizando a razão de correspondências boas, a distância euclidiana, a similaridade por cosseno, e a similaridade do cityblock incorporando características do descritor HOG (Histogram of Oriented Gradients) para a análise.

A função retorna uma lista ordenada de correspondências, contendo informações como: o nome da imagem, extensão, índice (referente ao diretório), caminho, similaridade Flann, similaridade percentual Flann, índice euclidiano, distância euclidiana, similaridade cosseno, similaridade percentual cityblock, OOE (Original Order Euclidean) e OOC (Original Order Cosine).

- **Distância Euclidiana:**
  - Reflete o quão próximo de 0 o valor é, indicando uma menor distância entre os vetores (ou imagens). Valores mais próximos de zero sugerem uma maior semelhança.

- **Similaridade Cosseno:**
  - Varia de -1 a 1, onde -1 representa vetores (ou imagens) totalmente opostos, 1 indica total identidade e 0 denota vetores ortogonais. Quanto mais próximo de 1, maior a similaridade.

- **Similaridade Percentual Cityblock:**
  - Quanto menor o valor retornado, maior é a similaridade. Se for zero, os vetores (ou imagens) são idênticos; quanto maior, menor a similaridade entre eles. Esta medida é sensível a diferenças entre os valores dos descritores.

- **Similaridade FLANN Matcher:**
  - Utiliza o algoritmo FlannBasedMatcher para realizar correspondência de características. A similaridade é calculada como a razão de correspondências boas para o total de correspondências, usando a fórmula:
    \[
    \text{Similaridade FLANN} = \frac{\text{Número de Correspondências Boas}}{\text{Número Total de Correspondências}}
    \]
  - A seleção de correspondências boas é feita através da comparação das distâncias entre as duas melhores correspondências para cada descritor:
    ```python
    for m, n in flann_matches:
        if m.distance < 0.75 * n.distance:
            flann_good_matches.append(m)
    ```
  - Valores mais altos indicam uma maior confiança nas correspondências encontradas.

### Sem o Front-end

O diretório `sem_frontEnd` contém o arquivo `teste.py`, que oferece uma implementação do algoritmo sem o uso do Django para a criação do Front-end. 

**Nota:**
O algoritmo implementado sem o uso do Django apresenta uma precisão mais elevada.

**Contribuidores:**
- Pedro Marcelo Roso Manica, 173722@upf.br | pedromarcelo9000@hotmail.com
- Victor Carneiro Cole, 183176@upf.br

**Licença:**
Este projeto está sob a licença GNU General Public License v3.0.
