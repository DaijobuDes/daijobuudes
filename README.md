# daijobuudes
A simple discord python bot

## Requirements
Open a terminal (linux) or command prompt (windows)

Clone this repository first by `git clone https://github.com/DaijobuDes/daijobuudes` and
then `cd daijobuudes`

Core prerequisties, `discord`, `discord.py` and automatic dependencies.
For audio core, `PyNaCl`, `youtube-dl` and `ffmpeg` must be installed.

### For linux systems

`# apt update && apt install ffmpeg`

`$ python3 -m pip install requirements.txt`

### For windows systems

Download the latest `youtube-dl` on https://youtube-dl.org/

Make sure you added `youtube-dl` to `%PATH%` or either move it to C:\Windows\System32 (not recommended).

To install python packages

`C:\Users\user> pip install requirements.txt`

## Running the bot
Simply open a terminal in linux or command prompt in Windows then type `python3 main.py`.
Also works in Android phones using Termux with dependencies installed.


## Bot Token
Simply get it from here https://discord.com/developers/applications/

Create a `token.txt` inside the directory with your discord bot token.
This is to separate the bot token for privacy purposes.


### TO-DO
- [ ] Complete rewrite of my IRC bot used in messenger to discord bot (probably)
- [ ] Code cleanup
- [ ] Moderation tools
- [ ] Games
- [ ] Bot Status
- [ ] IRC relay to Discord either through webhook
- [ ] Math
- [ ] Hashes
- [x] Audio core 
- [ ] Embeds (not yet fully implemented)
- [ ] And others
