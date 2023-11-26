from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .pdi import pre_processamento, compare_images
import os
import cv2
import numpy as np

# Função para manipular o upload de imagens
def image_upload(request):
    # Verifica se a requisição é do tipo POST (quando o formulário é enviado)
    if request.method == 'POST':
        # Cria um formulário com os dados da requisição
        form = ImageUploadForm(request.POST, request.FILES)
        
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva o formulário, mas não o commita no banco de dados ainda
            instance = form.save(commit=False)

            # Obtém o diretório do script em execução
            script_directory = os.path.dirname(os.path.realpath(__file__))
            # Define o caminho da pasta onde as imagens estão armazenadas
            images_folder_path = os.path.join(script_directory, 'static', 'imagens')

            # Lista todos os arquivos de imagem na pasta e carrega cada imagem em uma lista
            image_files = [f for f in os.listdir(images_folder_path) if os.path.isfile(os.path.join(images_folder_path, f))]
            image_list = []
            for image_file in image_files:
                image_path = os.path.join(images_folder_path, image_file)
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                nome = image_path
                image_list.append((image, nome))

            # Decodifica a imagem enviada no formulário para o formato OpenCV
            query_image = cv2.imdecode(np.frombuffer(instance.image.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
            
            # Compara a imagem enviada com as imagens na lista
            result = compare_images(pre_processamento(query_image), image_list)

            # Renderiza a página HTML com o formulário e os resultados da comparação
            return render(request, 'myapp/image_upload.html', {'form': form, 'results': result})

    else:
        # Se a requisição não for do tipo POST, cria um formulário vazio
        form = ImageUploadForm()

    # Renderiza a página HTML com o formulário vazio
    return render(request, 'myapp/image_upload.html', {'form': form, 'results': None})

# Reload da aplicação (limpar a tela)
def clear_results(request):
    #ImageResult.objects.all().delete()
    return redirect('image_upload')