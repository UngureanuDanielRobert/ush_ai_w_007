import numpy as np
import math
import tkinter.filedialog as fdialog
import tkinter.messagebox as messagebox
import os
import PIL
import PIL.Image
#import pyquark

# Ene George

# Definim valori initiale
format_imagini = [".jpeg",".jpg",".png"]

# momentan lucreaza cu numar fix de randuri si coloane text
w = 7   # numar coloane text
h = 9   # numar randuri text
input_size = w * h              # total elemente in text
states = np.zeros((w, h))      # matricea fisierului text
weights = {}    # ponderi pentru fiecare litera
bias = {}   #
threshold = 0   #
LR = 1  # cat de rapid isi schimba ponderile
max_iterations = 10000  # de cate ori rulam prin fisier si antrenam perceptronul

# bipolar - matricea va contine si valori total opuse de cele pozitive

def open_file(file):
    result = np.zeros((w,h))

    if file.endswith(".txt"):
        # daca e text se proceseaza ca text

        # considera randurile din text elemente din vector
        lines = [line.rstrip('\n') for line in open(file)]
        #print(lines)

        # luam indicele pozitie y pentru elemente din lines
        # line sunt randuri luate ca sir de caractere
        for y, line in enumerate(lines):
            # luam indicele pozitie x pentru fiecare sir de caractere
            # ch sunt caracterele de pe rand, sirurile devin coloane
            for x, ch in enumerate(line):
                # detecteaza steluta in loc de punct in text si pune 1, altfel zero
                result[x, y] = 1 if ch == '*' else 0
                #print(result[x, y])
        return result
    else:
        for e in format_imagini:
            if file.endswith(e):

                # daca e imagine se proceseaza ca imagine
                return result
            else:
                return result   # daca nu e text sau imagine jpg, jpeg, png atunci e zero


def train(input):
    weights = {}   # ponderi
    bias = {}      # tendinta de a scora o litera

    # incepem de la valoarea zero pentru ponderi
    for key in input:
        weights[key] = np.zeros(input_size)
        #print(f"{key} ->",weights[key])
        bias[key] = 0

    # invat perceptronul cu datele din fisier
    trained = False
    for epoch in range(max_iterations):  # epoch - numar de iteratie din maximul dat initial
        trained = True

        for key, samples in input.items():        # trece prin toate literele din fisier
            target = {}                           # init target
            for letter in input:
                # stabileste dupa ce invata daca face parte din litera a, b, c, ..., w, z
                target[letter] = 1 if letter == key else -1
                #print(target)

            for sample_index, sample in enumerate(samples):  # trece prin fisierele date
                for letter, t in target.items():            # verifica pentru toate
                    y_in = bias[letter]                     # bias - valori de a tindere spre litera
                    for i in range(input_size):
                        # produs scalar dintre fisiere date si ponderile alocate
                        y_in += sample[i] * weights[letter][i]

                    if y_in > threshold:
                        # daca tinde spre o litera asignez
                        y = 1
                    elif y_in < -threshold:
                        # daca nu tinde atunci este diferit
                        y = -1
                    else:
                        # daca produsul scalar este 0 atunci nu recunoaste ca litera
                        y = 0
                    if y != t:
                        # face un calcul bazat pe eroare daca nu se potriveste sau este aproape litera data
                        error = t - y
                        bias[letter] = bias[letter] + LR * error
                        for i in range(input_size):
                            # produs scalar dintre ponderi si randurile din fisierul dat cu eroare in calcul
                            weights[letter][i] = weights[letter][i] + LR * sample[i] * error
                        trained = False
        if trained:  # se opreste daca se decide o litera
            break
    return (trained, weights, bias, epoch)

def train_folder():
    global weights, bias
    
    # preia date de invatat
    dir_path = os.getcwd() + '/data/'
    data = {}
    for file in os.listdir(dir_path):
        if file.endswith('.txt'):   # accepta fisiere text
            ch = file[0].upper()
            if not ch in data:
                data[ch] = []
            matrix = open_file(dir_path + file)     # incarc fisier in matrice
            matrix = matrix.reshape(input_size)     # transform matricea in vector/coloana
            #print(matrix)
            matrix[matrix == 0] = -1     # actualizez ca matricea sa aiba determinant -1
            #print(matrix)
            data[ch].append(matrix)      # inserez datele intr-un dictionar

    trained, weights, bias, epoch = train(data)
    print('Rezulatul invatarii: %s, Iteratia: %d'%(trained,epoch))
    return (trained, epoch)

def test(input):
    found = []
    input[input == 0] = -1      # bipolar - matricea va contine si valori total opuse de cele pozitive
    for letter, weight in weights.items():
        y_in = bias[letter]
        for s, w in zip(input, weight):
            y_in += s * w
        if y_in > threshold:
            found.append(letter)
    return found 

def test_folder():
    text = '';
    # preia datele de invatat
    dir_path = os.getcwd() + '/test/'
    for file in os.listdir(dir_path):
        if file.endswith('.txt'):   # pentru fisiere txt
            ch = file[0].upper()
            states = open_file(dir_path + file)
            found = test(states.copy().reshape(input_size))
            
            text += '%s = %s\n' %(file[:-4], ', '.join(found))
    print(text)
    return text
            
# GUI
from tkinter import *
root = Tk()
root.title('Letter Detection')

frame = Frame()
frame.pack(padx=10, pady=10)
#root.geometry("700x550")

toolbar = Frame(frame)
toolbar.pack(fill=X)

# LOAD BUTTON
def load_callback():
    global states
    file = fdialog.askopenfilename()
    if file != '':
        states = open_file(file)
    print_grid()

Button(toolbar, text="Load", command = load_callback).pack(side=LEFT)

# SAVE BUTTON
def save_callback():
    file = fdialog.asksaveasfile(mode='w', defaultextension=".txt")

    for y in range(h):
        for x in range(w):
            file.write('.' if states[x,y] == 0 else '*')
        file.write('\n')
    file.close()

Button(toolbar, text="Save", command = save_callback).pack(side=LEFT)

def clear_callback():
    np.ndarray.fill(states, 0)
    print_grid()

Button(toolbar, text="Clear", command = clear_callback).pack(side=LEFT)
    
Label(toolbar, text='Learning Rate').pack(side=LEFT, padx = 10)
learning_rate_field = Entry(toolbar, textvariable=StringVar(root, value=LR), width=8)
learning_rate_field.pack(side=LEFT)

Label(toolbar, text='Threshold').pack(side=LEFT, padx = 10)
threshold_field = Entry(toolbar, textvariable=StringVar(root, value=threshold), width=8)
threshold_field.pack(side=LEFT)

Label(toolbar, text='Max. Iterations').pack(side=LEFT, padx = 10)
max_iterations_field = Entry(toolbar, textvariable=StringVar(root, value=max_iterations), width=8)
max_iterations_field.pack(side=LEFT)

def train_callback():
    global weights, bias, threshold, LR, max_iterations
    threshold = float(threshold_field.get())
    LR = float(learning_rate_field.get())
    max_iterations = int(max_iterations_field.get())
    trained, epoch = train_folder()
    messagebox.showinfo('Train', 'Training Result: %s, Iterations: %d'%(trained,epoch))
    

Button(toolbar, text="Train", command = train_callback).pack(side=LEFT)
    
def weights_and_bias_callback():
    window = Toplevel(root)
    window.title('Weights & Bias')
    text = Text(window, width=100, height=50)
    weights_value = ''
    for letter, value in weights.items():
        weights_value += '%s\n%s\n' %(letter, value)
    text.insert(END, 'Learning Rate: %s, Threshold: %s,\nWEIGHTS\n%s\nBIAS\n%s' %(LR, threshold, weights_value, bias))
    text.pack()

Button(toolbar, text="Weights & Bias", command = weights_and_bias_callback).pack(side=LEFT)

# CANVAS GRID
def mouseClick(event):
    x = math.floor(event.x / rect_size)
    y = math.floor(event.y / rect_size)
    if x < w and y < h: states[x, y] = 0 if states[x, y] > 0 else 1 # swap zero & one
    print_grid()
    
rect_size = 50  # grid rectangles size
canvas = Canvas(frame, width=rect_size*w, height=rect_size*h)
canvas.bind("<Button-1>", mouseClick)
canvas.pack(fill=X, pady=2)

# DRAW GRID
def print_grid():
    for i in range(w):
        for j in range(h):
            color = 'black' if states[i, j] > 0 else 'white'
            canvas.create_rectangle(i * rect_size, j * rect_size, (i + 1) * rect_size, (j + 1) * rect_size, outline="black", fill=color)
print_grid();

# BOTTOM BAR
bottom_bar = Frame(frame, height=50)
bottom_bar.pack(fill=X)

def test_callback():
    input = states.copy().reshape(input_size)
    found = test(input)
    
    if len(found) > 0:
        test_result_field_value.set(', '.join(found))
    else:
        test_result_field_value.set('???')
    
Button(bottom_bar, text="Test", command = test_callback).pack(side=LEFT)

Label(bottom_bar, text='Result').pack(side=LEFT, padx = 10)
test_result_field_value = StringVar()
test_result_field = Entry(bottom_bar, width=20, textvariable=test_result_field_value)
test_result_field.pack(side=LEFT, padx = 10)

def test_folder_callback():
    result = test_folder()
    window = Toplevel(root)
    window.title('Test Folder')
    text = Text(window, width=20, height=30)
    text.insert(END, result)
    text.pack()
    
Button(bottom_bar, text="Test Folder", command = test_folder_callback).pack(side=LEFT)

root.mainloop()

