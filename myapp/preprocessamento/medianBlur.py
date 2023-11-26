import cv2

def mediana(imagem, kernel_size=1):
    """
    Remove ruído de uma imagem usando um filtro (espacial) de mediana.
    Ruído impulsivo, como "sal e pimenta".

    Args:
    imagem: A imagem com ruído.
    kernel_size: Tamanho da janela do filtro de mediana.

    Returns:
    A imagem sem ruído.
    """
    return cv2.medianBlur(imagem, kernel_size)
