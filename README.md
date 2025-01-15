# PPGEEC2318-Machine-Learning-Otimiza-o-e-Visualiza-o-no-Aprendizado-Profundo

Inspirado pelo autor do livro Deep Learning with PyTorch Step-by-Step, este repositório é uma extensão do artigo publicado no Medium ["Otimização e Visualização no Aprendizado Profundo: Explorando Gradientes, Otimizadores e Schedulers"](https://medium.com/@paulo.eduardo.093/otimiza%C3%A7%C3%A3o-e-visualiza%C3%A7%C3%A3o-no-aprendizado-profundo-explorando-gradientes-otimizadores-e-schedulers-d56f1a1d530e), criado para aprofundar o entendimento dos conceitos apresentados, com ênfase no uso e integração das funções no PyTorch.


As simulações foram realizadas no Google Colab, utilizando um novo dataset, disponível em [![Kaggle](https://img.shields.io/badge/Kaggle-119ebd?style=plastic&logoColor=white)](https://www.kaggle.com/datasets/tongpython/cat-and-dog/data). Esse dataset contém imagens de gatos e cachorros, totalizando aproximadamente 1.012 imagens para cada classe.

No repositório, desenvolvemos um método para padronizar as imagens de forma eficiente, utilizando um carregador de dados temporário. Além disso, adotamos um modelo mais sofisticado, que inclui camadas de dropout para regularização.

O foco também foi ampliado para o processo de treinamento, com atenção especial a taxas de aprendizado, otimizadores e schedulers. Diversos métodos foram implementados, incluindo:

- Descoberta de taxas de aprendizado ideais;
- Captura de gradientes e parâmetros do modelo;
- Atualização dinâmica da taxa de aprendizado por meio de schedulers.


---

## 1. Usar o Google Colab
Google Colab é uma plataforma gratuita baseada em nuvem para executar notebooks.

### Passos:
1. **Abrir no Colab diretamente**:
   - Acesse o repositório no GitHub.
   - Substitua `github.com` no link por `colab.research.google.com/github`. Por exemplo:
     ```
     https://github.com/usuario/repositorio/blob/main/notebook.ipynb
     ```
     Torne-se:
     ```
     https://colab.research.google.com/github/usuario/repositorio/blob/main/notebook.ipynb
     ```

2. **Ou abra manualmente no Colab**:
   - Copie o URL do arquivo `.ipynb` no GitHub.
   - Abra o [Google Colab](https://colab.research.google.com/).
   - Clique em **File > Open notebook** (Arquivo > Abrir notebook).
   - Vá até a aba **GitHub**, cole o URL e carregue o notebook.

3. Execute as células no Colab diretamente.

---

## 2. Usar o VS Code
Se você prefere executar localmente, o VS Code é uma ótima ferramenta.

### Passos:
1. **Baixar o notebook do GitHub**:
   - No GitHub, clique em **Raw** no arquivo `.ipynb` e salve o conteúdo como um arquivo local (Ctrl+S ou Cmd+S).

2. **Abrir no VS Code**:
   - Certifique-se de ter a extensão **Jupyter** instalada no VS Code.
   - Abra o arquivo `.ipynb` no VS Code.
   - Clique em **Run All** ou execute célula por célula.

3. **Configure o ambiente Python**:
   - Instale o Python e as bibliotecas necessárias no seu ambiente virtual.

---

## 3. Usar Jupyter Notebook Localmente
Outra opção é usar o Jupyter Notebook na sua máquina.

### Passos:
1. **Baixar o notebook**:
   - Faça o download do arquivo `.ipynb` no GitHub.

2. **Instalar Jupyter**:
   - Certifique-se de ter o Jupyter instalado no seu ambiente Python:
     ```bash
     pip install notebook
     ```

3. **Executar o notebook**:
   - No terminal, navegue até a pasta onde o arquivo `.ipynb` está salvo.
   - Execute o comando:
     ```bash
     jupyter notebook
     ```
   - Seu navegador abrirá o ambiente do Jupyter, onde você pode carregar e executar o notebook.
