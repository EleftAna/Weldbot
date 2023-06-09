import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import END
import app_info
import app_event
import global_share as gs


#Debug test control
debug_test = False


def clear_console(console):
#   #Clear console contents
    console.delete('1.0',END)

def update_console(console,text,auto_scroll=True):
    console.configure(state='normal')
    console.insert(tk.INSERT,text)
    #auto scrolled
    if(auto_scroll == True):
        console.yview(END) 

def ai_console_output(gui_window):
    fontStyle = tkFont.Font(family=app_info.app_ai_console_l_fontstyle, size=app_info.app_ai_console_l_fontsize)

    #Console (Left)
    console_ai_text_L = scrolledtext.ScrolledText(gui_window, wrap=tk.WORD,\
        width=app_info.text_ai_box_w_l,height=app_info.text_ai_box_h_l,font=fontStyle)

    console_ai_text_L.grid(column=0,pady=10,padx=10)
    console_ai_text_L.configure(state='disabled',background=app_info.app_ai_console_l_background,foreground=app_info.app_ai_console_l_foreground)
    console_ai_text_L.place(x=app_info.text_ai_box_x_l,y=app_info.text_ai_box_y_l)

    #Console (middle)
    console_ai_text_M = scrolledtext.ScrolledText(gui_window, wrap=tk.WORD,\
        width=app_info.text_ai_box_w_m,height=app_info.text_ai_box_h_m,font=fontStyle)

    console_ai_text_M.grid(column=0,pady=10,padx=10)
    console_ai_text_M.configure(state='disabled',background=app_info.app_ai_console_m_background,foreground=app_info.app_ai_console_m_foreground)
    console_ai_text_M.place(x=app_info.text_ai_box_x_m,y=app_info.text_ai_box_y_m)

    #Console (right)
    console_ai_text_R = scrolledtext.ScrolledText(gui_window, wrap=tk.WORD,\
        width=app_info.text_ai_box_w_r,height=app_info.text_ai_box_h_r,font=fontStyle)

    console_ai_text_R.grid(column=0,pady=10,padx=10)
    console_ai_text_R.configure(state='disabled',background=app_info.app_ai_console_r_background,foreground=app_info.app_ai_console_r_foreground)
    console_ai_text_R.place(x=app_info.text_ai_box_x_r,y=app_info.text_ai_box_y_r)
    return console_ai_text_L,console_ai_text_M,console_ai_text_R


def progress_bar_update(indicator,work_done):
    indicator["value"]=work_done


def progress_bar_init(gui_window):
    progress_bar = ttk.Progressbar(gui_window,orient="horizontal",length=app_info.bar_length,mode="determinate")
    progress_bar.place(x=app_info.bar_x,y=app_info.bar_y)
    #Set Initial value and maximum value
    progress_bar["value"] = 0
    progress_bar["maximum"] = 100
    return progress_bar


def console_init(gui_window):
    fontStyle = tkFont.Font(family=app_info.app_console_fontstyle, size=app_info.app_console_fontsize)

    console_text = scrolledtext.ScrolledText(gui_window, wrap=tk.WORD,\
        width=app_info.text_box_w,height=app_info.text_box_h,font=fontStyle)

    console_text.grid(column=0,pady=10,padx=10)
    console_text.configure(state='disabled',background=app_info.app_console_background,\
    foreground=app_info.app_console_foreground)
    console_text.place(x=app_info.text_box_x,y=app_info.text_box_y)

    return console_text


def draw_control_elements(gui_window):
    #confirm button
    fontStyle = tkFont.Font(family=app_info.app_header_fontstyle, size=app_info.crtl_but_text_size)
    confirm_button = tk.Button(gui_window, text=app_info.crtl_but_conf_text, \
        bg=app_info.crtl_but_conf_bg,fg=app_info.crlt_but_conf_color,font=fontStyle,\
        highlightbackground=app_info.input_canvas_color,width=app_info.crtl_but_conf_width, \
        command=app_event.confirm_event)
    confirm_button.place(x=140,y=0)
    
    #Progress:
    fontStyle = tkFont.Font(family=app_info.bar_text_fontstyle, size=app_info.bar_text_font_size)
    progress_label = tk.Label(gui_window, text=app_info.bar_text, font=fontStyle,\
        bg=app_info.app_input1_bg,fg=app_info.bar_text_color)
    progress_label.place(x=app_info.bar_text_x,y=app_info.bar_text_y)


def draw_output_boundary(gui_window):  
    fontStyle = tkFont.Font(family="DejaVu Serif", size=9)
    zone_label = tk.Label(gui_window, text=app_info.out_zone_label, font=fontStyle,\
        bg=app_info.app_input1_bg,fg=app_info.out_label_text_color)
    zone_label.place(x=app_info.out_label_x,y=app_info.out_label_y)  

def input_current_init(gui_window):
    #input parameter 1 = input current
    #Set input parameter 1 label
    fontStyle = tkFont.Font(family=app_info.app_input1_fontstyle, size=app_info.app_input1_size)
    input_current_label = tk.Label(gui_window, text=app_info.app_input1_header, font=fontStyle,\
        bg=app_info.app_input1_bg,fg=app_info.app_input1_text_color)
    input_current_label.place(x=app_info.app_input1_x,y=app_info.app_input1_y)
    
    #Set input parameter 1 input box
    input_current_entry = tk.Entry(gui_window, width=app_info.app_input1_box_w,\
        bg=app_info.app_input1_box_bg,fg=app_info.app_input1_box_fg)
    input_current_entry.place(x=app_info.app_input1_box_x,y=app_info.app_input1_box_y)

    return input_current_label, input_current_entry

def speed_init(gui_window):
    #input parameter 2 = current speed
    fontStyle = tkFont.Font(family=app_info.app_input2_fontstyle, size=app_info.app_input2_size)
    speed_label = tk.Label(gui_window, text=app_info.app_input2_header, font=fontStyle,\
        bg=app_info.app_input2_bg,fg=app_info.app_input2_text_color)
    speed_label.place(x=app_info.app_input2_x,y=app_info.app_input2_y)

    #Set input parameter 2 input box
    speed_entry = tk.Entry(gui_window, width=app_info.app_input2_box_w,\
        bg=app_info.app_input2_box_bg,fg=app_info.app_input2_box_fg)
    speed_entry.place(x=app_info.app_input2_box_x,y=app_info.app_input2_box_y)   
    
    return speed_label,speed_entry 

def flow_rate_init(gui_window):
    #input parameter 3 = flow rate
    fontStyle = tkFont.Font(family=app_info.app_input3_fontstyle, size=app_info.app_input3_size)
    flow_rate_label = tk.Label(gui_window, text=app_info.app_input3_header, font=fontStyle,\
        bg=app_info.app_input3_bg,fg=app_info.app_input3_text_color)
    flow_rate_label.place(x=app_info.app_input3_x,y=app_info.app_input3_y)

    #Set input parameter 3 input box
    flow_rate_entry = tk.Entry(gui_window, width=app_info.app_input3_box_w,\
        bg=app_info.app_input3_box_bg,fg=app_info.app_input3_box_fg)
    flow_rate_entry.place(x=app_info.app_input3_box_x,y=app_info.app_input3_box_y)   

    return flow_rate_label,flow_rate_entry 
     
def main_window_init():
    window = tk.Tk()

    #Set basic window title, size and background color
    window.title(app_info.app_main_title)
    window.geometry(app_info.app_main_geometry)
    window.configure(background=app_info.app_main_background)
    window.iconbitmap(r'1660048337739.ico')
    #Set header
    fontStyle = tkFont.Font(family=app_info.app_header_fontstyle, size=app_info.app_header_size, weight="bold")
    header_label = tk.Label(window, text=app_info.app_main_header, font=fontStyle, \
        bg=app_info.app_header_bg,fg=app_info.app_header_text_color)
    header_label.place(x=app_info.app_header_x,y=app_info.app_header_y)
    return window


def main():
    #Setup root window
    gs.main_window = main_window_init()

    #Setup canvas for input zone
    gs.input_area = tk.Canvas(gs.main_window, width=app_info.input_canvas_w, height=app_info.input_canvas_h,\
        bg = app_info.input_canvas_color, bd = app_info.input_canvas_thick, highlightthickness=app_info.input_canvas_highlight)
    gs.input_area.place(x=app_info.input_canvas_x,y=app_info.input_canvas_y)

    #Setup different input interfaces on input canvas
    current_label, gs.current_entry = input_current_init(gs.input_area)
    speed_label, gs.speed_entry = speed_init(gs.input_area)
    flow_rate_lable, gs.flow_rate_entry = flow_rate_init(gs.input_area)

    #Setup canvas for control
    gs.control_area = tk.Canvas(gs.main_window,width=app_info.crtl_canvas_w, height=app_info.crtl_canvas_h,\
        bg = app_info.crtl_canvas_color, bd = app_info.crtl_canvas_thick, highlightthickness=app_info.crtl_canvas_highlight)
    gs.control_area.place(x=app_info.crtl_canvas_x,y=app_info.crtl_canvas_y)
  
    #Draw control elements
    draw_control_elements(gs.control_area)

    #Setup canvas for output zone
    gs.output_area = tk.Canvas(gs.main_window,width=app_info.out_canvas_w, height=app_info.out_canvas_h,\
        bg = app_info.out_canvas_color, bd = app_info.out_canvas_thick, highlightthickness=app_info.out_canvas_highlight)
    gs.output_area.place(x=app_info.out_canvas_x,y=app_info.out_canvas_y)    

    #Draw output boundary boxes
    draw_output_boundary(gs.output_area)

    #Import progress bar
    gs.bar = progress_bar_init(gs.control_area)

    #Import AI output console
    gs.ai_console_left,gs.ai_console_middle,gs.ai_console_right = ai_console_output(gs.output_area)

    if(debug_test):
        #update progress bar
        progress_bar_update(gs.bar,60)
        #Display text on different consoles
        update_console(gs.msg_console,"msg_console")
        update_console(gs.ai_console_left,"ai_console LEFT")
        update_console(gs.ai_console_middle,"ai_console MIDDLE")
        update_console(gs.ai_console_right,"ai_console Right")
    gs.main_window.mainloop()


if __name__ == "__main__":
    main()