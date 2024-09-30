# MMPose trainer
Este repositório possui os códigos e arquivos que foram utilizados para realizar um treinamento customizado utilizando a biblioteca [MMPose](https://github.com/open-mmlab/mmpose).

[Vídeo com todas as explicações](https://www.youtube.com/watch?v=WCb6mLgtlCo)

## Pré-requisitos
Abaixo seguem as principais bibliotecas instaladas para fazer o treinamento de um Pose Estimator:
- Python == 3.11.9


- pip install torch
- pip install numpy==1.26.4
- pip install -U openmim
- mim install mmengine
- mim install mmcv
- mim install mmdet  # Optional: Only if going to use detection model from the MMDet library
- mim install mmpose
- mim install mmpretrain
- pip install ultralytics  # Optional: Only if going to use YOLOv8 as a detector

OBS: Em environment.yml está o ambiente do Anaconda utilizado, contendo todas as bibliotecas e suas versões.

## Como rodar
Para realizar o treinamento é necessário clonar o repositório oficial do [MMPose](https://github.com/open-mmlab/mmpose), os códigos e arquivos neste repositório foram utilizados no vídeo mencionado no início do README.

Deixei em "work_dirst" o modelo de detecção do YOLO treinado e mencionado no vídeo para poder ser usado como fins de estudo.

As anotações se referem ao dataset [Humpback Whale Identification](https://www.kaggle.com/c/humpback-whale-identification/overview) e estão no formato COCO prontos pare sem utilizado no treinamento.

## Autor
* **Programador Artificial** - [GitHub](https://github.com/ProgramadorArtificial) - [YouTube](https://www.youtube.com/@ProgramadorArtificial)