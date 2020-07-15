from tkinter import * 
from tkinter import ttk
from methods import Mytranslator
from googletrans import Translator, LANGUAGES
app = Tk()
app.geometry('350x520')
app.title('translator')
app.resizable(0,0)
app.config(bg='blue')
appName = Label(app,text='My Translator',font=('helvetica',20),bg='green',fg='goldenrod1',height=2)
appName.pack(side=TOP,fill=BOTH,pady=0)
version=Label(app,text='beta',bg='green').place(x=250,y=45)
frame=Frame(app).pack(side=BOTTOM)
sourceText=Text(frame,font=('arial',10),height=11,wrap=WORD)
sourceText.pack(side=TOP,padx=5,pady=5)
transBtn =Button(frame,text='translate',font=('arial',10,'bold'),fg='red',bg='blue',activebackground='green',relief=GROOVE)
transBtn.pack(side=TOP,pady=15)
ld = Mytranslator(list(LANGUAGES.values()))
langs = ld.langs
srcLangs = ttk.Combobox(frame,values=langs,width=10)
srcLangs.place(x=30,y=280)
srcLangs.set('English')
destLangs = ttk.Combobox(frame,values=langs,width=10)
destLangs.place(x=240,y=280)
destLangs.set('Hindi')
destText=Text(frame,font=('arial',10),height=11,wrap=WORD)
destText.pack(side=TOP,padx=5,pady=5)
app.mainloop()
