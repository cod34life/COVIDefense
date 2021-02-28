document.getElementById("v").onclick = function() {getVaccine()};

function getVaccine() {
  fetch('https://us-central1-aiot-fit-xlab.cloudfunctions.net/gamesave', {method: 'POST'},
       body:JSON stringify({
      "opponents":{
      "COVID-19":[
         {
            "level":"100"
         },
         {
            "attack":"70"
         },
         {
            "maxhealth":"500"
         },
         {
            "remaininghealth":"370"
         }
      ],
      "Player":[
         {
            "level":"107"
         },
         {
            "attack":"30"
         },
         {
            "maxhealth":"500"
         },
         {
            "remaininghealth":"220"
         },
         {
            "strength":"30"
         },
         {
            "defense":"50"
         },
         {
            "healing":"25"
         },
         {
            "luck":"10"
         },
         {
            "loot":"15"
         },
         {
            "exp":"82"
         }
      ]
   }
})).then(results=>results.json()).then(console.log);

}


document.getElementById("m").onclick = function() {wearMask()};

function wearMask() {
  fetch('https://us-central1-aiot-fit-xlab.cloudfunctions.net/gamesave', {method: 'POST'},
       body:JSON stringify({
      "opponents":{
      "COVID-19":[
         {
            "level":"100"
         },
         {
            "attack":"70"
         },
         {
            "maxhealth":"500"
         },
         {
            "remaininghealth":"370"
         }
      ],
      "Player":[
         {
            "level":"107"
         },
         {
            "attack":"30"
         },
         {
            "maxhealth":"500"
         },
         {
            "remaininghealth":"220"
         },
         {
            "strength":"30"
         },
         {
            "defense":"50"
         },
         {
            "healing":"25"
         },
         {
            "luck":"10"
         },
         {
            "loot":"15"
         },
         {
            "exp":"82"
         }
      ]
   }
})).then(results=>results.json()).then(console.log);

}

document.getElementById("p").onclick = function() {takePills()};

function takePills() {
   fetch('https://us-central1-aiot-fit-xlab.cloudfunctions.net/gamesave', {method: 'POST'},
       body:JSON stringify({
      "opponents":{
      "COVID-19":[
         {
            "level":"100"
         },
         {
            "attack":"70"
         },
         {
            "maxhealth":"500"
         },
         {
            "remaininghealth":"370"
         }
      ],
      "Player":[
         {
            "level":"107"
         },
         {
            "attack":"30"
         },
         {
            "maxhealth":"500"
         },
         {
            "remaininghealth":"220"
         },
         {
            "strength":"30"
         },
         {
            "defense":"50"
         },
         {
            "healing":"25"
         },
         {
            "luck":"10"
         },
         {
            "loot":"15"
         },
         {
            "exp":"82"
         }
      ]
   }
})).then(results=>results.json()).then(console.log);

}