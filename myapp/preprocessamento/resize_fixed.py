import cv2

def redimensionar_imagem(imagem, tamanho_desejado = (128, 128)):
    """
    Redimenciona a imagem para o tamanho desejado.

    Args:
    imagem: A imagem a ser redimencionada.
    tamanho_desejado: O tamanho que a imagem terá.

    Returns:
    A imagem redimencionada para o tamanho escolhido.
    """
    return cv2.resize(imagem, tamanho_desejado)
