import CoreBluetooth
import objc

btm = objc.ivar()
btm = CoreBluetooth.CBCentralManager.alloc().init()

p = btm.scanForPeripherals()

print(p)