Scripts to automate safe shutdowns during power outage protection (Python, Apple Swift, Ms Visual Basic)


===== SAFE HIBERNATOR.PY FOR RASPBERRY PI =====


#!/usr/bin/env python

import time
import os
import urllib.request

def connected():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False


IsConnected = True
Counter = 0
print("Verifying Wi-Fi Status for electricity outage...")

while IsConnected :    
        IsConnected = connected()
        if IsConnected:
        # If WiFi is connected, check again in 5 seconds
            time.sleep(5)
            print("\n* ok *")
            Counter += 1
            if Counter == 5:
                Counter = 0
                print("\nVerifying Wi-Fi Status for electricity outage...")
        
        else:
        # Shutdown OS
            IsConnected = False
            print("Internet Disconnected!\nShutting down!!! Good Bye...")
            time.sleep(10)
            os.system("sudo shutdown -h now")


===== SAFE HIBERNATOR.VB FOR WINDOWS 7.0+ =====


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


===== SAFE HIBERNATOR.SWIFT FOR MAC =====


//
//  main.swift
//  WiFiHibernator
//
// PSEUDOCODE
// While(WiFi=true)
// {
//      Sleep(2)
// }
// Shutdown for Safety!
