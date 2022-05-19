Imports System
Imports System.Runtime
Imports System.Runtime.InteropServices
Imports System.Net
Imports System.Threading

Public Class SysProtect
    <DllImport("wininet.dll")>
    Private Shared Function InternetGetConnectedState(ByRef Description As Integer, ByVal ReservedValue As Integer) As Boolean
    End Function

    Public Shared Function Method1() 'First and fastest way to determine Internet Connection
        Dim ConnDesc As Integer
        Dim counter As Integer
        counter = 0
        Console.WriteLine("Verifying WiFi Connection Status for Electricity Outage...")
        While InternetGetConnectedState(ConnDesc, 0)
            If counter = 5 Then
                Console.WriteLine(vbCrLf & "Verifying WiFi Connection Status for Electricity Outage...")
                counter = 0
            Else
                counter = counter + 1
                Console.WriteLine(vbCrLf & "* ok *")
            End If
            Thread.Sleep(2000)
        End While

        Console.WriteLine("Wi-Fi disconnected. System hibernating to save work!")
        System.Diagnostics.Process.Start("ShutDown", "/h")
    End Function
End Class

Module Program
    Sub Main(args As String())
        SysProtect.Method1()
    End Sub
End Module