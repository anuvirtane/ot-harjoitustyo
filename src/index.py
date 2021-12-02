from tkinter import Tk, Button, Label, Entry
from ingredientanalyser.ingredientanalyser import IngredientAnalyser
from recipereader.recipereader import RecipeReader
from filesplitter.filesplitter import FileSplitter


def main():
    # window = Tk()
    # window.title('Ruokatilauksen laskija')

    # btn = Button(window, text="Tämä nappi ei tee vielä mitään", fg='blue')
    # btn.place(x=80, y=100)
    # lbl = Label(window, text="Ohjelma toimii komentorivillä", fg='red', font=("Helvetica", 16))
    # lbl.place(x=60, y=50)
    # txtfld = Entry(window, text="Terveisesi eivät lähde mihinkään tästä", bd=5)
    # txtfld.place(x=80, y=150)
    # window.geometry("300x200+10+10")

    # window.mainloop()
    # recipereader = RecipeReader("files/Day0.txt")
    # recipereader.read()
    fs = FileSplitter("files/Day1.txt")
    fs.read()

    #TÄSSÄ SE TOIMIVA ENNEN 2.12.
    # ingredientanalyser = IngredientAnalyser()
    # ingredientanalyser.save_ingredients("files/Day0.txt")



if __name__ == '__main__':
    main()
