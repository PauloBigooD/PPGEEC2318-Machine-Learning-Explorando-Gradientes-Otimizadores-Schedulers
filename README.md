
# PPGEEC2318 - Machine Learning: Otimização e Visualização no Aprendizado Profundo

Inspirado pelo livro *Deep Learning with PyTorch Step-by-Step*, este repositório é uma extensão do artigo publicado no Medium: ["Otimização e Visualização no Aprendizado Profundo: Explorando Gradientes, Otimizadores e Schedulers"](https://medium.com/@paulo.eduardo.093/otimiza%C3%A7%C3%A3o-e-visualiza%C3%A7%C3%A3o-no-aprendizado-profundo-explorando-gradientes-otimizadores-e-schedulers-d56f1a1d530e). Ele foi criado para aprofundar o entendimento dos conceitos apresentados, com foco no uso integrado de funções no PyTorch.

As simulações utilizam o dataset de gatos e cachorros, disponível no [Kaggle](https://www.kaggle.com/datasets/tongpython/cat-and-dog/data). O dataset possui cerca de 1.012 imagens para cada classe, sendo processado através de um pipeline otimizado de padronização de imagens e carregamento eficiente.

### Principais abordagens:
- Padronização e carregamento eficiente de dados com PyTorch;
- Uso de dropout para regularização;
- Exploração de otimizadores, schedulers e gradientes;
- Descoberta de taxas de aprendizado ideais e ajuste dinâmico de parâmetros.

---

## Como usar o notebook **PuttingAllTogether.ipynb**

Este notebook integra todos os conceitos apresentados no repositório, desde o pré-processamento dos dados até o ajuste de hiperparâmetros durante o treinamento. Abaixo, seguem instruções detalhadas para utilizá-lo em diferentes ambientes.

---

### 1. Usando o Google Colab

O **Google Colab** permite executar notebooks diretamente no navegador, sem a necessidade de configurar um ambiente local.

#### Passos:
1. **Acessar o notebook no Colab**:
   - No GitHub, copie o link do arquivo **PuttingAllTogether.ipynb**.
   - Substitua `github.com` no URL por `colab.research.google.com/github`. Por exemplo:
     ```
     https://github.com/usuario/repositorio/blob/main/PuttingAllTogether.ipynb
     ```
     Torna-se:
     ```
     https://colab.research.google.com/github/usuario/repositorio/blob/main/PuttingAllTogether.ipynb
     ```
   - Cole o link no navegador para abrir o notebook diretamente no Colab.

2. **Executar o notebook**:
   - Conecte-se ao ambiente de execução clicando em **Connect** (Conectar).
   - Execute as células do notebook sequencialmente (Shift+Enter).

3. **Configurar bibliotecas** (se necessário):
   - Certifique-se de instalar as dependências listadas no início do notebook. Execute o comando:
     ```bash
     !pip install -r requirements.txt
     ```

---

### 2. Usando o VS Code

Se preferir trabalhar localmente, o **VS Code** é uma ferramenta poderosa e personalizável.

#### Passos:
1. **Baixar o notebook**:
   - No GitHub, clique no arquivo **PuttingAllTogether.ipynb** e, em seguida, em **Raw**.
   - Salve o arquivo localmente como `.ipynb`.

2. **Abrir no VS Code**:
   - Certifique-se de ter a extensão **Jupyter** instalada.
   - Abra o arquivo no VS Code e configure um kernel Python compatível.

3. **Configurar dependências**:
   - Crie um ambiente virtual e instale as bibliotecas necessárias:
     ```bash
     python -m venv .env
     source .env/bin/activate   # No Windows: .env\Scripts\activate
     pip install -r requirements.txt
     ```

4. **Executar o notebook**:
   - Use o comando **Run All** ou execute célula por célula.

---

### 3. Usando Jupyter Notebook Localmente

Outra opção é executar o notebook no ambiente local utilizando o **Jupyter Notebook**.

#### Passos:
1. **Instalar o Jupyter Notebook**:
   - Instale o Jupyter no seu ambiente Python:
     ```bash
     pip install notebook
     ```

2. **Baixar o notebook**:
   - Faça o download do arquivo **PuttingAllTogether.ipynb** no GitHub.

3. **Executar o Jupyter**:
   - Navegue até a pasta onde o arquivo foi salvo e execute:
     ```bash
     jupyter notebook
     ```
   - O ambiente será aberto no navegador, onde você poderá executar o notebook.

4. **Configurar dependências**:
   - Instale as bibliotecas necessárias antes de executar as células.

---

Se precisar de ajuda ou encontrar problemas, sinta-se à vontade para abrir uma *issue* no repositório. Feedbacks são sempre bem-vindos! 😊
