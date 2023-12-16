import cv2

def redimenciona(imagem, fator_escala):
    """
    Redimenciona o tamanho de uma imagem com base em uma escala.
    Exemplos de escala: 0.1 (10%), 0.5 (50%), 0.99 (99%), 1.0 (100%)...

    Args:
    imagem: A imagem a ser redimencionada.
    fator_escala: Escala do redimencionamento em %.

    Returns:
    A imagem redimencionada.
    """
    altura, largura = imagem.shape[:2]
    return cv2.resize(imagem, (int (largura * fator_escala), int (altura * fator_escala)))
