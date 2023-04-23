# kmeans-img
These scripts run kmeans on an image and save (or display) the result.

## Which script to use?
There are two scripts in this repo, `kimg.py` is a terminal utility that receives the input, output filenames and number of clusters and saves the result.
`gkimg.py` has a GUI made with CustomTKInter, it can also display results before saving.
## Dependencies
- opencv
- numpy
- matplotlib
- tkinter
- customtkinter
- CTkMessagebox
## Usage
To use `kimg.py`, use it like this:
```console
$ ./kimg.py <clusters> <input> <output>
```
Like this:
```console
$ ./kimg.py 5 example.jpg input.jpg
```
To use `gkimg.py` simply run it, either by clicking it or by using the console:
```console
$ ./gkimg.py
```
It will open a window where you simply select a file and a k value, generate an output and preview it, if you like the result, you can save the image.
## Example
This image was run through k means with a k value of 5:
![Example input](https://github.com/AxelElRojo/kmeans-img/blob/main/examples/input.jpg?raw=true)
This was the result:
![Example result](https://github.com/AxelElRojo/kmeans-img/blob/main/examples/result.jpg?raw=true)
