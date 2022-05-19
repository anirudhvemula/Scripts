VERSION 5.00
Begin VB.Form Form1 
   ClientHeight    =   3650
   ClientLeft      =   50
   ClientTop       =   330
   ClientWidth     =   4610
   LinkTopic       =   "Form1"
   MinButton       =   0   'False
   ScaleHeight     =   3650
   ScaleWidth      =   4610
   StartUpPosition =   2  'CenterScreen
   WindowState     =   2  'Maximized
   Begin VB.Timer Timer1 
      Interval        =   50
      Left            =   1440
      Top             =   1440
   End
   Begin VB.TextBox Text1 
      Height          =   3610
      Left            =   0
      TabIndex        =   0
      Text            =   "Display Off"
      Top             =   0
      Width           =   4570
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Declare Function SetWindowPos Lib "user32" (ByVal hwnd As Long, ByVal hWndInsertAfter As Long, ByVal x As Long, y, ByVal cx As Long, ByVal cy As Long, ByVal wFlags As Long) As Long
Private Const HWND_TOPMOST = -1
Private Const HWND_NOTOPMOST = -2
Private Const SWP_NOMOVE = &H2
Private Const SWP_NOSIZE = &H1
Private Const TOPMOST_FLAGS = SWP_NOMOVE Or SWP_NOSIZE
Public Sub MakeNormal(hwnd As Long)
    SetWindowPos hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, TOPMOST_FLAGS
End Sub
Public Sub MakeTopMost(hwnd As Long)
    SetWindowPos hwnd, HWND_TOPMOST, 0, 0, 0, 0, TOPMOST_FLAGS
End Sub

Private Sub Form_Initialize()
    MakeTopMost Form1.hwnd
    'Text1.SetFocus
End Sub

Private Sub Form_Paint()
    'Do While True
        'Text1.SetFocus
        'Sleep
    'Loop
    
    With Text1
        .Height = 10360
        .Width = 19100
        .SetFocus
    End With
    'Text1.SetFocus
    Shell "F:\doff\doff.exe", vbHide
End Sub

Private Sub Form_QueryUnload(Cancel As Integer, UnloadMode As Integer)
    've
    'MsgBox "test"
    End
End Sub



Private Sub Text1_KeyPress(KeyAscii As Integer)
    MakeTopMost Form1.hwnd
    Timer1.Enabled = True
    
    Do While True
    If KeyAscii = vbKeyDown Then
        'Text1.SetFocus
        SendKeys "{LEFT}"
    ElseIf KeyAscii = vbKeyLeft Then
        
        Exit Do
    End If
    Loop
    Shell "F:\doff\doff.exe", vbHide
    Timer1.Enabled = False
End Sub

Private Sub Timer1_Timer()
    Text1.SetFocus
End Sub
