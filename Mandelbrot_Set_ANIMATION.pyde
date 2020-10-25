maxval = 1.9
minval = -maxval
#minval = -0.45

def setup():
    size(1920,1080)
    pixelDensity(1)
   
def draw():
    res = 100
    
    drawSet(res)
    save("Mandelbrot-resolution-{}.png".format(res))
        

def drawSet(resolution):

    maxiterations = resolution
    loadPixels()
    
    for x in range(0, width):
        for y in range(0,height):
            
            a = map(x-400, 0, width, minval, maxval)
            b = map(y+450, 0, width, maxval, minval)
            
            ca = a
            cb = b
            n = 0
            z = 0
            
            while n < maxiterations:
                
                aa = a*a - b*b
                bb = 2 * a * b
                
                a = aa + ca
                b = bb + cb
                
                #print(abs(a + b), "                                     {}                                                 ".format(n))
                
                if abs(a + b) > 16:
                    break
                
                n += 1
                
                # Colorizações diferentes
                acender = map(n, 0, maxiterations, 0, resolution+200)
                #acender = (n * 16) % 255
                #acender = 200
                
                if n == maxiterations:
                    acender = 0
            
            pix = (x + y * width)
            
            pixels[pix] = color(acender)
        
    updatePixels()
