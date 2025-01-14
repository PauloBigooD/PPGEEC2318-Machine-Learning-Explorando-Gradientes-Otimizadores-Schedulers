# PPGEEC2318-Machine-Learning-Otimiza-o-e-Visualiza-o-no-Aprendizado-Profundo

Inspirado pelo autor do livro Deep Learning with PyTorch Step-by-Step, este repositório é uma extensão do artigo publicado no Medium ["Título do Artigo"](colocar link), criado para aprofundar o entendimento dos conceitos apresentados, com ênfase no uso e integração das funções no PyTorch.

As simulações foram realizadas no Google Colab, utilizando um novo dataset, disponível em [![Kaggle](https://img.shields.io/badge/Kaggle-119ebd?style=plastic&logoColor=white)](https://www.kaggle.com/datasets/tongpython/cat-and-dog/data). Esse dataset contém imagens de gatos e cachorros, totalizando aproximadamente 1.012 imagens para cada classe.

No repositório, desenvolvemos um método para padronizar as imagens de forma eficiente, utilizando um carregador de dados temporário. Além disso, adotamos um modelo mais sofisticado, que inclui camadas de dropout para regularização.

O foco também foi ampliado para o processo de treinamento, com atenção especial a taxas de aprendizado, otimizadores e schedulers. Diversos métodos foram implementados, incluindo:

- Descoberta de taxas de aprendizado ideais;
- Captura de gradientes e parâmetros do modelo;
- Atualização dinâmica da taxa de aprendizado por meio de schedulers.
