from app_main import *
import global_share as gs
import app_ai_core as AI

def confirm_event():
    #Clear all consoles
    clear_console(gs.ai_console_left)
    clear_console(gs.ai_console_middle)
    clear_console(gs.ai_console_right)
    #clear_console(gs.msg_console)
    a,b,c = 0,0,0
    #When confirm button is pressed
    confirm_flag = True
    #start progress bar to be 0%
    progress_bar_update(gs.bar,0)
 
    #Read user input
    if(len(gs.current_entry.get()) == 0):
        a = 0
    else:
        a = gs.current_entry.get()
    if(len(gs.speed_entry.get()) == 0):
        b = 0
    else:
        b = gs.speed_entry.get()    
    if(len(gs.flow_rate_entry.get()) == 0):
        c = 0
    else:
        c = gs.flow_rate_entry.get()
    
    #Starts AI core
    gs.AI_current = a
    gs.AI_speed = b
    gs.AI_flow = c

    AI_anaylze = False

    print(gs.AI_flow)
    
    #AI analyze
    gs.AI_input_vector,gs.AI_total=AI.generate_input_vector(gs.AI_current,gs.AI_speed,gs.AI_flow)
    AI_anaylze,gs.AI_total,gs.AI_score = AI.classification(gs.AI_input_vector,gs.AI_total)
    if(AI_anaylze == True):
        #Finding optimal parameters
        AI.optimization(gs.AI_score,gs.AI_total)  

