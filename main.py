from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from PIL import Image, ImageTk


from pathlib import Path


def select_path_and_download():
    """This function allow user to select a path from explorer
    then download Youtube link in chosen path

    Returns:
        .mp4: Audio from youtube link as .mp4
    """
    path = filedialog.askdirectory()

    return YouTube(link_field.get()).streams.get_audio_only().download(path)


def download_from_list():
    """This function allow user to download audio.mp4 from a list of link
    register in text document
    """
    path = filedialog.askopenfilename()
    first_list = []
    with open(path, "r", encoding='utf-8') as f:
        for element in f:
            first_list.append(element.strip())
            filtered_list = list(filter(None, first_list))
        path_to_downdload = filedialog.askdirectory()
        for url in filtered_list:
            print(url)
            YouTube(url).streams.get_audio_only().download(path_to_downdload)


path = Path().cwd()
window = Tk(className="Téléchargement de Musiques")

window.geometry("600x600")
window.minsize(600, 600)

#### WINDOWS VERSION###
# window.iconbitmap(Path(path / r"C:\path_to\.png"))

"""im = Image.open('167(1).png')
photo = ImageTk.PhotoImage(im)
window.wm_iconphoto(True, photo)"""

window.attributes("-alpha", 0.90)

canvas = Canvas(window, width=600, height=600)
canvas.pack()

logo_img = Image.open("167(1).png")
logo_photo = ImageTk.PhotoImage(logo_img)
canvas.create_image(300, 150, image=logo_photo)

##### image logo for windows version####
#logo_img = PhotoImage(file=Path(path / r"C:\path_to\.png"))
# resize
# canvas.create_image(300, 150, image=logo_img,)


# This part set link field
link_label = Label(window, text="Coller l'url Youtube: ctrl + v ",
                   font=("JetBrains Mono", 12))
link_field = Entry(window, width=35, font=("JetBrains Mono", 12))

# Add widgets to window
canvas.create_window(300, 350, window=link_label)
canvas.create_window(300, 380, window=link_field)

# Select Path for saving single file
select_btn = Button(window, text="Choisir un dossier pour Télécharger", bg='#901a01',
                    padx='25', pady='5', font=("JetBrains Mono", 10), fg='#fefefe',
                    command=select_path_and_download, relief=GROOVE)

canvas.create_window(300, 450, window=select_btn)

# Select file to download list of url then select path to save download
select_btn_2 = Button(window, text="Ouvrir une Liste / Choisir un dossier pour "
                      "Télécharger", bg='#901a01', padx='25', pady='5',
                      font=("JetBrains Mono", 10), fg='#fefefe',
                      command=download_from_list, relief=GROOVE)

canvas.create_window(300, 530, window=select_btn_2)

window.mainloop()
