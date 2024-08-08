# OCR com Tesseract e Python

Este projeto demonstra como usar o Tesseract OCR em um script Python para extrair texto de imagens. O código foi organizado em classes e possui uma interface gráfica (GUI) simples para facilitar o uso.

## Requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Tesseract-OCR**: 
  - [Instruções de Instalação](https://github.com/tesseract-ocr/tesseract)
  - **Windows**: Baixe o instalador [aqui](https://github.com/tesseract-ocr/tesseract/wiki).
  - **Linux/MacOS**: Instale via pacote `apt-get` ou `brew`.
  
  ```bash
  sudo apt-get install tesseract-ocr  # Para Ubuntu/Debian
  brew install tesseract              # Para macOS
  ```

- **Bibliotecas Python**: 
  - As dependências do Python estão listadas no arquivo `requirements.txt`. Para instalá-las, siga as instruções abaixo.

- **Modelo de Idioma Português (opcional)**:
  - Baixe o modelo de idioma português em: [por.traineddata](https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata).
  - Após fazer o download do arquivo `por.traineddata`, salve-o na pasta `tessdata` do Tesseract. Por padrão, essa pasta está localizada em:
    - **Windows**: `C:\Program Files\Tesseract-OCR\tessdata`
    - **Linux/MacOS**: `/usr/share/tesseract-ocr/4.00/tessdata/` ou similar, dependendo da instalação.

## Instalação

### 1. Clone o Repositório

Clone o repositório para sua máquina local usando o Git:

```bash
git clone https://github.com/SeuUsuario/SeuRepositorio.git
cd SeuRepositorio
```

### 2. Crie e Ative um Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para gerenciar as dependências do projeto.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/MacOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências

Com o ambiente virtual ativado, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 4. Configure o Tesseract

Após instalar o Tesseract, certifique-se de que o caminho para o executável esteja incluído no seu `PATH` ou configure diretamente no código Python, caso necessário.

Exemplo para Windows:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 5. Execute o Script

Agora você pode executar o script principal (`main.py`) para iniciar a aplicação:

```bash
python main.py
```

Uma interface gráfica será exibida, permitindo que você selecione uma imagem e extraia o texto utilizando o Tesseract OCR.

## Uso

1. **Selecione uma Imagem**: Use o botão "Selecionar Imagem" na GUI para carregar a imagem da qual deseja extrair o texto.
2. **Extraia o Texto**: O texto extraído da imagem será exibido na caixa de texto da interface.

## Problemas Comuns

- **Erro "Tesseract não está instalado ou não está no PATH"**: Verifique se o Tesseract está instalado corretamente e se o caminho para o executável está configurado no `PATH`.
- **Erro ao carregar o arquivo de dados de idioma**: Verifique se o idioma especificado está disponível na pasta `tessdata`. Para o idioma português, baixe o arquivo `por.traineddata` [aqui](https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata) e salve-o na pasta `tessdata` conforme indicado.

## Contribuição

Se desejar contribuir com o projeto, sinta-se à vontade para fazer um fork do repositório, criar uma branch e enviar um pull request.

## Licença

Este projeto está licenciado sob os termos da licença MIT.
