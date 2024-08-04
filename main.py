import VerbWindow
import verbs


if __name__ == "__main__":
    v = verbs.loadVerbs()
    vw = VerbWindow.VerbWindow(v)
    vw.mainloop()
    
