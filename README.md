# Use of the UR5 Robot to Help People with Disabilities Pick up Items

## Flow Designer:
- Hansen Ade R
- Itqan Fikri A

## Requirements
- Flask
- re (built-in)
- requests
- loguru
- streamlit
- os (built-in)
- time (built-in)
- Automate Android App (play store)

## Description
Robot controlled using speech recognition from Android and then sending it to a laptop program. The purpose of the robot is to be controlled using speech recognition and to pick up 3 items: a box, a bottle, and a Remote, then give them to the user. The location of each item is fixed without using additional sensors, as well as the location of the user.

There are several commands, including:
"Buka" to open the gripper
"Tutup" to close the gripper
"Siap" to move to the main position when the robot is usually first turned on
"Siaga" to move to the standby position
"Ambilkan Kontak" to pick up the box and give it to the person and then return to the standby position
"Ambilkan Botol" to pick up the bottle and give it to the person and then return to the standby position
"Ambilkan Remote" to pick up the can and give it to the person and then return to the standby position
"Kembalikan" to return the picked-up item to its original location
"Thank you" to open the gripper


control.py for the main code to control movements and post relay from the program
captured_text.txt as a temporary storage for commands (similar to a cache)

