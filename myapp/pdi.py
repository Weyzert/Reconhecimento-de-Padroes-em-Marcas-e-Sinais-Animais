from .preprocessamento import equalizeHist, gaussianBlur, medianBlur, resize_fixed, sobel, threshold, gama
from skimage.feature import hog
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
from scipy.spatial.distance import cityblock
import cv2
import numpy as np

def pre_processamento(query_image):
    """
    Realiza o uso de tecnicas de pré processamento de imagens.

    Args:
    imagem: A imagem a ser pré-processada.

    Returns:
    A imagem resultante do pré-processamento aplicado.
    """
    # Redimencionamento da imagem
    query_image = resize_fixed.redimensionar_imagem(query_image)

    # Correção de gama
    query_image = gama.corrigir_gama(query_image)

    # Remoção de ruído
        # Espacial Mediana
    query_image = medianBlur.mediana(query_image)         

    # Equalização de Histograma          
    query_image = equalizeHist.equalizacao_histograma(query_image)

    # Binarização (Equalização do histograma)
    query_image = threshold.binarizacao(query_image)

    # Gaussiano (Anti-Aliasing)
    query_image = gaussianBlur.gaussiano(query_image)

    # Remoção de ruído
        # Sobel
    #query_image = sobel.filtro_sobel(query_image)

#Remoção de ruído   USAR O SOBEL SOBRE O BINARIZADA GERA UMA IMAGEM HUMANAMENTE MAIS AGRADÁVEL que sobre o gaussinizada
        # Sobel
    #sobel = filtro_sobel(binarizada)

    return query_image

def compare_images(query_image, image_list):
    # Pré-processa a imagem de consulta
    query_image = pre_processamento(query_image)

    # Inicializa o detector SIFT
    sift = cv2.SIFT_create()

    # Extrai keypoints e descritores da imagem de query
    _, des_query = sift.detectAndCompute(query_image, None)

    # Inicializa o objeto BFMatcher e FlannBasedMatcher
    #bf = cv2.BFMatcher()
    flann = cv2.FlannBasedMatcher()

    # Parâmetros FLANN
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Lista para armazenar características HOG
    caracteristicas_banco_dados = []

    # Lista para armazenar as correspondências
    matches_list = []

    # Extraia características da imagem de consulta usando o descritor HOG
    features_query = hog(query_image, pixels_per_cell=(16, 16), cells_per_block=(2, 2), block_norm="L2-Hys", visualize=False)

    for index, (img, nome) in enumerate(image_list):
        # Pré-processa a imagem atual na lista
        img = pre_processamento(img)

        # Extrair características HOG
        features = hog(img, pixels_per_cell=(16, 16), cells_per_block=(2, 2), block_norm="L2-Hys", visualize=False)
        caracteristicas_banco_dados.append(features)

        # Calcula a similaridade do Cityblock entre as características HOG da imagem de consulta e da imagem atual na lista
        cityblock_similarity = cityblock(features_query, features)

        # Extrai keypoints e descritores da imagem atual na lista
        _, des_img = sift.detectAndCompute(img, None)

        # Realiza a correspondência de features usando o BFMatcher
        #bf_matches = bf.knnMatch(des_query, des_img, k=2)

        # Realiza a correspondência de features usando o FlannBasedMatcher
        flann_matches = flann.knnMatch(des_query, des_img, k=2)

        # Aplica o teste de razão para filtrar correspondências boas para BFMatcher
        #bf_good_matches = []
        #for m, n in bf_matches:
        #    if m.distance < 0.75 * n.distance:
        #        bf_good_matches.append(m)

        # Aplica o teste de razão para filtrar correspondências boas para FlannBasedMatcher
        flann_good_matches = []
        for m, n in flann_matches:
            if m.distance < 0.75 * n.distance:
                flann_good_matches.append(m)

        # Calcula o grau de semelhança como a razão de correspondências boas para o total de correspondências
        # A variável similarity calculada representa a fração de correspondências boas em relação ao total, onde 0 indica nenhuma correspondência e 1 indica todas as correspondências são consideradas boas.
        #bf_similarity = len(bf_good_matches) / len(bf_matches) if len(bf_matches) > 0 else 0
        flann_similarity = len(flann_good_matches) / len(flann_matches) if len(flann_matches) > 0 else 0

        # Armazena o resultado na lista de correspondências
        matches_list.append({
            #'img': img.tolist(),
            #'bf_similarity': bf_similarity,
            'flann_similarity': flann_similarity,
            'nome': nome.split("\\")[-1].split(".")[0],
            'extensao': nome.split('.')[-1],
            'index': index,
            'path': nome,
            #'bf_similarity_percent': bf_similarity * 100.0,
            'flann_similarity_percent': flann_similarity * 100.0,
            'cityblock_similarity_percent': cityblock_similarity * 100.0,  # Valores menores indicam maior semelhança
            #'cityblock_similarity_percent': 100.0 - cityblock_similarity * 100.0,  # Inverte para que valores menores sejam mais semelhantes'
        })

    # Converte as listas em matrizes NumPy
    X = np.array(caracteristicas_banco_dados)

    # Extraia características da imagem de consulta usando o descritor HOG
    features_query = hog(query_image, pixels_per_cell=(16, 16), cells_per_block=(2, 2), block_norm="L2-Hys", visualize=False)

    # Calcula a distância euclidiana entre a imagem de consulta e todas as imagens do banco de dados
    distancias_euclidianas = euclidean_distances([features_query], X)
    similaridade_cosseno = cosine_similarity([features_query], X)

    # Classifica as imagens com base na similaridade (distância euclidiana)
    # Retorna os índices que classificam os valores em ordem crescente. indices_classificados_euclidiana é usado para representar a ordem das imagens com base na distância euclidiana, do menor para o maior.
    indices_classificados_euclidiana = np.argsort(distancias_euclidianas)[0][::]

    # Classifica as imagens com base na similaridade do cosseno
    # Representa a ordem das imagens com base na similaridade de cosseno, do maior para o menor
    indices_classificados_cosseno = np.argsort(-similaridade_cosseno)[0][::]

    # Atualiza a lista de correspondências com informações adicionais
    for i, (idx_euclidiana, idx_cosseno) in enumerate(zip(indices_classificados_euclidiana, indices_classificados_cosseno)):
        matches_list[i].update({
            'euclidean_and_cosine_index': i,
            'euclidean_distance': distancias_euclidianas[0][idx_euclidiana],
            'cosine_similarity': similaridade_cosseno[0][idx_cosseno],
            'original_order_euclidiana': idx_euclidiana,
            'original_order_cosine': idx_cosseno,
        })

    # Ordena a lista de correspondências com base no grau de semelhança
    #matches_list = sorted(matches_list, key=lambda x: (x['bf_similarity'], x['flann_similarity']), reverse=True)
    matches_list = sorted(matches_list, key=lambda x: x['flann_similarity'], reverse=True)

    return matches_list