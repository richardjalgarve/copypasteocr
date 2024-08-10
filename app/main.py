import tkinter as tk
from tkinter import filedialog, messagebox
import sys
from PyQt5.QtWidgets import QApplication
from ocr import OCR
from cut import ScreenshotSelector

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Image Reader")
        
        self.ocr_processor = OCR(lang='por')
        
        self._setup_widgets()

    def _setup_widgets(self):
        # Criação de um frame para alinhar os botões lado a lado
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.select_button = tk.Button(button_frame, text="Selecionar Imagem", command=self.select_image)
        self.select_button.pack(side=tk.LEFT, padx=5)

        self.cut_button = tk.Button(button_frame, text="Recortar", command=self.recortar)
        self.cut_button.pack(side=tk.LEFT, padx=5)

        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)

    def recortar(self):
        app = QApplication(sys.argv)
        selector = ScreenshotSelector()
        selector.show()
        app.exec_()
        screenshot_path = "screenshot.png"  # Presumindo que essa é a imagem salva
        self.processarOCR(screenshot_path)

    def select_image(self):
        # Abre o diálogo para selecionar uma imagem
        image_path = filedialog.askopenfilename(
            title="Selecione uma imagem", 
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if image_path:
            self.processarOCR(image_path)

    def processarOCR(self, image_path):
        try:
            # Extrai o texto da imagem
            text = self.ocr_processor.extract_text(image_path)
            # Exibe o texto extraído na caixa de texto
            self.result_text.delete(1.0, tk.END)  # Limpa o conteúdo anterior
            self.result_text.insert(tk.END, text)  # Insere o texto extraído
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar OCR: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
