function generate(x,attacking,unitnum){
    let ret = "";
    let bonus = 0;
    let type = 0;
    bonus = 0;
    type = 0; //3 is air (2 probably armor)
    ret += `unit${unitnum} = unit("${type}",${x.unit_off_str},${x.unit_def_str},${x.unit_speed},${x.unit_max_health},${bonus},[]);\n`;
    return(ret);
}


let a = await fetch(`https://api.nationsgame.net/game/getBattleData.php?battle=${window.location.href.substring(35)}`, {
  "headers": {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  },
  "referrer": window.location.href,
  "referrerPolicy": "no-referrer-when-downgrade",
  "body": null,
  "method": "GET",
  "mode": "cors",
  "credentials": "include"
});
let b = await a.json();

let str = "";
let unit = 0;
b.defenders[0].groups[0].units.forEach(function(x){unit++;str += generate(x,0,unit);});
b.defenders[1].groups[0].units.forEach(function(x){unit++;str += generate(x,0,unit);});
str += "\n";
unit = 0;
b.attackers[0].groups[0].units.forEach(function(x){unit++;str += generate(x,0,unit);});
b.attackers[1].groups[0].units.forEach(function(x){unit++;str += generate(x,0,unit);});
console.log(str);
