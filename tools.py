from PIL import Image
from os import listdir

def greyscaleConverter(source_dir, dist_dir):
    '''
    Parameters
    ----------
    source_dir : source_dir image path
    dist_dir : the path to save converted image
    converts source_dir image to greyscale and saves it to dist path
    '''
    image = Image.open(source_dir)
    grayscale = image.convert('L')
    grayscale.save(dist_dir +'\\'+ source_dir.split('\\')[-1])

def collectImages(source_dir):
    '''
    Parameters
    ----------
    source_dir : dir of desired folder

    Returns
    -------
    imageArray : array that contains paths of all images in souce_dir.

    '''
    imageArray = []
    print("FOUNDED IMAGES:\n")
    for file in listdir(source_dir):
        if(file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg')):
           imageArray.append(source_dir + '\\' + file)
           print(source_dir + '\\' + file)
    print(len(imageArray),"images are found.")
    return imageArray

def convertAllImagesInFolder(source_dir, dist_dir):
    imageArray = collectImages(source_dir)
    for image in imageArray:
        greyscaleConverter(image, dist_dir)