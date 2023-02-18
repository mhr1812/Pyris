# import wx
# import wikipedia
# import wolframalpha

# class MyFrame(wx.Frame):
#     def __init__(self) -> None:
#         wx.Frame.__init__(self,None,pos=wx.DefaultPostion,size=wx.Size(450,100),style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,title="Pyris")
#         panel = wx.Panel(self)
#         my_sizer = wx.BoxSizer(wx.VERTICAL)
#         lbl = wx.StaticText(panel,label="Hello I am Pyris, the Python Virtual Digital Assistant. How can I help you?")
#         my_sizer.Add(lbl,0,wx.ALL,5)
#         self.txt = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(400,30))
#         self.txt.SetFocus()
#         self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
#         my_sizer.Add(self.txt,0,wx.ALL,5)
#         panel.SetSizer(my_sizer)
#         self.Show()

# def OnEnter(self,event):
#     inp = self.txt.GetValue()
#     inp = inp.lower()
#     try:
#         app_id = "K43XWG-9Q5JHVYQ86"
#         client = wolframalpha.Client(app_id)
#         res = client.query(inp)
#         answer = next(res.results).text 
#         print(answer)
#     except:
#         print(wikipedia.summary(inp))

# if __name__=="__main__":
#     app = wx.App(True)
#     frame = MyFrame()
#     app.MainLoop()

import wolframalpha
app_id = "K43XWG-9Q5JHVYQ86"
client = wolframalpha.Client(app_id)

import wikipedia

import PySimpleGUI as sg
sg.theme('DarkBlack')
layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('Pyris', layout)

import pyttsx3
engine = pyttsx3.init()

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (values[0])