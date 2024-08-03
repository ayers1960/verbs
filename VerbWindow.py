import tkinter as tk


class VerbWindow(tk.Tk):
    def __init__(self,verbs):
        super().__init__()
        font = ("Ariel", 25)
        self.v = 0
        self.verbs = verbs
        self.maxX = 1024
        self.maxY = 700
        maxX = self.maxX
        maxY = self.maxY
        self.geometry(f"{self.maxX}x{self.maxY}")

        self.prevButton = tk.Button(self, text="PREV",
                                    font=('Ariel', 20),
                                    command=lambda:self.setVerbs(self.v-1))
        self.prevButton.place(x=int(self.maxX*0.25),y=int(self.maxY-35), anchor=tk.CENTER)

        self.nextButton = tk.Button(self, text="NEXT", 
                                    font=('Ariel', 20),
                                    command=lambda:self.setVerbs(self.v+1))
        self.nextButton.place(x=int(self.maxX*0.75),y=int(self.maxY-35), anchor=tk.CENTER)

        self.quitButton = tk.Button( self, text='EXIT',
                                    font=('Ariel', 20),
                                    command=self.destroy)
        self.quitButton.place(x=int(self.maxX/2), y=int(self.maxY-35), anchor=tk.CENTER)

        wordSize=15
        x=100
        self.enVar = tk.StringVar()
        self.en = tk.Entry(
            self, 
            textvariable=self.enVar, 
            font=('Ariel", 35'),  
            width=wordSize, 
            background="#D9D9D9",
            relief=tk.FLAT,
            justify=tk.RIGHT,
        )
        self.en.place(x=15, y=40, anchor=tk.W)

        self.ptVar = tk.StringVar()
        self.pt = tk.Entry(
            self, 
            textvariable=self.ptVar, 
            font=('Ariel", 35'),  
            width=wordSize, 
            background="#D9D9D9",
            relief=tk.FLAT,
        )
        self.pt.place(x=int(self.maxX*0.5 +15), y=40, anchor=tk.W)

        tk.Label(self, text="Eu ",  font=font,).place(x=x, y=int(maxY-maxY*0.75), anchor=tk.E)
        self.euVar = tk.StringVar()
        self.eu = tk.Entry(self, textvariable=self.euVar, font=font,  width=wordSize, background='#A9A9A9')
        self.eu.place(x=x, y=int(maxY-maxY*0.75), anchor=tk.W)

        self.tuVar = tk.StringVar()
        tk.Label(self, text="Tu ", font=font).place(x=x, y=int(maxY-maxY*0.50), anchor=tk.E)
        self.tu = tk.Entry(self, font=font,  textvariable=self.tuVar, width=wordSize, background='#A9A9A9')
        self.tu.place(x=x, y=int(maxY-maxY*0.50), anchor=tk.W)

        self.eleVar = tk.StringVar()
        tk.Label(self, text="Ele ",font=font).place(x=x, y=int(maxY-maxY*0.25), anchor=tk.E)
        self.ele = tk.Entry(self, textvariable=self.eleVar, font=font,  width=wordSize, background='#A9A9A9')
        self.ele.place(x=x, y=int(maxY-maxY*0.25), anchor=tk.W)

        x=int(maxX*0.50)

        self.nósVar = tk.StringVar()
        tk.Label(self, text="Nós ",font=font).place(x=x, y=int(maxY-maxY*0.75), anchor=tk.E)
        self.nós = tk.Entry(self, textvariable=self.nósVar, font=font,  width=wordSize, background='#A9A9A9')
        self.nós.place(x=x, y=int(maxY-maxY*0.75), anchor=tk.W)

        self.elesVar = tk.StringVar()
        tk.Label(self, text="Eles ",font=font).place(x=x, y=int(maxY-maxY*0.25), anchor=tk.E)
        self.eles = tk.Entry(self, textvariable=self.elesVar, font=font,  width=wordSize, background='#A9A9A9')
        self.eles.place(x=x, y=int(maxY-maxY*0.25), anchor=tk.W)

        self.setVerbs(0)

    def setVerbs(self,i):
        if i >= 0 and i < len(self.verbs):
            self.enVar.set(self.verbs[i].English)
            self.ptVar.set(self.verbs[i].Portuguese)
            self.euVar.set(self.verbs[i].present.eu)
            self.tuVar.set(self.verbs[i].present.tu)
            self.nósVar.set(self.verbs[i].present.nós)
            self.eleVar.set(self.verbs[i].present.ele)
            self.elesVar.set(self.verbs[i].present.eles)
            self.v = i
            


if __name__ == "__main__":
    vw = VerbWindow(verbs)
    vw.mainloop()
