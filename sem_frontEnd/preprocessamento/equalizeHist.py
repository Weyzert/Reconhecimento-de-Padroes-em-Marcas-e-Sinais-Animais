import cv2

def equalizacao_histograma(imagem):
    """
    Aplica uma equalização de histograma a uma imagem.

    Args:
    imagem: A imagem a ser equalizada.

    Returns:
    A imagem equalizada.
    """
    return cv2.equalizeHist(imagem)
