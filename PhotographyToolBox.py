from PIL import Image
#pip install Pillow
from PIL.ExifTags import TAGS
#pip install exifread
import os
print('Photography ToolBox by Deval Parikh')
print('')
print('Choose the following photo options:')
print('')
print('1. Organize collection by format')
print('2. [in development] Organize collection by date')
print('3. Resize photos')
print('4. [in development] Enhance photos (Contrast)')
print('')
userInput = input('Enter "1", "2", "3", "4" (Without quotation): ')
if userInput == "1":
    #makes a copy of the photo into respective diretory based on format
    for f in os.listdir('.'):
        if f.endswith('.png'):
            #f = Image.open('NightSky.png')
            #f.show()
            i = Image.open(f)
            #fn - file name; fext - file extension
            #organizing into folders by fext
            fn, fext = os.path.splitext(f)
            if not os.path.exists('pngs'):
                os.makedirs('pngs')
            #fn is passed in for formatting labels for photos
            i.save('pngs/{}.png'.format(fn))
        elif f.endswith('.gif'):
            #f = Image.open('NightSky.png')
            #f.show()
            i = Image.open(f)
            #fn - file name; fext - file extension
            #organizing into folders by fext
            fn, fext = os.path.splitext(f)
            if not os.path.exists('gifs'):
                os.makedirs('gifs')
            #fn is passed in for formatting labels for photos
            i.save('gifs/{}.gif'.format(fn))
        elif f.endswith('.jpeg'):
            #f = Image.open('NightSky.png')
            #f.show()
            i = Image.open(f)
            #fn - file name; fext - file extension
            #organizing into folders by fext
            fn, fext = os.path.splitext(f)
            if not os.path.exists('jpegs'):
                os.makedirs('jpegs')
            #fn is passed in for formatting labels for photos
            i.save('jpegs/{}.jpeg'.format(fn))
        elif f.endswith('.jpg'):
            #f = Image.open('NightSky.png')
            #f.show()
            i = Image.open(f)
            #fn - file name; fext - file extension
            #organizing into folders by fext
            fn, fext = os.path.splitext(f)
            if not os.path.exists('jpgs'):
                os.makedirs('jpgs')
            #fn is passed in for formatting labels for photos
            i.save('jpgs/{}.jpg'.format(fn))
        elif f.endswith('.psd'):
            #f = Image.open('NightSky.png')
            #f.show()
            i = Image.open(f)
            #fn - file name; fext - file extension
            #organizing into folders by fext
            fn, fext = os.path.splitext(f)
            if not os.path.exists('psds'):
                os.makedirs('psds')
            #fn is passed in for formatting labels for photos
            i.save('psds/{}.psd'.format(fn))
        elif f.endswith('.tiff'):
            #f = Image.open('NightSky.png')
            #f.show()
            i = Image.open(f)
            #fn - file name; fext - file extension
            #organizing into folders by fext
            fn, fext = os.path.splitext(f)
            if not os.path.exists('tiffs'):
                os.makedirs('tiffs')
            #fn is passed in for formatting labels for photos
            i.save('tiffs/{}.tiff'.format(fn))
        elif f.endswith('.img'):
            #f = Image.open('NightSky.png')
            #f.show()
            i = Image.open(f)
            #fn - file name; fext - file extension
            #organizing into folders by fext
            fn, fext = os.path.splitext(f)
            if not os.path.exists('imgs'):
                os.makedirs('imgs')
            #fn is passed in for formatting labels for photos
            i.save('imgs/{}.img'.format(fn))
############################################################################
#                        ADD YOUR OWN FORMATS HERE                         #
############################################################################
elif userInput == "2":
    def get_exif(fn):
        ret = {}
        i = Image.open(fn)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        return ret
    for f in os.listdir('.'):
        if f.endswith('.jpg' or '.png' or '.img' or '.jpeg'):
            get_exif(f)


elif userInput == "3":
    try:
        userWidthInput = int(input("Enter size of width: "))
        userHeightInput = int(input("Enter size of height: "))
    except:
        print("Please input integer values.")
    size = (userWidthInput, userHeightInput)
    if os.path.exists('ResizedPhotos'):
        print("folder already exist.")

    else:
        os.makedirs('ResizedPhotos')
        for f in os.listdir('.'):
            if f.endswith('.jpg' or '.png' or '.img' or '.jpeg'):
                i = Image.open(f)
                fn, fext = os.path.splitext(f)
                i = i.resize(size)
                #Future edits naming update below
                #sizeText = str(userWidthInput) + "x" + str(userHeightInput)
                #if not os.path.exists(sizeText):
                #    os.makedirs(sizeText)
                #i.save(sizeText + '/{}_'+ sizeText +'{}'.format(fn, fext))
                i.save('ResizedPhotos/{}_resized{}'.format(fn, fext))
