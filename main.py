import VerbWindow
import verbs


if __name__ == "__main__":
    v = verbs.loadVerbs()
    print(v[0].present.eu)
    vw = VerbWindow.VerbWindow(v)
    vw.mainloop()
    
