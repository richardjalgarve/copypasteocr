# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from ocr import OCR

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Image Reader")

        self.ocr_processor = OCR(lang='por')

        self.label = tk.Label(root, text="Selecione uma imagem para realizar OCR:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Selecionar Imagem", command=self.select_image)
        self.select_button.pack(pady=5)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=10)

    def select_image(self):
        # Abre o diálogo para selecionar uma imagem
        image_path = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if image_path:
            # Extrai o texto da imagem
            text = self.ocr_processor.extract_text(image_path)
            # Exibe o texto extraído na caixa de texto
            self.result_text.delete(1.0, tk.END)  # Limpa o conteúdo anterior
            self.result_text.insert(tk.END, text)  # Insere o texto extraído

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
