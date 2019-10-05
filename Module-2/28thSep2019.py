import numpy as np

def convertTextToNpArray(text):
    newArray = np.array(text.split(' '))

    newArray = newArray[((np.vectorize(len)) (newArray))<5]

    return newArray

def multiplyArrays(arr1 , arr2):

    return np.dot(np.array(arr1),(np.array(arr2)))

arr1 = [1,2]
arr2 = [1,2]
mytext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eu sagittis ligula," \
         " eget congue mi. Donec scelerisque, sem fringilla dignissim scelerisque, elit nibh euismod massa," \
         " vitae finibus dolor ligula ac dui? Ut dictum, turpis in tristique facilisis, ante ligula sollicitudin tortor, " \
         "vulputate semper nibh augue at lorem. Ut varius ullamcorper ligula id suscipit. Cras in congue elit, ac blandit turpis. " \
         "Vestibulum gravida nisi et neque lobortis, tincidunt mollis lorem finibus. Nullam viverra purus sit amet felis vestibulum viverra. " \
         "Vivamus ultrices egestas fringilla. Maecenas pharetra ex sit amet enim malesuada, sit amet ultricies eros commodo. Suspendisse lobortis dignissim tempor." \
         " Aliquam tellus tellus, ultricies eget lacinia sed, semper sit amet nibh. Aenean eget tellus diam. Suspendisse accumsan nisi sit amet sem convallis auctor." \
         "Quisque blandit tellus nec justo iaculis laoreet? Donec laoreet lacus ac volutpat venenatis!" \
         "Quisque at sagittis orci, sed porta odio. Phasellus sagittis malesuada enim, eget placerat magna maximus et." \
         " Etiam ut ligula dignissim lectus faucibus dapibus. Praesent rutrum purus eget diam aliquet mollis. Lorem ipsum dolor sit amet," \
         " consectetur adipiscing elit. Integer quis rutrum ex. Praesent nisi elit, porttitor sit amet orci eu, tincidunt varius magna." \
         " Praesent ornare tincidunt odio, in rhoncus nulla ultrices id. Nam nisl urna, imperdiet eu suscipit at, " \
         "commodo in quam. Aliquam arcu est, eleifend et cursus at, volutpat egestas orci. Aenean quis placerat mauris. " \
         "Etiam semper sollicitudin viverra. Ut commodo diam nibh, nec aliquet ipsum porta porttitor. Morbi sollicitudin diam vitae nulla cursus porttitor." \
         "Donec laoreet turpis in tortor auctor? quis egestas tellus sollicitudin. Sed placerat consectetur nibh! in consequat enim vulputate sit amet." \
         " In massa purus, tristique at dolor cursus, eleifend dapibus dolor. Pellentesque arcu enim, porttitor eu venenatis sodales, bibendum in nibh." \
         " Donec facilisis aliquet velit sed egestas. Maecenas posuere lectus ac ultricies finibus. Sed pharetra varius elit, vel convallis enim aliquet at."
# print(convertTextToNpArray(mytext))

myArray = ["ALI","PRINCE", "KHAN" , "IMRANKHAN"]
#
myArray=np.array(myArray)
#

def myFuc(array):

    return len(array)


myArray = myArray[(np.vectorize(len)(myArray))<5]

print(np.vstack(myArray))
print(np.hstack(myArray))

# print(multiplyArrays(arr1,arr2))