from k_means import *
from image_utils import *


print("Welcome to image filter")

print("Enter the name of the image you wish to convert")
file_name = input(">>")

print("Enter the name of your new image")
new_file_name = input(">>")

print("Enter the number of colors you want the image reduced to")
k = int(input(">>"))

print("Please wait. Converting Image.")

image = read_ppm(file_name)         # Reading the ppm file to a two-dimensional list
k_means = create_k_means(k, image)  # Creating random color averages

different = True
while different: # Loop runs while the k-mean color averages continues to change
    cluster_list = group_colors(image, k_means)  # Compares colors in image to k-mean color averages
    new_k_means = update_k_means(cluster_list)   # Creates a new k-means based off the cluster_list

    different = is_different(k_means, new_k_means)  # Determines whether the color averages are different
    k_means = new_k_means  # Sets most recent color average as the current color average

new_image = create_new_image(image, k_means)
save_ppm(new_file_name, new_image)

print(new_file_name, "has been created")





