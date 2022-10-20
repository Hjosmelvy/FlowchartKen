import wx
import config
from gui import MainGui
class MainGui(wx.Frame):  
  
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        self.panel = wx.Panel(self)     
        self.playerStatus = wx.StaticText(self.panel, id = 1, label ="Old Label.", pos =(150, 100),
                                size = wx.DefaultSize, style = 0)
  
        self.playerLeft = wx.Button(self.panel, id = 2, label="Left", pos = (75,150))
        self.playerLeft.Bind(wx.EVT_BUTTON, lambda event :  self.setPlayerToLeft(event= event))

        self.playerRight = wx.Button(self.panel, id = 3, label="Right", pos = (200,150) )
        self.playerRight.Bind(wx.EVT_BUTTON, lambda event : self.setPlayerToRight(event = event))
        # NEW LABEL
        self.playerStatus.SetLabelText("TEST")
  
        self.SetSize((350, 250))
        self.SetTitle('wx.Button')
        self.Show()

    def updatePlayerPosGui(self):
        self.playerStatus.SetLabel("Right" if config.player1.isRightSide else "Left")
    def setPlayerToLeft(self,event):
        self.updatePosition(False)
        self.updatePlayerPosGui()

    def setPlayerToRight(self,event):
        self.updatePosition(True)
        self.updatePlayerPosGui()


    @staticmethod
    def updatePosition(isRight : bool):
        if isRight:
            if config.player1.midpoint[0] < config.player2.midpoint[0]:
                temp = config.player2
                config.player1 = config.player2
                config.player2 = temp
        else: #player is supposed to be on the left side
            if config.player1.midpoint[0] > config.player2.midpoint[0]:
                temp = config.player2
                config.player1 = config.player2
                config.player2 = temp

if __name__ == '__main__':
    app = wx.App()
    frame = MainGui()
    app.MainLoop()



# import wx
# import config
# from gui import MainGui
# class MyFrame(wx.Frame):  
  
#     def __init__(self):
#         super().__init__(parent=None, title='Hello World')
#         self.panel = wx.Panel(self)     
#         self.playerStatus = wx.StaticText(self.panel, id = 1, label ="Old Label.", pos =(150, 100),
#                                 size = wx.DefaultSize, style = 0)
  
#         self.playerLeft = wx.Button(self.panel, id = 2, label="Left", pos = (75,150))
#         self.playerLeft.Bind(wx.EVT_BUTTON, lambda event :  self.setPlayerToLeft(event= event))

#         self.playerRight = wx.Button(self.panel, id = 3, label="Right", pos = (200,150) )
#         self.playerRight.Bind(wx.EVT_BUTTON, lambda event : self.setPlayerToRight(event = event))
#         # NEW LABEL
#         self.playerStatus.SetLabelText("TEST")
  
#         self.SetSize((350, 250))
#         self.SetTitle('wx.Button')
#         self.Show()

#     def setPlayerToLeft(self, event):
#         print("Working")

#     def setPlayerToRight(self, event):
#         print("Working")


# if __name__ == '__main__':
#     app = wx.App()
#     frame = MyFrame()
#     app.MainLoop()
