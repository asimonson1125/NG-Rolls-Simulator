# NG-Rolls-Simulator
**A Python NationsGame battle simulator for division predictions**

(JS version added on June 6th, 2020 for Discord bots)

I reverse-engineered the battle mechanics of the browser game, [NationsGame](https://www.Nationsgame.net), and rebuilt them into this python project that can simulate individual attacks as well as run mass battle simulations to determine the victor and remaining units.  It includes the following elements from the game:
* Base damage (estimation, but pretty close)
* Firepower
* Armor
* Maneuver
* HP
* Defense bonus
* Continent bonus
* Target-unit type bonuses
* Counters
* Friendly damage reduction (healing)
* Attacks per round (ie. MG Infantry and Jackhammer stat)
* Retreating
* Minimum damage output

It does not account for:
* Targeting
* Officers
* Real initiative rolls

I don't intend to implement targeting into this project because I wasn't able to pinpoint how it was done ingame other than a few specific conditions the game favors.  In the bigger and tougher battles I found the correlations to be virtually negligable, so I just made it random.  I won't be adding officers for the same reason.  Officers just amplifiy the effects of targeting, so nobody knows exactly how they work.

The initiative roll has many factors and getting the exact formula would be a heck of a headache for a fun project like this.  Instead, I just took a random roll and multiplied it by the unit's HP % squared ( and *3 if it counters Special Forces).  This shouldn't be a major factor in the long battles that I expect this to be used for anyway.

If you intend to use it, you should only need to look at `main.py` (or `predict.js` for the JavaScript version) to add your units and adjust how many battles you want to simulate.  Each unit has a ton of different stats and inputting them manually takes quite a while, so I also threw in `getUnitsFromBattle.js`.  Just paste this bad boy in the console on the battle page of what you want to simulate and it'll print out all of the unit stats like it was a regular Tuesday morning. 

I don't really care what you do with this since it's just a fun little project for a small browser game, so have fun!
