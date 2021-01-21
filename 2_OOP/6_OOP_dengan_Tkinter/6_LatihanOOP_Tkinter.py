#ternyata Tkinter juga pake paradigma OOP

import tkinter

main_window = tkinter.Tk() #bikin objek di class tk

def ditekan1():
    label3 = tkinter.Label(main_window, text = 'aku ditekan')
    label3.pack()

def ditekan2():
    label4 = tkinter.Label(main_window, text = 'aku juga ditekan')
    label4.pack()





label1 = tkinter.Label(main_window, text = 'label1') #bikin objek di class label
label2 = tkinter.Label(main_window, text = 'label2') #bikin objek
tombol1 = tkinter.Button(main_window, text = 'tombol1', command = ditekan1)
tombol2 = tkinter.Button(main_window, text = 'tombol2', command = ditekan2)



#method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

#method untuk menampilkan GUI
main_window.mainloop()


'''bisa dilihat perbedaan penulisan CLASS dan METHOD
class huruf pertamanya selalu gede
method / fungsi bebas
'''