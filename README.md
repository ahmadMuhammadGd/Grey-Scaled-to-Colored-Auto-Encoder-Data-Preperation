```
# Image Greyscale Converter

This Python script allows you to convert images from color to greyscale in a specified directory. It includes functions for converting individual images and for converting all images in a folder.

## Usage

### `greyscaleConverter`

This function converts a single image to greyscale and saves it to the destination directory.

```python
from PIL import Image

def greyscaleConverter(source_dir, dist_dir):
    '''
    Parameters
    ----------
    source_dir : str
        Source image path
    dist_dir : str
        The path to save the converted image

    Converts the source image to greyscale and saves it to the destination path.
    '''
    image = Image.open(source_dir)
    grayscale = image.convert('L')
    grayscale.save(f"{dist_dir}/{source_dir.split('/')[-1]}")
```

### `collectImages`

This function collects the paths of all image files (PNG, JPG, JPEG) in a specified directory.

```
from os import listdir

def collectImages(source_dir):
    '''
    Parameters
    ----------
    source_dir : str
        Directory of the desired folder

    Returns
    -------
    imageArray : list
        An array that contains paths to all images in the source_dir.
    '''
    imageArray = []
    print("FOUND IMAGES:\n")
    for file in listdir(source_dir):
        if (file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg')):
            imageArray.append(f"{source_dir}/{file}")
            print(f"{source_dir}/{file}")
    print(f"{len(imageArray)} images are found.")
    return imageArray
```

### `convertAllImagesInFolder`

This function uses the `collectImages` function to collect all images in a specified directory and then converts them to greyscale using the `greyscaleConverter` function.
```
def convertAllImagesInFolder(source_dir, dist_dir):
    imageArray = collectImages(source_dir)
    for image in imageArray:
        greyscaleConverter(image, dist_dir)
```

## Example

To convert all images in a folder, you can use the following code:

```
source_dir = 'input_folder'
dist_dir = 'output_folder'
convertAllImagesInFolder(source_dir, dist_dir)
```

This will convert all the images in the `input_folder` to greyscale and save them in the `output_folder`.

## Dependencies

- Python 3.x
- Pillow (PIL Fork) Library: You can install it using `pip install Pillow`.
<<<<<<< HEAD:README.md
=======
```
>>>>>>> 43ab5cfa166191dd0368d10985c471b97d42e563:README
