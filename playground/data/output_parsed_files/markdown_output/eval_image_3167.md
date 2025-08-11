

# Innovative driving stage for EV inverter
## able to drive IGBT + SiC SIMULTANEOUSLY in synergy

[Circuit diagram showing MCU connected to LOGIC block, which connects to two transistor symbols with an arrow indicating "LOSSES" direction]

| Current (A) | SiC Losses | IGBT Losses | Performance Advantage          |
| ----------- | ---------- | ----------- | ------------------------------ |
| 0-75        | Lower      | Higher      | SiC is better at low current   |
| 75-200      | Higher     | Lower       | IGBT is better at high current |


## Less expensive BOM vs. full SiC
## More efficient than full IGBT

**TODAY**  
ALL SiC  
[Circuit diagram showing 4 SiC transistors in series]

→

**NEW - Hybrid approach**  
SiC + IGBTs  
[Circuit diagram showing 2 SiC transistors and 2 IGBTs with diodes]

### BOM Cost saving
* Dedicate output stage able to drive SiC + IGBT SIMULTANEOUSLY

### Compact  
* On-chip galvanic isolation

### Robustness
* High voltage rail 1200 V
* Immunity up to >100 V/ns CMTI  
* Negative gate drive ability (-10 V)
