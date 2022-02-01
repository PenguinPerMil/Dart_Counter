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



from Function import Fenetre

nb_players=Fenetre.Generate_Nb_Player_Window()

tab_players_name=Fenetre.Generate_Name_player_window(nb_players)
#nb_players=4

Fenetre.Generate_Main_Window(tab_players_name,nb_players)