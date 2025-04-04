# 🤖 Autobot - Automação de Processos e Manipulacao de Arquivos

Projeto de automação criado com foco em tarefas repetitivas, como atividades de rotina no desktop, extração de informações de imagens, manipulação de arquivos e scraping de preços na web.

---

## 📌 Funcionalidades

- **Desktop Automation**: Automatiza processos no Windows usando PyAutoGUI.
- **File Handler**: Verifica, identifica e remove duplicados em arquivos `.json`, além de exportar para `.csv`, `.xlsx` e `.xml`.
- **OCR Processor**: Extração de texto de imagens com Tesseract OCR e OpenCV.
- **Web Scraper**: Busca automatizada de preços na web usando Selenium.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- [PyAutoGUI](https://pypi.org/project/pyautogui/)
- [Selenium](https://pypi.org/project/selenium/)
- [pandas](https://pandas.pydata.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Pillow](https://pypi.org/project/Pillow/)
- [Logging](https://docs.python.org/3/library/logging.html)

---

## ▶️ Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/lgzanoni/RoboDoc.git
   cd RoboDoc
   ```
2. **Instale as dependências**:
   pip install -r requirements.txt

3. **Execute o menu principal**:
   python main.py

## 📦 Requisitos

    Além das bibliotecas Python, você precisa:

    Tesseract OCR instalado no sistema:

        Windows: Baixe em https://github.com/tesseract-ocr/tesseract/wiki

        Linux: sudo apt install tesseract-ocr

    Google Chrome instalado (para o Selenium funcionar corretamente).

    ChromeDriver compatível com sua versão do Chrome.

        Ajuste o caminho no código se necessário.

## ✍️ Autor

**Desenvolvido por Luis Gustavo Zanoni**
🔗 [LinkedIn](https://www.linkedin.com/in/luiszanoni/)
🐙 [GitHub](https://github.com/luiszanoni)
