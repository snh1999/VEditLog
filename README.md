# VEditLog

[The Edited video](./images-videos/demo.mp4)

![Tutorial Demo](./images-videos/output.gif "Tutorial Demo")
For some reason, the converted gif image looks weird on github README. So I added short summary with images.

|      Welcome Screen       |       Open Project        |        New Project        |
| :-----------------------: | :-----------------------: | :-----------------------: |
| ![](/images-videos/1.png) | ![](/images-videos/2.png) | ![](/images-videos/3.png) |

|       Editor Window       |
| :-----------------------: |
| ![](/images-videos/5.png) |

<ul>
<li>Top Left : Project Details[1]</li>
<li>Top Right : Video Player[2]</li>
<li>Bottom Left : History[3]</li>
<li> Bottom Right : Current Video details[4]</li>
<li> Window sizes are adjustable, </li>
</ul>

|        Video Added        |
| :-----------------------: |
| ![](/images-videos/6.png) |

<ul>
<li>Opening Video (at <u>Video Player[2]</u>) updates source path, and makes other features editable at <u>Current Video details[4]</u></li>
<li>After necessary edit is done, <b>Add To project</b> takes it to <u> Project Details[1]</u></li>
<li>Double Click on any row (video) from <u>Project Details[1]</u> opens the video in <u>Player[2]</u> and makes effects editable at  <u>Current Video details[4].</u> Update or delete is possible from there</li>
<li> There is option for Save, Render and Commit from <u>Project Details[1]</u> </li>
</ul>

<h3><b>Current State</b></h3>
I kind of broke the code trying to apply Design Pattern Principles (while fixing the undo/redo AKA History mechanism).  (I will be back at development of that as soon as I complete bug2progress frontend).

<details open>
    <summary><h3> Active Features</h3></summary>
    <ul>
    <li>Supports Trim, Volume-Speed control, Resizing (changing quality) </li>
    <li>Effects: Rotate, Fade In, Fade Out, Reverse </li>
    <li>Projects Saved to json file (limited Git support)</li>
    </ul>
</details>

<details open>
    <summary><h3> Plans Before first Release</h3></summary>
    <ul> 
    <li>Multiple file insert to project</li>
    <li>Aggregate time in Project Details Window</li>
    <li>Modification Project Details Window view</li>
    <li> GUI status Bar</li>
    <li>Proper Dialogue Boxes</li>
    <li>Shortcuts (To be added after history is restored, a few of shortcyts already added)</li>
    <li>Useability Improvement (continous)</li>
    <li>Frame by Frame feature for Player </li>
    <li>Preview (This part is technically done, but for some reason application crashes. So for now, That is kept on queue) </li>
    <li>Github Integration (Done, for authentication done beforehand)</li>
    </ul> 
</details>

<details Close>
    <summary><h3> Feature Plans for Future (Click to expand) </h3></summary>
    <ul>
    <li>More effects from moviepy library</li>
    <li>In app Git GUI (To access different commit/changes and revert from app) </li>
    <li>Traditional drag drop version of editor (The simpler, lighter layout will be there too)</li>
    </ul> 
</details>

</div>
