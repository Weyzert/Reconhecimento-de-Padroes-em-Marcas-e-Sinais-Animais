import numpy as np

def corrigir_gama(imagem, gama = 1.5):
    """
    Aplica a correção de gama.

    Args:
    imagem: A imagem para a correção.
    gama: O valor de gama para a correção.

    Returns:
    A imagem com o gama corrigido.
    """
    imagem_corrigida = np.power(imagem / 255.0, gama) * 255.0
    imagem_corrigida = np.uint8(imagem_corrigida)
    return imagem_corrigida