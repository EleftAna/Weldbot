#app parameter details

#main interface
#--------------------------------------------------------------------
app_main_title = 'A.I. MIG Weld Parameters Generator'
app_main_geometry = '500x800'
app_main_background = '#F0F8FF'
#--------------------------------------------------------------------


#header
#--------------------------------------------------------------------
header_style_1 = "Lucida Grande"
header_style_2 = "Helvetica"
header_style_3 = "DejaVu Serif"

app_main_header = 'A.I. MIG Weld Parameters Generator'
app_header_fontstyle = header_style_3
app_header_size = 13
app_header_x = 12
app_header_y = 20
app_header_bg = '#F0F8FF'
app_header_text_color = 'black'
#--------------------------------------------------------------------


#input boundary box canvas
#--------------------------------------------------------------------
input_canvas_w = 310
input_canvas_h = 195
input_canvas_color = '#F0F8FF'
input_canvas_thick = 0
input_canvas_highlight = 0
input_canvas_x = 20
input_canvas_y = 60

input_zone_label = "Weld Parameter Input"
input_label_x = 20
input_label_y = 10
input_label_text_color = 'yellow'

#Left
line1_xmin, line1_xmax, line1_ymin, line1_ymax = 0,0,0,input_canvas_h-1
#Right
line2_xmin, line2_xmax, line2_ymin, line2_ymax = input_canvas_w-1,input_canvas_w-1,0,input_canvas_h-1
#Top
line3_xmin, line3_xmax, line3_ymin, line3_ymax = 0,input_canvas_w-1,0,0
#Bottom
line4_xmin, line4_xmax, line4_ymin, line4_ymax = 0,input_canvas_w-1,input_canvas_h-1,input_canvas_h-1
#--------------------------------------------------------------------


#input current (input1)
#--------------------------------------------------------------------
input_current_style_1 = "Lucida Grande"
input_current_style_2 = "DejaVu Serif"
app_input1_header = 'Current (A):'
app_input1_fontstyle = input_current_style_2
app_input1_size = 12
#x,y based on canvas
app_input1_x = 50
app_input1_y = 20
app_input1_bg = '#F0F8FF'
app_input1_text_color = 'black'

app_input1_box_w = 8
app_input1_box_x = app_input1_x+190
app_input1_box_y = app_input1_y
app_input1_box_bg = app_input1_bg
app_input1_box_fg = 'black'
#--------------------------------------------------------------------

#current speed (input2)
#--------------------------------------------------------------------
current_speed_style_1 = "Lucida Grande"
current_speed_style_2 = "DejaVu Serif"

app_input2_header = 'Speed (In/min):'
app_input2_fontstyle = current_speed_style_2
app_input2_size = 12
#x,y based on canvas
app_input2_x = 50
app_input2_y = 60
app_input2_bg = '#F0F8FF'
app_input2_text_color = 'black'
app_input2_box_w = 8
app_input2_box_x = app_input2_x+190
app_input2_box_y = app_input2_y
app_input2_box_bg = app_input2_bg
app_input2_box_fg = 'black'
#--------------------------------------------------------------------


#flow rate (input3)
#--------------------------------------------------------------------
flow_rate_style_1 = "Lucida Grande"
flow_rate_style_2 = "DejaVu Serif"
app_input3_header = 'Flow Rate (l/min):'
app_input3_fontstyle = current_speed_style_2
app_input3_size = 12
#x,y based on canvas
app_input3_x = 50
app_input3_y = 100
app_input3_bg = '#F0F8FF'
app_input3_text_color = 'black'
app_input3_box_w = 8
app_input3_box_x = app_input3_x+190
app_input3_box_y = app_input3_y
app_input3_box_bg = app_input3_bg
app_input3_box_fg = 'black'
#--------------------------------------------------------------------


#control boundary box canvas
#--------------------------------------------------------------------
crtl_canvas_w = 310
crtl_canvas_h = 300
crtl_canvas_color = '#F0F8FF'
crtl_canvas_thick = 0
crtl_canvas_highlight = 0
crtl_canvas_x = 20
crtl_canvas_y = 240

crtl_zone_label = " "
#based on message canvas
crtl_label_x = 20
crtl_label_y = 10
crtl_label_text_color = 'yellow'
crtl_hardware_label = " "
crtl_hardware_label_size = 9
crtl_hardware_label_x = 20
crtl_hardware_label_y = 190
crtl_hardware_label_color = "PaleTurquoise1"



#confirm button
crtl_but_text_size = 10
crtl_but_conf_text = 'Start'
crtl_but_conf_x = 20
crtl_but_conf_y = 5
crtl_but_conf_bg = 'cyan4'
crlt_but_conf_color = 'white'
crtl_but_conf_width = 8

#output boundary box canvas
#--------------------------------------------------------------------
out_canvas_w = 300
out_canvas_h = 200
out_canvas_color = '#F0F8FF'
out_canvas_thick = 0
out_canvas_highlight = 0
out_canvas_x = 20
out_canvas_y = 450

out_zone_label = "A.I. Output Propositions"
#based on message canvas
out_label_x = 80
out_label_y = 12
out_label_text_color = 'black'

#progress bar
#--------------------------------------------------------------------
bar_text_fontstyle = "DejaVu Serif"
bar_text = "Calculation Progress"
bar_text_font_size = crtl_hardware_label_size
bar_text_color = 'black'
bar_text_x = 80
bar_text_y = 70
bar_x = 80
bar_y = 100
bar_length = 250
#--------------------------------------------------------------------


#ai output console terminal
#--------------------------------------------------------------------
#Console_left
app_ai_console_l_fontstyle = "DejaVu Serif"
app_ai_console_l_fontsize = 11
app_ai_console_l_background = '#F0F8FF'
app_ai_console_l_foreground = 'black'
text_ai_box_w_l = 18
text_ai_box_h_l = 1
text_ai_box_x_l = 80
text_ai_box_y_l = 40

#Console_middle
app_ai_console_m_fontstyle = "DejaVu Serif"
app_ai_console_m_fontsize = 10
app_ai_console_m_background = '#F0F8FF'
app_ai_console_m_foreground = 'black'
text_ai_box_w_m = 18
text_ai_box_h_m = 1
text_ai_box_x_m = 80
text_ai_box_y_m = 100

#Console_right
app_ai_console_r_fontstyle = "DejaVu Serif"
app_ai_console_r_fontsize = 11
app_ai_console_r_background = '#F0F8FF'
app_ai_console_r_foreground = 'black'
text_ai_box_w_r = 18
text_ai_box_h_r = 1
text_ai_box_x_r = 80
text_ai_box_y_r = 160

#-------------------------------------------------------------------
