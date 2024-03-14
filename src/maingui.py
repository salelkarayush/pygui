import tkinter as tk
from tkinter import ttk
# import lib.logger_d_gui_asset as ls
# import lib.analyse_csv as acv
import sv_ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
# import lib.mne_gui as mg 
import serial 

filename=''
filepath =''
class MainApp:
    def __init__(self, master):
        #setup
        self.master = master
        self.master.title("Map-y")
        self.master.geometry("800x550+500+300")

        #theme
        self.master.tk.call('source', 'Azure/azure.tcl')
        
        self.master.tk.call('set_theme', 'dark')

        def change_theme():
            # NOTE: The theme's real name is azure-<mode>
            if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
                # Set light theme
                root.tk.call("set_theme", "light")
            else:
                # Set dark theme
                root.tk.call("set_theme", "dark")

        # Remember, you have to use ttk widgets

        self.switch = ttk.Checkbutton(self.master,style="Switch.TCheckbutton", command=change_theme)
        self.switch.pack(side=tk.BOTTOM, anchor=tk.SE)
        self.themelabel = ttk.Label(
            self.master,
            text="Theme",
            font=("-size", 10),
        )
        self.themelabel.pack(padx=10,side=tk.BOTTOM, anchor=tk.SE,expand=True)
        # self.master.tk.call('source', 'Sun-Valley/sv.tcl')
        # self.master.tk.call('set_theme', 'dark')
        
        # Create the widgets for the second app
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs with frames and widgets
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Live")
        self.notebook.add(self.tab2, text="Train")

        # self.frame2 = tk.Frame(self, padx=20, pady=30)
        # self.frame2.pack(padx=40, pady=60)

        self.notebook1 = ttk.Notebook(self.tab2)
        self.notebook1.pack(fill=tk.BOTH, expand=True)

        # Create tabs with frames and widgets
        self.tab3 = ttk.Frame(self.notebook1)
        self.tab4 = ttk.Frame(self.notebook1)
        # self.tab3 = ttk.Frame(self.tab2)
        # self.tab4 = ttk.Frame(self.tab2)

        self.notebook1.add(self.tab3, text="Logdata")
        # self.notebook1.add(self.tab4, text="Visualise")

        # self.notebook2=ttk.Frame(self.tab4)
        # self.notebook2.pack(fill=tk.BOTH)
        
        self.tab5 = ttk.Frame(self.notebook1)
        self.tab6 = ttk.Frame(self.notebook1)
        self.label1 = ttk.Label(
            self.tab1,
            text="Mapy AI model",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        # label1 = ttk.Label(self.tab1, text="Mapy AI model")
        self.label1.pack(pady=20)
        # label3.pack()
        liveb=ttk.Button(self.tab1,text="Start Model",style="Accent.TButton",command=self.callmodel)
        liveb.pack(pady=20)
        

        self.progressBar1= ttk.Progressbar(self.tab1, mode='determinate',
                                          maximum=50, length=200, orient= tk.VERTICAL)
        self.progressBar1.pack(padx=20,side = tk.LEFT)
        lpb1 = ttk.Label(self.tab1, text="REST")
        lpb1.pack(padx=0,side=tk.LEFT,expand=False)
        self.progressBar2= ttk.Progressbar(self.tab1, mode='determinate',
                                          maximum=50, length=200, orient= tk.VERTICAL)
        self.progressBar2.pack(padx=20,side = tk.LEFT)
        lpb2 = ttk.Label(self.tab1, text="RSM")
        lpb2.pack(padx=0,side=tk.LEFT,expand=False)
        
        self.progressBar3= ttk.Progressbar(self.tab1, mode='determinate',
                                          maximum=50, length=200, orient= tk.VERTICAL)
        self.progressBar3.pack(padx=20,side = tk.LEFT)
        lpb3 = ttk.Label(self.tab1, text="RFM")
        lpb3.pack(padx=0,side=tk.LEFT,expand=False)
        self.progressBar4= ttk.Progressbar(self.tab1, mode='determinate',
                                          maximum=50, length=200, orient= tk.VERTICAL)
        self.progressBar4.pack(padx=20,side = tk.LEFT)
        lpb4 = ttk.Label(self.tab1, text="LSM")
        lpb4.pack(padx=0,side=tk.LEFT,expand=False)
        
        self.progressBar5= ttk.Progressbar(self.tab1, mode='determinate',
                                          maximum=50, length=200, orient= tk.VERTICAL)
        self.progressBar5.pack(padx=20,side = tk.LEFT)
        lpb5 = ttk.Label(self.tab1, text="LFM")
        lpb5.pack(padx=0,side=tk.LEFT,expand=False)
        self.progressBar6= ttk.Progressbar(self.tab1, mode='determinate',
                                          maximum=50, length=200, orient= tk.VERTICAL)
        self.progressBar6.pack(padx=20,side = tk.LEFT)
        lpb6 = ttk.Label(self.tab1, text="RAND")
        lpb6.pack(padx=0,side=tk.LEFT,expand=False)
        
        
        
        
        self.notebook1.add(self.tab5, text="Basic Visualisation")
        self.notebook1.add(self.tab6, text="Advanced Component Visualisation")

        self.label2 = ttk.Label(
            self.tab3,
            text="Ensure that you have connected the device to comport7",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label2.pack(pady=20)

        self.label3 = ttk.Label(
            self.tab5,
            text="Visualisation of EEG using FFT and PSD with Correlation of Muscle States",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label3.pack(pady=20)

        actual = ttk.Button(self.tab3, text="muscle movement data",style="Accent.TButton", command=self.actual)
        actual.pack(pady=20)

        imaginary = ttk.Button(self.tab3, text="Imaginary data",style="Accent.TButton" ,command=self.imaginary)
        imaginary.pack(pady=20)
        eegpl=ttk.Button(self.tab5,text='Plot eeg signal vs Time',style="Accent.TButton",command=self.eegplot)
        eegpl.pack(pady=10)
        emgpl=ttk.Button(self.tab5,text='Plot eeg signal vs Time with Muscle-states',style="Accent.TButton",command=self.eegemgplot)
        emgpl.pack(pady=10)
        
        fftpl=ttk.Button(self.tab5,text='plot FFT of EEG chx',style="Accent.TButton",command=self.fftplot)
        fftpl.pack(pady=10)
        
        psdpl1=ttk.Button(self.tab5,text='PSD of EEG chx T7',style="Accent.TButton",command=self.psdplotT7)
        psdpl1.pack(pady=10)
        psdpl2=ttk.Button(self.tab5,text='PSD of EEG chx C3',style="Accent.TButton",command=self.psdplotC3)
        psdpl2.pack(pady=10)
        psdpl3=ttk.Button(self.tab5,text='PSD of EEG chx C4',style="Accent.TButton",command=self.psdplotC4)
        psdpl3.pack(pady=10)
        psdpl4=ttk.Button(self.tab5,text='PSD of EEG chx T8',style="Accent.TButton",command=self.psdplotT8)
        psdpl4.pack(pady=10)
        
        
        mne_pl2=ttk.Button(self.tab6,text='ICA PLOT',style="Accent.TButton",command=self.plot_ica)
        mne_pl2.pack(pady=10)
        mne_pl3=ttk.Button(self.tab6,text='epoch plot of Rest movement',style="Accent.TButton",command=self.plot_epochs2)
        mne_pl3.pack(pady=10)
        mne_pl4=ttk.Button(self.tab6,text='epoch plot of Right-Hand slow Movement',style="Accent.TButton",command=self.plot_epochs3)
        mne_pl4.pack(pady=10)
        mne_pl5=ttk.Button(self.tab6,text='epoch plot of Right-Hand fast Movement',style="Accent.TButton",command=self.plot_epochs4)
        mne_pl5.pack(pady=10)
        mne_pl6=ttk.Button(self.tab6,text='epoch plot of Left-Hand slow Movement',style="Accent.TButton",command=self.plot_epochs5)
        mne_pl6.pack(pady=10)
        mne_pl7=ttk.Button(self.tab6,text='epoch plot of Left-Hand fast Movement',style="Accent.TButton",command=self.plot_epochs6)
        mne_pl7.pack(pady=10)
        mne_pl8=ttk.Button(self.tab6,text='epoch plot of Random Hand Movement',style="Accent.TButton",command=self.plot_epochs7)
        mne_pl8.pack(pady=10)
# class Redirect():

#     def __init__(self, widget):
#         self.widget = widget

#     def write(self, text):
#         self.widget.insert('end', text)
    
    def actual(self):
        global filename, filepath
        # filename, filepath = ls.logger_data()
        

    
    def imaginary(self):
        global filename, filepath
        # filename, filepath = ls.logger_data_img()
    
    def eegplot(self):
        global filename,filepath
              
    
        # if filename == '' and filepath == '':
        #     # filename, filepath = acv.pass_file_path(0)
        #     # acv.figure_option_eeg(filename,filepath)
        # #
        # else:
        #     acv.figure_option_eeg(filename,filepath)
        #     plt.show()
            
    
    def eegemgplot(self):
        global filename,filepath
        
        
    
        # if filename == '' and filepath == '':
        #     filename, filepath = acv.pass_file_path(0)
        #     acv.eeg_muscle_plot(filename,filepath)
        # #
        # else:
        #     acv.eeg_muscle_plot(filename,filepath)

    def fftplot(self):
        global filename,filepath
        
        
    
        # if filename == '' and filepath == '':
        #     filename, filepath = acv.pass_file_path(0)
        #     acv.figure_option_fft(filename,filepath)        
        # #
        # else:
        #     acv.figure_option_fft(filename,filepath)
            
            
    def psdplotT7(self):
        global filename,filepath
        
        
    
        # if filename == '' and filepath == '':
        #    filename, filepath =  acv.pass_file_path(0)
        #    acv.figure_option_psdT7(filename,filepath)
        # #
        # else:
        #     acv.figure_option_psdT7(filename,filepath)
            
       
    def psdplotC3(self):
       global filename,filepath
        
        
    
    #    if filename == '' and filepath == '':
    #         filename, filepath = acv.pass_file_path(0)
    #         acv.figure_option_psdC3(filename,filepath)
            
    #     #
    #    else:
    #         acv.figure_option_psdC3(filename,filepath)
             
            
    def psdplotT8(self):
       global filename,filepath
        
        
    
    #    if filename == '' and filepath == '':
    #         filename, filepath = acv.pass_file_path(0)
    #         acv.figure_option_psdT8(filename,filepath)
            
    #     #
    #    else:
    #         acv.figure_option_psdT8(filename,filepath)
              
              
    
    def psdplotC4(self):
       global filename,filepath
        
        
    
    #    if filename == '' and filepath == '':
    #        filename, filepath =  acv.pass_file_path(0)
    #        acv.figure_option_psdC4(filename,filepath)
             
    #     #
    #    else:
    #         acv.figure_option_psdC4(filename,filepath)
    
    def plot_ica(self):
        global filename,filepath
        # if filename == '' and filepath == '':
        #    filename, filepath = mg.ret_filename()
        #    mg.ica_plots(filename)
             
        # #
        # else:
        #     mg.ica_plots(filename)
            
    def plot_epochs(self):
        global filename,filepath
        # if filename == '' and filepath == '':
        #    filename, filepath = mg.ret_filename()
        #    mg.epoch_plots(filename)
             
        # #
        # else:
        #     mg.epoch_plots(filename)
    
    def plot_epochs2(self):
        global filename,filepath
        # if filename == '' and filepath == '':
        #    filename, filepath = mg.ret_filename()
        #    mg.epochp1(filename)
             
        # #
        # else:
        #     mg.epochp1(filename)        

    def plot_epochs3(self):
        global filename,filepath
        # if filename == '' and filepath == '':
        #    filename, filepath = mg.ret_filename()
        #    mg.epochp2(filename)
             
        # #
        # else:
        #     mg.epochp2(filename)        

    def plot_epochs4(self):
        global filename,filepath
        # if filename == '' and filepath == '':
        #    filename, filepath = mg.ret_filename()
        #    mg.epochp3(filename)
             
        # #
        # else:
        #     mg.epochp3(filename)        

    def plot_epochs5(self):
        global filename,filepath
        # if filename == '' and filepath == '':
        #    filename, filepath = mg.ret_filename()
        #    mg.epochp4(filename)
             
        # #
        # else:
        #     mg.epochp4(filename)        


    def plot_epochs6(self):
        global filename,filepath
        # if filename == '' and filepath == '':
        #    filename, filepath = mg.ret_filename()
        #    mg.epochp5(filename)
             
        # #
        # else:
        #     mg.epochp5(filename)        

    def plot_epochs7(self):
        global filename,filepath
        # if filename == '' and filepath == '':
        #    filename, filepath = mg.ret_filename()
        #    mg.epochp6(filename)
             
        # #
        # else:
        #     mg.epochp6(filename)        

    def callmodel(self):
        try:
            serlive=ls.ser
        except AttributeError:
            pass
        while(True):
            try :
                print(str(serlive.readline().decode('utf-8').strip().
                            split(',')).replace("[","").replace("]","").
                            replace("'","").replace(" ",""))
            except UnboundLocalError:
                pass
        return 0


        #     # figure1,figure2,figure3 = acv.get_fft(filename,filepath)
        #     fig1 = acv.figure_option_eeg(filename, filepath)
        #     top_level = tk.Toplevel(self.master)
        #     top_level.title("Matplotlib Plot in Tkinter")
        #
        #     canvas = FigureCanvasTkAgg(fig1, master=top_level)
        #     canvas.draw()
        #     canvas_widget = canvas.get_tk_widget()
        #     canvas_widget.pack(fill=tk.BOTH, expand=True)
        #     plt.show()



#
#         self.notebook.add(self.tab1, text="Tab 1")
#         self.notebook.add(self.tab2, text="Tab 2")
#
#         # self.frame2 = tk.Frame(self, padx=20, pady=30)
#         # self.frame2.pack(padx=40, pady=60)
#         label = ttk.Label(self.tab1, text="This is the second app.")
#         label.pack(pady=20)
#         logdata = ttk.Button(self.tab1, text="Logdata", command=self.logdatafile)
#         logdata.pack(pady=20)
#
#         visualise = ttk.Button(self.tab1, text="Visualise", command=self.visualise)
#         visualise.pack(pady=20)



if __name__ == "__main__":
    root = tk.Tk()

    # Set the theme
    # root.tk.call('source', "D:/matlab/ymaps_code/code/python/azure.tcl")
    # root.tk.call("set_theme", "dark")
    # sv_ttk.set_theme("dark")
    # root.iconbitmap('./scr/mainicon.ico')


    app = MainApp(root)

    # # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    # sv_ttk.set_theme("dark")

    root.mainloop()
 