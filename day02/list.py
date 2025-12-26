a = [100,200,300,4.5, True] # Option 1 
print (type(a))
a.append(10)
print(a)

clouds = list (["aws", "azure", "gcp", "utho"]) # Option 2
# print (dir (type (clouds)))
print ("Amazon Cloud Provider is: ", clouds[0])
print ("Microsoft Cloud Provider is: ", clouds[1])
print ("Google Cloud Provider is: ", clouds[2])
print(clouds.extend.__doc__)

for cloud in clouds:
    if cloud == "aws":
        print ("AWS is amazing")
    elif cloud == "azure":
        print ("azure is now Entra")
    elif cloud == "gcp":
        print ("GCP is growing fast")
    else:
        print ("Utho is indian Cloud Provider")
