## Install Python 3.10
Make sure to install `libssl-dev` and `libffi-dev` before installing Python 3.10.
Download the source and install using `./configure --enable-optimizations` and `sudo make altinstall`.

## Create asound.conf
Create the file `/etc/asound.conf` with the following content:
```
pcm.!default {
    type hw
    card 1
}
ctl.!default {
    type hw
    card 1
}
```

## Modify alsa config
In the `/usr/share/alsa/alsa.conf` file change the following lines
```
defaults.ctl.card 0
defaults.pcm.card 0
```
to
```
defaults.ctl.card 1
defaults.pcm.card 1
```
and comment out the following lines by adding a `#` to the start of the line
```
pcm.front cards.pcm.front
pcm.rear cards.pcm.rear
pcm.center_lfe cards.pcm.center_lfe
pcm.side cards.pcm.side
pcm.surround21 cards.pcm.surround21
pcm.surround40 cards.pcm.surround40
pcm.surround41 cards.pcm.surround41
pcm.surround50 cards.pcm.surround50
pcm.surround51 cards.pcm.surround51
pcm.surround71 cards.pcm.surround71
pcm.iec958 cards.pcm.iec958
pcm.spdif iec958
pcm.hdmi cards.pcm.hdmi
pcm.modem cards.pcm.modem
pcm.phoneline cards.pcm.phoneline
```