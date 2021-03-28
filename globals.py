# Global variables
def init():
    # 0 = no-stimulus, 1 = audio, 2 = video
    global testMode
    testMode = 2

    global usingAudio
    usingAudio = False
    global usingVideo
    usingVideo = False

    if testMode == 1:
        usingAudio = True
    elif testMode == 2:
        usingVideo = True

    # use camera to record interactions
    global recordingOn
    recordingOn = True

    # use the audio of the video files
    global videoAudio
    videoAudio = False

    global pid

    global mediaorder
    mediaorder = [None, None, None, None]
