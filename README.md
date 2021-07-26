# Simple-Gillespie-Simulation
Motor protein walking on microtubule

The python script models motor protein walking on a microtubule track inside a cell.

Reactions and their rates in the model:

Reaction                        Rates 
Forward movement on the track - k 
Backward movement on the track - gamma
Dissociation from the track - delta

Change the rates in the script and play around and observe the changes in the trajectory of the movement of the protein.

Theoretical value for the average movement of the motor protein is calculated as: forward rate(k) - backward rate(gamma) / dissociation rate(delta)
The model should get closer & closer to the theoretical value as you increase the number of runs.
Approximately, in around 100,000 runs, the model becomes accurate upto 2 decimal points of the theoretical value.
