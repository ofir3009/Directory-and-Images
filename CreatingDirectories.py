import os
import matplotlib.pyplot as plt
#import opencv
from PIL import Image
import numpy as np
import shutil

def CreateDirectory(path, name):
    '''
    Function gets the parameters:
    path = the path of the directory we want to create.
    name = the name of the directory we want to create.
    Function creates a directory with the name and the path.
    Returns the directory's address
    '''
    if (path==""):                                                                              #User input in ENTER
        path= r"C:\Users\PCP\Desktop"                                                           #path will be on desktop as default
    path=os.path.join(path, name)                                                               #path is needed to have the name in it to create it
    print("Directory will be created in the path: " + path)
    try:
        os.mkdir(path)                                                                          #Calling the function that will create the directory
    except OSError:                                                                             #When there is already a directory with the same name.
        print("Creation of the directory %s failed" % path)                                     #print that there was an error in creating the directory
    else:
        print ("Succesfully created directory %s " % path)                                      #print that the creation was successful
    return path
        
def SaveFiles(Source_path,Which_One,Train_path,Test_path):
    '''
    Function gets the parameters:
    Source_path = the path of a directory with jpg images in it
    Which_One = input string that determines if the images go to test or train
    If user inputted train: transfer 70% of the images
    If user inputted test: transfer all of the images
    '''
    if(Which_One=="test"):                                                              #If the path leads to test directory
        for file in os.listdir(Source_path):                                                                #A loop to move every file
            shutil.move(os.path.join(Source_path, file), os.path.join(Test_path,file))     #moving file from source to directory
    if(Which_One=="train"):                                                             #If the path leads to train directory
        i=0.0                                                                                   #setting a counter for number of files
        for file in os.listdir(Source_path):                                                               #loop to count how many files are in the source directory
            i=i+1                                                                               #increase count by 1
        i =int(0.7*i)                                                                           #Multiplying the counter by 0.7 so it we can take 70% of the files in the source
        for file in os.listdir(Source_path):                                                                #a loop to move 70% of the files in the source directory
            if i>0:                                                                         #while loop to help stop the moving of the files at 70%
                shutil.move(os.path.join(Source_path,file),os.path.join(Train_path,file))   #moving file from source to directory
                i=i-1                                                                           #decrease count by 1 - essential for our while loop
 
def image_plot(path):
    '''
    function gets the parameters:
    images = the test path or the train path
    Function prints all of the images in plot
    '''
    li=os.listdir(path)
    #image_array = [np.array(Image.open(filename)) for filename in li]
    image_array =  [np.array(Image.open(os.path.join(path,filename))) for filename in li]
    f,axs=plt.subplots(len(image_array))
    for i in range(len(image_array)):
        axs[i].imshow(image_array[i])
    plt.tight_layout()
    plt.show()
    
#Input for main directory
TheDirectoryPath = input("Enter Directory Path, press enter to create the directory on desktop ") #Main directory path input
TheDirectoryName = input("Enter Directory Name ")                                                 #Main directory name input
TheDirectoryPath = CreateDirectory(TheDirectoryPath, TheDirectoryName)                            #Creating the Directory with the name 'Dina_Directory'
#Creating Train and Test directories
#Train
Train_Path=TheDirectoryPath                                                                     # The Train directory path will be updated in its creation
Train_Path = CreateDirectory(Train_Path, "train")
#Test
Test_Path=TheDirectoryPath                                                                      # The Test directory path will be upddated in its creation
Test_Path = CreateDirectory(Test_Path, "test")
#Saving files in test or train
Which_One = input("type 'test' for test directory, type 'train' for train directory ")
SaveFiles(input("Enter Source Directory Path: "), Which_One, Train_Path, Test_Path)
#Showing the images in plot
if(Which_One=="test"):
    image_plot(Test_Path)
if(Which_One=="train"):
    image_plot(Test_Path)