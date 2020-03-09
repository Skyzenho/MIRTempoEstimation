import os
import xml.etree.ElementTree as et
import glob

dir_dataset_mp3="C:/TCC/BallRoom/"
dir_dataset_wav="C:/TCC/BallRoomWAV/"

xtree = et.parse("extendedballroom_v1.1.xml")
xroot = xtree.getroot()

rows_mp3=[]
rows_wav=[]
for node in xroot: 
    for song in node:
        s_rit=node.tag
        s_id=song.attrib.get("id")
        rows_mp3.append(dir_dataset_mp3+s_rit+'/'+s_id+'.mp3')
        rows_wav.append(dir_dataset_wav+s_rit+'/'+s_id+'.wav')
        
print("Start Convertion MP3 to WAV")
for i in range(len(rows_mp3)):
    os.system(f"""ffmpeg -i {rows_mp3[i]} -acodec pcm_u8 -ar 22050 {rows_wav[i]}""")
    print(f"""{i} Concluido""")

