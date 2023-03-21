ingreso_mensual = 70000
gasto_mensual = 65000

# if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print('estas en defict')
    elif ingreso_mensual - gasto_mensual > 3000:
        print('estas bien')
    else:
        print('gastas una banda, hay que ver si te alcanza ')
    
elif ingreso_mensual > 1000:
    print('estas bien en latam')
    
elif ingreso_mensual > 500:
    print('estas bien en arg')
    
elif ingreso_mensual > 200:
    print('estas bien en venezuela')

else:
    print('sos pobre')        
    