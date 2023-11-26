import cv2

def gaussiano(imagem):
    """
    Aplica umum filtro gaussiano a uma imagem (Anti-Aliasing).

    Args:
    imagem: A imagem a ser aplicado o filtro.

    Returns:
    A imagem com a remoção do ruído e suavizada.
    """
    kernel_size = (5, 5)  # Tamanho do kernel do filtro gaussiano (ímpar)
    return cv2.GaussianBlur(imagem, kernel_size, 0)
