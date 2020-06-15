//import
const mathlab = require('./mathlab');
const unitClass = require('./Unit');

// ______________________________________________________________________________
// make your units here:
// just drop the percent sign where necessary.
// syntax is unit(type, fp, arm, man, hp, continent+defense bonuses, type bonuses (like 10% damage against armor), counters, healing, shots per turn (as in jackhammer attacks))

// say I have a mortar infantry with 10% healing to friendly infantry, 20% defense bonus, and  10% damage increase against armor/air
exampleMortar = new unitClass.unit("Infantry", 3, 2, 2, 50, 20, [["Armor", 10],["Air", 10]], ["Infantry"], [["Infantry", 10]],2);
exampleInfantry = new unitClass.unit("Infantry", 3, 1, 2, 50, 0, [], [], [],1);
testHealer = new unitClass.unit("idkMan", 0,0,0,10,0,[],[],[["Infantry",30]],1);

unit1 = new unitClass.unit("Special Forces",4,1,4,50,0,[["Infantry",50]],[],[],1);
unit2 = new unitClass.unit("Special Forces",4,1,4,50,0,[["Infantry",50]],[],[],1);
unit3 = new unitClass.unit("Special Forces",4,1,4,50,0,[["Infantry",50]],[],[],1);
unit4 = new unitClass.unit("Special Forces",4,1,4,50,0,[["Infantry",50]],[],[],1);
unit5 = new unitClass.unit("Special Forces",4,1,4,50,0,[["Infantry",50]],[],[],1);
unit6 = new unitClass.unit("Special Forces",4,1,4,50,0,[["Infantry",50]],[],[],1);
unit7 = new unitClass.unit("Special Forces",4,1,4,50,0,[["Infantry",50]],[],[],1);
unit8 = new unitClass.unit("Special Forces",4,1,4,50,0,[["Infantry",50]],[],[],1);
unit9 = new unitClass.unit("Special Forces",4,1,4,50,0,[["Infantry",50]],[],[],1);

eunit1 = new unitClass.unit("Infantry",5,2,4,56,0,[],["Special Forces"],[],1);
eunit2 = new unitClass.unit("Infantry",4,4,2,60,0,[],["Special Forces"],[],1);
eunit3 = new unitClass.unit("Infantry",5,2,2,62,0,[],["Special Forces"],[],1);
eunit4 = new unitClass.unit("Infantry",4,1,4,62,0,[],["Special Forces"],[],1);
eunit5 = new unitClass.unit("Infantry",4,2,5,50,0,[["Static",10]],["Special Forces"],[],1);
eunit6 = new unitClass.unit("Infantry",3,2,5,62,0,[],["Special Forces"],[],1);
eunit7 = new unitClass.unit("Infantry",3,2,2,50,0,[],["Special Forces"],[],1);
eunit8 = new unitClass.unit("Infantry",3,1,3,56,0,[],["Special Forces"],[],1);
eunit9 = new unitClass.unit("Infantry",3,1,2,56,0,[],["Special Forces"],[],1);

// ______________________________________________________________________________

// instantBattle simulates the battle 'rounds' number of times and prints how many each side won with remaining units
// change pFriendlies and pEnemies to fit how many units you have in your battle and what you named them.
async function instantBattle(rounds){
    const pFriendlies = [unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8, unit9]//, unit10, unit11, unit12, unit13, unit14, unit15, unit16, unit17, unit18, unit19, unit20];
    const pEnemies = [eunit1, eunit2, eunit3, eunit4, eunit5, eunit6, eunit7, eunit8, eunit9]//, eunit10, eunit11, eunit12, eunit13, eunit14, eunit15, eunit16, eunit17, eunit18, eunit19, eunit20];

    let friendlies = pFriendlies.slice();
    let enemies = pEnemies.slice();

    let enemyWins = 0;
    let friendliesretreated = 0;
    let friendlyWins = 0;
    let enemiesretreated = 0;
    let enemyremainder = 0;
    let friendlyremainder = 0;
    for(roundnum = 0; roundnum < rounds; roundnum++){
        let winner = "unknown";
        while (winner == "unknown"){
            let order = await mathlab.initiativeRoll(friendlies.slice(), enemies.slice());
            for(let i = 0; i < order.length; i++){
                if (friendlies.length > 0 && enemies.length > 0 && order[i].alive && winner == "unknown"){
                    if (friendlies.includes(order[i])){
                        let target = enemies[Math.floor(Math.random() * enemies.length)];
                        await mathlab.attack(order[i], target, pEnemies);
                        if (target.alive == false){
                            enemies.splice(enemies.indexOf(target), 1);
                            if (enemies.length == 0){ winner = "friendlies";}
                        }
                    }
                    else if (enemies.includes(order[i])){
                        let target = friendlies[Math.floor(Math.random() * friendlies.length)];
                        await mathlab.attack(order[i], target, pFriendlies);
                        if (target.alive == false){
                            friendlies.splice(friendlies.indexOf(target), 1);
                            if (friendlies.length == 0){ winner = "enemies";}
                        }
                    }
                    if(winner == "unknown"){ winner = mathlab.checkRetreat(friendlies, enemies);}
                }
            }
        }
        if (winner == "enemies"){
            enemyWins += 1;
            enemyremainder += enemies.length;
            friendliesretreated += friendlies.length;
        }
        if (winner == "friendlies"){
            friendlyWins += 1;
            friendlyremainder += friendlies.length;
            enemiesretreated += enemies.length;
        }
        friendlies = pFriendlies.slice();
        enemies = pEnemies.slice();
        pFriendlies.forEach(function(unit){
            unit.hp = unit.maxhp;
            unit.alive = true;
        });
        pEnemies.forEach(function(unit){
            unit.hp = unit.maxhp;
            unit.alive = true;
        });
    }
    if(friendlyWins > 1){ friendlyremainder /= friendlyWins; enemiesretreated /= friendlyWins;}
    if(enemyWins > 1){ enemyremainder /= enemyWins; friendliesretreated /= enemyWins;}
    console.log(`${friendlyWins} friendly wins vs ${enemyWins} enemy wins`);
    console.log(`On average, when the the friendlies won, the friendlies had ${Math.round(friendlyremainder)} units left while enemies had ${Math.round(enemiesretreated)} units retreat.`);
    console.log(`On average, when the the enemies won, the enemies had ${Math.round(enemyremainder)} units left while friendlies had ${Math.round(friendliesretreated)} units retreat.`);
}

instantBattle(1000);

//mathlab.attack(attacker,defender,allies);
//mathlab.attack(eunit1,unit1,[]);
//attack(exampleMortar, exampleInfantry, [exampleInfantry, testHealer]);
