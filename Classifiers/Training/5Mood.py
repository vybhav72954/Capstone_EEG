from pyAudioAnalysis import audioTrainTest as aT
midTerm = 3
shortTerm = 0.0625
aT.extract_features_and_train([
    "C:\\Users\\asus\\Desktop\\10sec\\Sad\\",
    "C:\\Users\\asus\\Desktop\\10sec\\Devotional\\",
    "C:\\Users\\asus\\Desktop\\10sec\\Happy\\",
    "C:\\Users\\asus\\Desktop\\10sec\\Party\\",
    "C:\\Users\\asus\\Desktop\\10sec\\Romantic\\",
                               ],
                              midTerm, midTerm/4, shortTerm, shortTerm/4, "extratrees", "ET_5M_15-July", compute_beat=True, train_percentage=1.0)
print("******************************************************************************************************************************")
print("******************************************************************************************************************************")
print("******************************************************************************************************************************")
print("******************************************************************************************************************************")
print("******************************************************************************************************************************")
print("******************************************************************************************************************************")
print("******************************************************************************************************************************")
print("******************************************************************************************************************************")
print("******************************************************************************************************************************")
print("******************************************************************************************************************************")




print("******************************************************************************************************************************")
print("******************************************************************************************************************************")

