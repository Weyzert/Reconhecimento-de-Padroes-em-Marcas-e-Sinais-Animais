import cv2
import numpy as np

def filtro_sobel(imagem):
    """
    Aplica o filtro de Sobel para a detecção de bordas.
    Ruído impulsivo, como "sal e pimenta".

    Args:
    imagem: A imagem para a detecção de bordas.

    Returns:
    A imagem com o filtro aplicado.
    """
    sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)
    return np.sqrt(sobel_x**2 + sobel_y**2)
