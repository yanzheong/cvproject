# CSE 455 Computer Vision Final Project

For our final project, we seek to augment the ease of access to the webcam using computers. Allowing users to communicate, execute commands using dynamic gestures that are recorded with the user's webcam. The dynamic gestures are defined as left to right, right to left, top to bottom, and bottom to right motion. Swipe right raises screen brightness, swipe left lowers screen brightness, swipe up increases the system's volume, and swipe down lowers the system's volume.  <br/>

# Approach
Our approach was to ultize OpenCv's optical flow to detect what the user's gesture. Once a gesture is detected, then the corresponding method is triggered. 

# Contributers:
Brian Zhu, Jasmine Woon, and Yan Zhe Ong

# Demo Video / Results
<a href="https://www.youtube.com/watch?v=p4-2M7LDLtY">Project Demo Video</a>

# Dicussion
<b> *What problms did you encounter* </b> <br/>

One problem that we encounter was downloading OpenCV compatible with C/C++. After multiple tries, we resorted to using OpenCV-python. As a result, we couldn't use the library we have built up from our homework. Another issue that we encounter was working on different operating systems. Our team is comprised of Mac and Windows users, so we had to look for a library to check which operating system is being used and then run the correct keyboard shortcut. In addition, Windows requires downloading utility programs or other modules to run command-line instructions. <br/>

Besides setup issues, we also ran into the problem of fine-tuning our motion detection. Our program has a difficult time recognizing the difference between left to right. Also, our python script had trouble detecting vertical lines.  <br/>

<b>*Are there next steps you would take if you kept working on the project?* </b> <br/>

If we kept working on the project, we would like to continue fine-tuning our four current dynamic gestures, so that our results are more consistent. Also, we would like to incorporate more gestures. One possibility is to add static gestures, and so we have more command-line options to run. With the addition of static images, we would require training so that our computer can recognize a user's hand gesture. <br/>


<b>*How does your approach differ from others? Was that beneficial?* </b> <br/>

Our approach differs from others by only looking at the instance we care about: when our palm is moving. We eliminated all noise that was originally part of OpenCV's repository. We used the angle of movement to check if the direction is horizontal or vertical movement. Once our program recognizes the movement, we will count how many times in that frame our palm is still moving in the same direction. Once we hit a threshold, then a command-line action is triggered. This approach was beneficial for us because we did not have to worry about counting motion other than our hands. We can control our threshold for our counter more easily too. <br/>



# References

<a href="https://github.com/opencv/opencv_contrib/blob/master/modules/optflow/samples/motempl.py">OpenCv library </a>

<a href="https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python">Determining OS systems</a>

<a href="https://www.nirsoft.net/utils/nircmd.html">Window nircmd (command-line actions)</a>

<a href="https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-appcommand">Window APPCommand (command-line actions for volume)</a>

<a href="https://coderwall.com/p/22p0ja/set-get-osx-volume-mute-from-the-command-line">Mac volume control</a>


<a href="https://osxdaily.com/2019/08/14/change-screen-brightness-mac-terminal/">Mac brightness control</a>
