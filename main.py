'''------------------------------------------------------------ 
1. A paros() nevü függvény True -val térjen vissza ha az argumentum páros. '''
def paros (a):
        if a % 2 == 0:
            return True
        else:
            return False
 

'''------------------------------------------------------------
2. A paratlan() nevü függvény True -val térjen vissza ha az argumentum páratlan. '''
def paratlan (a):
        if a % 2 == 1:
            return True
        else:
            return False
    
'''------------------------------------------------------------
3. A harommal_osztható() nevü függvény True -val térjen vissza ha az argumentum hárommal osztható. '''
def harommal_osztható (a):
        if a % 3 == 0:
            return True
        else:
            return False

'''------------------------------------------------------------
4. kisebb() nevü függvény a két argumentum közül a kisebbikkel térjen vissza.'''
def kisebb(a,b):
        if a < b:
            return a
        elif b < a:
            return b
        elif a == b:
            return a