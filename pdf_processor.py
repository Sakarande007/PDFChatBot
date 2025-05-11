import PyPDF2
from typing import List, Dict

class PDFProcessor:
    def __init__(self):
        self.pdf_contents: Dict[str, str] = {}
    
    def process_pdf(self, pdf_file, filename: str) -> str:
        """Process a single PDF file and return its text content."""
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            # Store the content with the filename as key
            self.pdf_contents[filename] = text
            return text
        except Exception as e:
            raise Exception(f"Error processing PDF {filename}: {str(e)}")
    
    def get_all_content(self) -> str:
        """Get all processed PDF content combined."""
        return "\n\n".join(self.pdf_contents.values())
    
    def get_pdf_names(self) -> List[str]:
        """Get list of processed PDF filenames."""
        return list(self.pdf_contents.keys())
    
    def clear(self):
        """Clear all processed PDFs."""
        self.pdf_contents.clear() 