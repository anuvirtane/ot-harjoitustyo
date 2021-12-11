from tkinter import Tk, Button, Label, Entry
from ordermaker.ordermaker import OrderMaker
from recipereader.recipereader import RecipeReader

from docx import Document


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
    print("This is a temporary text based user interface without error handling")
    print("For how many people do you wish to make a food order? (type an integer and press enter)")
    answer = int(input())
    print('\nThanks, here is a simple list\n')
    ordermaker = OrderMaker(answer)
    for i in range(0, 11):

        recipereader = RecipeReader(f'files/Day {i} ENG Jan 20.docx')
        recipereader.read()
        ingr_list = recipereader.get_ingredients_list()
        ordermaker.add_ingredients(ingr_list)
    
    ordermaker.print()
    

if __name__ == '__main__':
    main()
