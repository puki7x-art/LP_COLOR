# Launchpad Mini MK2 - Script Simple Colores Automáticos

import device
import midi

# Lista de colores seguros
COLORS = [15, 30, 45, 60, 75, 90, 105, 120]

# Obtener color según el pad
def get_color(note):
    return COLORS[note % len(COLORS)]

# Cuando tocás un pad
def OnNoteOn(event):
    note = event.data1
    color = get_color(note)
    
    device.midiOutMsg(midi.MIDI_NOTE_ON, note, color)
    
    event.handled = False

# Cuando soltás el pad
def OnNoteOff(event):
    note = event.data1
    
    device.midiOutMsg(midi.MIDI_NOTE_ON, note, 0)
    
    event.handled = False

# Al iniciar (apaga todo)
def OnInit():
    for i in range(128):
        device.midiOutMsg(midi.MIDI_NOTE_ON, i, 0)
      
