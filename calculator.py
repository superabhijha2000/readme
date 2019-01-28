from tkinter import*
def iCalc (source, side):
    storeObj = frame(source, borderwidth=1, bd= 4, bg="powderblue")
    storeObj(side=side,expand=YES, fill = BOTH)
    return storeObj
def button (source, side , text , command = none):
    storeObj = Button(source, text = text , command = command)
    storeObj.pack (side=side, expand = YES , fill = BOTH)
    return storeObj
class app (Frame):
    def _init_(self):
        Frame.init_(self)
        #self.option_add('*Font',arial 20 bold')
        self.pack(expand= YES , fill = BOTH)
        self.master.title('calculator')
        
        display = stringvar()
        entery(self, relif = FLAT 
               textvariable = display , justify = ' right' , bd= 30 ,
               bg= "powder blue" )pack(side = TOP, expand = YES, fill= BOTH)
        for clear But in (["ce"],["c"]):
            erase = icalc(self, TOP)
            for ichar in clearBut:
                button(erase , LEFT, ichar,
                       lambda storeObj = display, q= ichar: storeObjset(" "))
                for Numbut in ("789/", "456*", "123-", "0.+"):
                    Function Num = icalc (self , TOP)
                    for char in NumBUt:
                        button(Function Nun=m, LEFT, Char,
                               lambda storeObj = display , q= char: storeObj.set
                               (storeObj.get() +q))
                        EqualButton = icalc(self ,TOP)
                        for iEquals in "=":
                            if iEquals == '=':
                                btniEquals = button (equals Button, LEFT ,iEquals)
                                btniEquals.bind('<Button Release - 1>',
                                                lambda e, s= self , store Obj = display ' s,calc (storeObj),'+')
                                else:
                                    btniEquals = button(Equals = '%s' % iEquals:storeobj.set(storeobj.get() +s)
                            
               