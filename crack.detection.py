from tkinter import *
import tkinter.messagebox as box
"""
def openfile():
    openfilenode=True
    from time import strftime 
    dia = Tk()
    dia.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    fname=dia.filename
    for i in open(fname):
        lenth,width,intensity,density,b=i.split()
        print(guied(detect(lenth,width,intensity,density,b),intensity,density))
"""

reasons={
    "Alligator":    "Reasons :\n\t 1- Decrease in pavement load supporting characteristics \n\t 2- Poor or weak subgrade, base or surface \n\t 3- Inadequate drainage systems",
    "Edge":         "Reasons :\n\t 1- Lack of lateral support \n\t 2- Settlement of underlying material \n\t 3- Shrinkage of drying out soil",
    "Slippage":     "Reasons :\n\t 1- Lack of a good bond between surface layer and the course beneath \n\t 2- Lack of bond due to dust, oil, dirt, rubber, water and\n\t    other non-adhesive material \n\t 3- Tack coat has not been used \n\t 4- Mixture has a high sand content",
    "Longitudinal": "Reasons :\n\t 1- Spray bar not set at correct height \n\t 2- Nozzle on spray bar not set at the correct angle \n\t 3- Wrong asphalt pump seed \n\t 4- Asphalt too cold \n\t 5- Pump pressure too low",
    "Reflection":   "Reasons :\n\t 1- Verttical or horizontal movement\n\t(Traffic , Temperature , Moisture change)",
    "Block":        "Reasons :\n\t 1- Heat shrinking of asphalt material due to stress and strain"
    }

tips={
    "Alligator" :   "Repair Tips :\n\tRemove all distressed area to a depth of firm\n\tmaterial and replace with the proper asphalt\n\tmix, allowing 25% times depth of patch for\n\tcompaction.",
    "Edge":         "Repair Tips :\n\tImprove drainage. Remove trees, shrubs\n\tetc., close to edge. Fill cracks with asphalt\n\temulsion slurry or emulsified asphalt.",
    "Slippage":     "Repair Tips :\n\tRemove surface layer from around crack \n\tuntil good bond between layers is found.\n\tPatch with plant-mixed asphalt material. Tuck\n\twith an asphalt emulsion.",
    "Longitudinal": "Repair Tips :\n\tRe-seal surface using proper procedure and\n\tadjustment of equipment."

}



    
def openthis():

    def fix(kind,intensity ,density):
        dosz={
            "Alligator":
            {
                "L":
                [
                    "Do nothing",
                    "Adding a layer of asphalt mortar",
                    "Adding a layer of asphalt mortar"],
                "M":
                [
                    "The process of patching deep",
                    "The process of patching deep",
                    "The process of patching deep"],
                "H":
                [
                    "The process of patching deep",
                    "The process of patching deep",
                    "The process of re-constructions"]},
            "Block":
            {
                "L":
                [
                    "Do nothing",
                    "Do nothing",
                    "Do nothing"],
                "M":
                [
                    "The mpbilization of crack",
                    "The mpbilization of crack",
                    "Adding a layer of asphalt mortar"],
                "H":
                [
                    "Adding a layer of asphalt mortar",
                    "Adding a layer of asphalt mortar",
                    "The additional layer of (Thin Asphalt)"]},
            "Edge":
            {
                "L":
                [
                    "Do nothing",
                    "Do nothing",
                    "Do nothing"],
                "M":
                [
                    "The mpbilization of crack",
                    "The process of patching surface",
                    "The process of patching surface"],
                "H":
                [
                    "Maintenance and repair of road shoulders drop or patching deep",
                    "Maintenance and repair of road shoulders drop or patching deep",
                    "Maintenance and repair of road shoulders drop or patching deep"]},
            "Longitudinal":
            {
                "L":
                [
                    "Do nothing",
                    "Do nothing",
                    "Do nothing"],
                "M":
                [
                    "The mpbilization of crack",
                    "The mpbilization of crack",
                    "The mpbilization of crack"],
                "H":
                [
                    "Adding a layer of asphalt mortar",
                    "Adding a layer of asphalt mortar",
                    "The additional layer of (Thin Asphalt)"]} ,
            "Reflection":
            {
                "L":
                [
                    "Do nothing",
                    "The mpbilization of crack",
                    "The mpbilization of crack"],
                "M":
                [
                    "The mpbilization of crack",
                    "The mpbilization of crack",
                    "The mpbilization of crack"],
                "H":
                [
                    "The process of patching surface",
                    "The process of patching surface",
                    "The process of patching surface"]} ,
            "Slippage":
            {
                "L":
                [
                    "Do nothing",
                    "Do nothing",
                    "Do nothing"],
                "M":
                [
                    "The process of patching surface",
                    "The process of patching surface",
                    "The process of patching surface"],
                "H":
                [
                    "The process of patching deep",
                    "The process of patching deep",
                    "The process of patching deep"]}}    
        return "Repair Method : \n \t "+dosz[kind][intensity.get().title()][0 if density.get().title()=="L" else 1 if density.get().title()=="M" else 2]
     
      
       
        

    def detect(lenth,width,intensity,density,b):
        lst=[0,0,0,0,0,0]
        val=round((float(b)/10500)*100)
        if val in range(11):lst[0]="Edge" 
        elif val in range(10,101):
            # Alligator
            if (((intensity in "hH") and (width>1000)) and (lenth>=3000)):lst[1]="Alligator"
            # Block
            if (((intensity in "lL") and (width<=10)) or ((intensity in "Mm") and (width in range(10,76))) or ((intensity in "hH") and (width>75))) and (lenth<3000):lst[2]="Block"         
            # Reflection
            if (((intensity in "lL") and (width in range(0,11))) or ((intensity in "Mm") and (width in range(10,70))) or ((intensity in "hH") and (width>75))):lst[3]="Reflection" 
            # Slippage
            if (((intensity in "lL") and (width<=10)) or ((intensity in "Mm") and (width<=40)) or ((intensity in "hH") and (width>=40))):lst[4]="Slippage" 
            #Longitudinal  
            if (((intensity  in "lL") and (width<=6)) or ((intensity in "Mm") and (width in range(6,20))) or ((intensity in "hH") and (width>=19))) :lst[5]="Longitudinal"
        lst=list(filter(lambda x:x!=0,lst))
        return lst if len(lst)>1 else "".join(lst)

    def openfile():
        openfilenode=True
        from time import strftime
        from tkinter import filedialog
        fname=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
        with open(strftime("%I:%m:%S %d:%M:%Y")+".txt","w") as curf:
            for i in open(fname):
                lenth,width,intensity,density,b=i.split()
                curf.write()

    def windows(lst):
        def msg(tite,txt):
            hi=Tk()
            hi.title(tite)
            hi.resizable(False, False)
            text=Text(hi)
            text.insert(INSERT,txt)
            text.pack()
        if len(lst)>1 and type(lst)==list:
            for i in lst:
                msg(i,fix(i,intensity,density)+"\n\n"+reasons[i]+"\n\n"+(tips[i] if i in tips else ""))
        elif len(lst)>1:
            msg(lst,fix(lst,intensity,density)+"\n\n"+reasons[lst]+"\n\n"+(tips[lst] if lst in tips else ""))
        else:box.askretrycancel("Retry","Crack not detected")


    root = Tk()
    root.resizable(False, False)
    root.title("expert system")
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_command(label="Save", command="donothing")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    lenth=StringVar()
    width=StringVar()
    intensity=StringVar()
    density=StringVar()
    b=StringVar()

    Label(root, text = "Width:").grid(row = 0, column = 0, padx = 10, pady = 10)
    width = Entry(root, textvariable=width ,width = 25, font = ("Arial", 16))
    width.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10)
    
    Label(root, text = "Lengh:").grid(row = 1, column = 0, padx = 10, pady = 10)
    lenth = Entry(root, textvariable=lenth ,width = 25, font = ("Arial", 16))
    lenth.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10)
    
    Label(root, text = "Intensity:").grid(row = 3, column = 0, padx = 10, pady = 10)
    intensity = Entry(root, textvariable=intensity ,width = 25, font = ("Arial", 16))
    intensity.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)

    Label(root, text = "Density:").grid(row = 4, column = 0, padx = 10, pady = 10)
    density = Entry(root, textvariable=density ,width = 25, font = ("Arial", 16))
    density.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10)
    
    Label(root, text = "b:").grid(row = 6, column = 0, padx = 10, pady = 10)
    b = Entry(root, textvariable=b, width = 25, font = ("Arial", 16))
    b.grid(row = 6, column = 1, padx = 10, pady = 10)
    button = Button(root, text = "Submit",command=lambda :windows(detect(float(lenth.get()),float(width.get()),intensity.get(),density.get(),float(b.get()))))
    button.grid(row = 7, column = 1, padx = 10, pady = 10, ipadx = 10, ipady = 5)
    button.configure(background = "#00bfff")

    root.config(menu=menubar)
    root.mainloop()

def secure(string, key="",action="encrypt"):
	chars="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	def gtkey(key, plaintxt, keyd="", counter=0):
		while len(keyd) != len(plaintxt):
			if counter == len(key): counter = 0
			if plaintxt[len(keyd)] == " ": keyd += " "
			keyd += key[counter]
			counter += 1
		return keyd
	do=lambda a,op,b:a+b if op=="+" else a-b
	key,chi= gtkey(key, string),""
	for i in range(len(string)):
		if string[i] in chars:chi+=chars[do(chars.index(string[i]),"+" if action=="encrypt" else "-",chars.index(key[i]))%len(chars)]
		else:chi+=string[i]
	return chi

openthis()