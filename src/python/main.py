# from tkinter import Tks
import customtkinter as ctk

def converter():
    encoded = ''
    text = entry.get()
    
    for ch in entry.get():
        encoded = f'{encoded}&#{ord(ch)};'
    
    app.clipboard_clear()
    app.clipboard_append(encoded)
    
    entry.delete(0, ctk.END)

def paste(event):
    text = app.clipboard_get()
    if text:
        entry.insert(0, text)

def btn_togle(*args):
    if entry_text.get():
        button.configure(state='normal')
    else:
        button.configure(state='disabled')

if __name__ == '__main__':
    
    ctk.set_appearance_mode('dark')
    # ctk.set_default_color_theme('green')
        
    app = ctk.CTk()
    app.title('GFY, dir.bg!')
    
    app.bind('<Return>', converter)
    
    entry_text = ctk.StringVar()
    
    main = ctk.CTkFrame(master=app,
                        bg_color='transparent'
                        )
    main.pack(padx=20, pady=20, fill='both')
    
    entry = ctk.CTkEntry(master=main,
                         width=480,
                         height=50,
                         font=('Arial', 28),
                         textvariable=entry_text
                         )
    entry.pack(pady=5, fill='both')
    entry.focus()
    
    entry.bind('<Button-3>', paste)

    button = ctk.CTkButton(master=main,
                           width=480,
                           height=50,
                           text='Encode and Copy',
                           font=('Arial', 28),
                           anchor='center',
                           command=converter,
                           state='disabled'
                           )
    button.pack(pady=5, fill='both')
    
    entry_text.trace_add('write', btn_togle)
    

    app.mainloop()