# Image-Filter
Filters ppm p3 images to a user-specified number of core colors

Some notes on use:
Program only accepts images formatted to ppm with a magic number of p3
Images of this type can be obtained from the Linux command line
Program returns a new image also formatted as a ppm with a magic number of p3
Also, the greater the number of colors the user requests, the longer the program will take to execute
Takes 2-7 minutes depending on input size (input of 10 ranges somewhere between 4-7 minutes)

Some future goals:
Add additional image manipulation functions (increasing brightness, reducing blurriness, etc)
Allow users to upload different formatted images
Optimize image filtering algorithm

