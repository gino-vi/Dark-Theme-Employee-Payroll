"use strict";

/*
   digital clock javascript file
   
   function getWeekday(dayNum)
      Returns the text of the day of the week where dayNum
      is the number of the week from 0 (Sunday) to 6 (Saturday)
*/

runClock();
setInterval("runClock()", 1000);


function runClock() {
  console.log("Function Running");
  var thisDay = new Date();
  var thisDate = thisDay.toLocaleDateString();
  var thisDayNum = thisDay.getDay();
  var thisWeekday = getWeekday(thisDayNum);
  var thisTime = thisDay.toLocaleTimeString();

  document.getElementById('date').innerHTML = thisDate;
  document.getElementById("wday").innerHTML = thisWeekday;
  document.getElementById('time').innerHTML = thisTime;
}

function getWeekday(dayNum) {
   var wDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
   return wDays[dayNum];
}
