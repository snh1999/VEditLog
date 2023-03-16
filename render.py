from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx


# cut video
clip1 = VideoFileClip("test/1.mp4").subclip(10, 20).fx(vfx.fadeout, 1)
clip_dimensions = clip1.size
# clip.duration
# clip.fps
# clip1.rotate(180)
# clip1.volumex(1)
# clip1.crossfadein(2)
# clip1.audio # gets the audio of the clip
# clip1.set_audio


clip2 = VideoFileClip("test/1.mp4").subclip(0, 5)

combine = concatenate_videoclips([clip1, clip2])
# combine.write_videofile("added.mp4")

# class Render:
#     def __init__(self):
#         pass
