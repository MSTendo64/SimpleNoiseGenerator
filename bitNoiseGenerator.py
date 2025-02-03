import random as rand
from PIL import Image, ImageDraw, ImageFilter

class SimpleNoiseGenerator():

    def Generate(self, sizeOfData = 256):
        byteData = {}
        sizeOfData = int(sizeOfData)
        for i in range(sizeOfData):
            byteData[i] = rand.randint(0, 1)
        return byteData
    
    def CreateImage(self, byteData = Generate(256), imageSize = 16):
        sizeOfData = len(byteData)
        sizeOfData = int(sizeOfData)
        imageSize = int(imageSize)
        #print(f"Size: {sizeOfData}")
        image = Image.new("RGBA", (imageSize, imageSize), (255,255,255,255))
        draw = ImageDraw.Draw(image)
        x = 0
        y = 0
        for i in range(sizeOfData):

            if byteData[i]==1:
                draw.point([x,y], fill="black")

            if not x == imageSize-1:
                #print(byteData[i], end=' ')
                x += 1

            else:
                x = 0
                #print(byteData[i])
                y+=1

        return image

if __name__ == "__main__":
    nGener = SimpleNoiseGenerator()
    image = nGener.CreateImage(nGener.Generate(256/2), 16/2)
    #image.resize([1024, 1024]).save("test.png", "PNG")
    image.resize([1024, 1024]).show()
 
    
