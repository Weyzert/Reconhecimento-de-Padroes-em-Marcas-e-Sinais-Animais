import cv2

def binarizacao(imagem):
    """
    Aplica uma equalização de histograma a uma imagem.

    Args:
    imagem: A imagem a ser binarizada.

    Returns:
    A imagem binarizada.
    """
    valor_limiar = 128  # Valor de limiar (ajuste conforme necessário)
    valor_maximo = 255  # Valor máximo para pixels acima do limiar
    _, imagem_binaria = cv2.threshold(imagem, valor_limiar, valor_maximo, cv2.THRESH_BINARY)
    return imagem_binaria
