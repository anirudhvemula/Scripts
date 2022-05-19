//
//  main.swift
//  WiFiHibernator
//
//  Created by Sri Nihira on 19/03/21.
//  Copyright © 2021 Sri Group. All rights reserved.
//

// PSEUDOCODE
// While(WiFi=true)
// {
//      Sleep(2)
// }
// Shutdown for Safety!





/*
 
 import SystemConfiguration
 
 public class Reachability {
 
 class func isConnectedToNetwork() -> Bool {
 
 var zeroAddress = sockaddr_in(sin_len: 0, sin_family: 0, sin_port: 0, sin_addr: in_addr(s_addr: 0), sin_zero: (0, 0, 0, 0, 0, 0, 0, 0))
 zeroAddress.sin_len = UInt8(MemoryLayout.size(ofValue: zeroAddress))
 zeroAddress.sin_family = sa_family_t(AF_INET)
 
 let defaultRouteReachability = withUnsafePointer(to: &zeroAddress) {
 $0.withMemoryRebound(to: sockaddr.self, capacity: 1) {zeroSockAddress in
 SCNetworkReachabilityCreateWithAddress(nil, zeroSockAddress)
 }
 }
 
 var flags: SCNetworkReachabilityFlags = SCNetworkReachabilityFlags(rawValue: 0)
 if SCNetworkReachabilityGetFlags(defaultRouteReachability!, &flags) == false {
 return false
 }
 
 /* Only Working for WIFI
 let isReachable = flags == .reachable
 let needsConnection = flags == .connectionRequired
 
 return isReachable && !needsConnection
 */
 
 // Working for Cellular and WIFI
 let isReachable = (flags.rawValue & UInt32(kSCNetworkFlagsReachable)) != 0
 let needsConnection = (flags.rawValue & UInt32(kSCNetworkFlagsConnectionRequired)) != 0
 let ret = (isReachable && !needsConnection)
 
 return ret
 
 }
 }
 Usage:
 
 if Reachability.isConnectedToNetwork(){
 print("Internet Connection Available!")
 }else{
 print("Internet Connection not Available!")
 }
 
 */








import Foundation
import Cocoa
import SystemConfiguration

public class Reachability {
    
    class func isConnectedToNetwork() -> Bool {
        
        var zeroAddress = sockaddr_in(sin_len: 0, sin_family: 0, sin_port: 0, sin_addr: in_addr(s_addr: 0), sin_zero: (0, 0, 0, 0, 0, 0, 0, 0))
        zeroAddress.sin_len = UInt8(MemoryLayout.size(ofValue: zeroAddress))
        zeroAddress.sin_family = sa_family_t(AF_INET)
        
        let defaultRouteReachability = withUnsafePointer(to: &zeroAddress) {
            $0.withMemoryRebound(to: sockaddr.self, capacity: 1) {zeroSockAddress in
                SCNetworkReachabilityCreateWithAddress(nil, zeroSockAddress)
            }
        }
        
        var flags: SCNetworkReachabilityFlags = SCNetworkReachabilityFlags(rawValue: 0)
        if SCNetworkReachabilityGetFlags(defaultRouteReachability!, &flags) == false {
            return false
        }
        
        let isReachable = flags == .reachable
        let needsConnection = flags == .connectionRequired
        
        return isReachable && !needsConnection
    }
}


print("Monitoring Network Status (electricity outage) for Safe Shutdown")

while Reachability.isConnectedToNetwork()
{
    sleep(2)
    print(".")
}

print("Goodbye!")
print("Safe Shutdown Initiated Successfully!!!")

let source = "tell application \"Finder\"\nshut down\nend tell"
let script = NSAppleScript(source: source)
script?.executeAndReturnError(nil)

 
