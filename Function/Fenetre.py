#Penguin_Per_Mil
#      _.._                   
#              .-'    `-.                
#             :          ;               
#             ; ,_    _, ;               
#             : \{"  "}/ :               
#            ,'.'"=..=''.'.              
#           ; / \      / \ ;             
#         .' ;   '.__.'   ; '.           
#      .-' .'              '. '-.        
#    .'   ;                  ;   '.      
#   /    /                    \    \     
#  ;    ;                      ;    ;    
#  ;   `-._                  _.-'   ;    
#   ;      ""--.        .--""      ;     
#    '.    _    ;      ;    _    .'      
#    {""..' '._.-.    .-._.' '..""}      
#     \           ;  ;           /       
#      :         :    :         :        
#      :         :.__.:         :        
#       \       /"-..-"\       /     
#        '-.__.'        '.__.-'  

from tkinter import *
import tkinter as tk
import math

table_of_player_name=[]
Current_player_string="default"
actif_player=-1
Score_table=[]
Score_Text=[]
def Generate_Window(nb_player=2):

    global actif_player

    for i in range(0,nb_player):
        Score_table.append(301)

    #Generation of the main window
    main_window = tk.Tk()
    main_window.geometry("720x480")
    main_window.title("Compteur pour fléchettes")
    e=[]
    label=[]
    Score_1_value=StringVar()
    Score_2_value=StringVar()
    Score_3_value=StringVar()
    Score_1_value.set("0")
    Score_2_value.set("0")
    Score_3_value.set("0")

    def Update_Score():
        global actif_player

        Score_calc=int(Score_1_value.get())+int(Score_2_value.get())+int(Score_3_value.get())
        Score_table[actif_player]=Score_table[actif_player]-Score_calc
        
        if Score_table[actif_player]<0:
            Score_table[actif_player]=Score_table[actif_player]+Score_calc
            Commentaire.delete("1.0",END)
            Commentaire.insert(INSERT,"BUUUUURNNN !!!")
        elif Score_table[actif_player]==0:
            Commentaire.delete("1.0",END)
            Commentaire.insert(INSERT,"Victory !!! " + table_of_player_name[actif_player].get())
        else:
            Commentaire.delete("1.0",END)

        Score_1_value.set("0")
        Score_2_value.set("0")
        Score_3_value.set("0")
        Score_Text[actif_player].delete("1.0",END)
        Score_Text[actif_player].insert(INSERT,str(Score_table[actif_player]))

        actif_player=(actif_player+1)%nb_player
        Current_player_string=table_of_player_name[actif_player].get()

        Current_player_display.delete("1.0",END)
        Current_player_display.insert(INSERT,Current_player_string)

    for i in range(0,nb_player):
        table_of_player_name.append(StringVar())
        label.append(tk.Label(main_window, text='Joueur ' + str(i)))
        label[i].grid(row=i)
        e.append(tk.Entry(main_window,textvariable=table_of_player_name[i]))
        e[i].grid(row=i,column=1)
        Score_Text.append(tk.Text(main_window,width=20,height=1))
        Score_Text[i].grid(row=i,column=3)
        Score_Text[i].insert(INSERT,"301")


    Calcul_button=tk.Button(main_window,text='Calcul',command=Update_Score)
    Calcul_button.grid(row=nb_player+3,column=3)
    
    Current_player_label=tk.Label(main_window,text='Joueur courant:')
    Current_player_label.grid(row=nb_player+2,column=0)
    
    Current_player_display=tk.Text(main_window,width=20,height=1)
    Current_player_display.grid(row=nb_player+2,column=1)

    Score_1_label=tk.Label(main_window,text='Score 1')
    Score_2_label=tk.Label(main_window,text='Score 2')
    Score_3_label=tk.Label(main_window,text='Score 3')
    Score_1_label.grid(row=nb_player+1,column=2)
    Score_2_label.grid(row=nb_player+1,column=3)
    Score_3_label.grid(row=nb_player+1,column=4)

    Score_1_Entry=tk.Entry(main_window,textvariable=Score_1_value)
    Score_2_Entry=tk.Entry(main_window,textvariable=Score_2_value)
    Score_3_Entry=tk.Entry(main_window,textvariable=Score_3_value)
    Score_1_Entry.grid(row=nb_player+2,column=2)
    Score_2_Entry.grid(row=nb_player+2,column=3)
    Score_3_Entry.grid(row=nb_player+2,column=4)

    Commentaire=tk.Text(main_window,width=50,height=3)
    Commentaire.grid(row = nb_player+4,column=1)

    main_window.mainloop()    

