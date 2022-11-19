cp ./asound.conf /etc/asound.conf
sed -n -i -e 's/defaults.ctl.card 0/defaults.ctl.card 1/g' \
-e 's/defaults.pcm.card 0/defaults.pcm.card 1/g' \
-e 's/pcm.front cards.pcm.front/#pcm.front cards.pcm.front/g' \
-e 's/dpcm.rear cards.pcm.rear/#pcm.rear cards.pcm.rear/g' \
-e 's/pcm.center_lfe cards.pcm.center_lfe/#pcm.center_lfe cards.pcm.center_lfe/g' \
-e 's/pcm.side cards.pcm.side/#pcm.side cards.pcm.side/g' \
-e 's/pcm.surround21 cards.pcm.surround21/#pcm.surround21 cards.pcm.surround21/g' \
-e 's/pcm.surround40 cards.pcm.surround40/#pcm.surround40 cards.pcm.surround40/g' \
-e 's/pcm.surround41 cards.pcm.surround41/#pcm.surround41 cards.pcm.surround41/g' \
-e 's/pcm.surround50 cards.pcm.surround50/#pcm.surround50 cards.pcm.surround50/g' \
-e 's/pcm.surround51 cards.pcm.surround51/#pcm.surround51 cards.pcm.surround51/g' \
-e 's/pcm.surround71 cards.pcm.surround71/#pcm.surround71 cards.pcm.surround71/g' \
-e 's/pcm.iec958 cards.pcm.iec958/#pcm.iec958 cards.pcm.iec958/g' \
-e 's/pcm.spdif iec958/#pcm.spdif iec958/g' \
-e 's/pcm.hdmi cards.pcm.hdmi/#pcm.hdmi cards.pcm.hdmi/g' \
-e 's/pcm.modem cards.pcm.modem/#pcm.modem cards.pcm.modem/g' \
-e 's/pcm.phoneline cards.pcm.phoneline/#pcm.phoneline cards.pcm.phoneline/g' \
/usr/share/alsa/alsa.conf
