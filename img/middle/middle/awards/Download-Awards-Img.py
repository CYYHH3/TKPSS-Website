import requests

start_jpg = 146
end_jpg = 166

start_png = 167
end_png = 168

if_start_jpg = "start_jpg" in dir()
if_end_jpg = "end_jpg" in dir()

if_start_png = "start_png" in dir()
if_end_png = "end_png" in dir()

print("\n")

if if_start_jpg == True and if_end_jpg == True:
    while start_jpg <= end_jpg:
        print('Downloading "awards_' + str(start_jpg) + '.jpg"...')
        download_jpg = requests.get("http://tkpss.edu.hk/v2/_images/awards/awards_" + str(start_jpg) + ".JPG")
        open("awards_" + str(start_jpg) + ".jpg", "wb").write(download_jpg.content)
        print("Success!")
        start_jpg +=1

if if_start_png == True and if_end_png == True:
    while start_png <= end_png:
        print('Downloading "awards_' + str(start_png) + '.png"...')
        download_png = requests.get("http://tkpss.edu.hk/v2/_images/awards/awards_" + str(start_png) + ".png")
        open("awards_" + str(start_png) + ".png", "wb").write(download_png.content)
        print("Success!")
        start_png +=1

print("\n")