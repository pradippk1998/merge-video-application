from moviepy.editor import *
clip1=VideoFileClip("1.mp4").subclip(3,7)
clip2=VideoFileClip("2.mp4").subclip(1,4)
clip2=clip2.set_position((45,150))
final_video=concatenate_videoclips([clip1,clip2])
final_video.write_videofile("new.mp4")