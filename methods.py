from googletrans import Translator, LANGUAGES
print(LANGUAGES)
class Mytranslator:

    def __init__ (self , langs):
        self.langs = langs
    def run(self,txt='type text here',src='English',dest='Hindi'):
        self.translator = Translator()
        self.txt = txt
        self.src = src
        self.dest = dest
        try:
            self.translated = self.translator.translate(self.txt,src=self.src,dest=self.dest)
        except:
            self.translated = self.translator.translate(self.txt)
            self.ttext = self.translated.text
        return self.ttext  
