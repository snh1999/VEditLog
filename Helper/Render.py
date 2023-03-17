from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import math


class Render:
    @staticmethod
    def render_project(values_arr, file_path):
        print(values_arr)
        clip_arr = []
        for value in values_arr:
            clip_arr.append(Render.process_clip(value))
        
        combine = concatenate_videoclips(clip_arr)
        combine.write_videofile(file_path)


    # ["source", "start", "end", "quality", "volume", "speed", "is_reverse", "rotation(degree)", "fade in(s)", "fade out(s)"]
    @staticmethod
    def process_clip(value):

        source = value[0]
        clip = VideoFileClip(source)

        start = 0 if value[1] == '-' else int(value[1]) // 1000/ 60
        end = clip.duration if value[2] == '-' else int(value[2]) // 1000/ 60
        clip = clip.subclip(start, end)

        quality = 0 if value[3].startswith('default') else int(value[3].split('p')[0])

        volume = float(value[4])
        speed = float(value[5])
        clip = clip.volumex(volume).fx(vfx.speedx, 2)

        is_reverse = True if value[6] != "Normal" else False
        if is_reverse:
            clip = clip.fx(vfx.time_mirror)
            
        rotation = float(value[7])
        fade_in = float(value[8])
        fade_out = float(value[9])

        clip = clip.rotate(rotation).fx(vfx.fadein, fade_in).fx(vfx.fadeout, fade_out)

        if quality != 0:
            clip = clip.resize((math.ceil(quality * 1.7775), quality))
            
        return clip


