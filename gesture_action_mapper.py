import pyautogui
import subprocess
import sys


def _mac_osascript(commands):
    # commands: list of AppleScript -e strings
    cmd = ["osascript"]
    for c in commands:
        cmd += ["-e", c]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


def perform_action(gesture):
    """Map a gesture string to a system action.

    On macOS we use AppleScript (osascript) for reliable volume/mute control.
    For other keys we fall back to pyautogui.
    """
    print(f"perform_action: {gesture}")

    # macOS-specific volume controls (more reliable than pyautogui media-key presses)
    if sys.platform == "darwin":
        if gesture == "Pointing Up":
            # increase volume by 10, cap at 100
            cmds = [
                'set cur to output volume of (get volume settings)',
                'set new to cur + 10',
                'if new > 100 then',
                'set new to 100',
                'end if',
                'set volume output volume new'
            ]
            if _mac_osascript(cmds):
                print("perform_action: increased volume via osascript")
                return
        elif gesture == "Peace":
            # decrease volume by 10, floor at 0
            cmds = [
                'set cur to output volume of (get volume settings)',
                'set new to cur - 10',
                'if new < 0 then',
                'set new to 0',
                'end if',
                'set volume output volume new'
            ]
            if _mac_osascript(cmds):
                print("perform_action: decreased volume via osascript")
                return
        elif gesture == "Fist":
            # toggle mute
            cmds = [
                'set cur to output muted of (get volume settings)',
                'if cur then',
                'set volume output muted false',
                'else',
                'set volume output muted true',
                'end if'
            ]
            if _mac_osascript(cmds):
                print("perform_action: toggled mute via osascript")
                return

    # Fallback / generic actions
    if gesture == "Pointing Up":
        print("perform_action: falling back to pyautogui volumeup")
        try:
            pyautogui.press("volumeup")
        except Exception as e:
            print("perform_action: pyautogui volumeup failed:", e)
    elif gesture == "Peace":
        print("perform_action: falling back to pyautogui volumedown")
        try:
            pyautogui.press("volumedown")
        except Exception as e:
            print("perform_action: pyautogui volumedown failed:", e)
    elif gesture == "Thumbs Up":
        # play/pause: send space (works when the media window is focused)
        print("perform_action: sending space via pyautogui")
        try:
            pyautogui.press("space")
        except Exception as e:
            print("perform_action: pyautogui space failed:", e)
    elif gesture == "Open Hand":
        print("perform_action: sending right arrow via pyautogui")
        try:
            pyautogui.press("right")
        except Exception as e:
            print("perform_action: pyautogui right failed:", e)
    elif gesture == "Fist":
        print("perform_action: falling back to pyautogui volumemute")
        try:
            pyautogui.press("volumemute")
        except Exception as e:
            print("perform_action: pyautogui volumemute failed:", e)
