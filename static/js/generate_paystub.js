
function retrieveDateRange() {
    console.log("Running retriveDateDate() Method");
    var startDate = document.getElementById('so_period').value;
    var endDate = document.getElementById('eo_period').value;
    console.log(startDate);
    console.log(endDate);
    if(startDate) {
        if(endDate) {
            getDates(new Date(startDate), new Date(endDate));
        }
    } 
    
}

function getDates(startDate, endDate) {
    console.log("Running getDates() Method");
    const dateArray = [];
    let currentDate = new Date(
        startDate.getFullYear(),
        startDate.getMonth(),
        startDate.getDate() + 1 // add 1 day becuase of server base time
    );
    let newEndDate = new Date(
        endDate.getFullYear(),
        endDate.getMonth(),
        endDate.getDate() + 1 // add 1 day becuase of server base time
    )

    while (currentDate <= newEndDate) {
        dateArray.push(currentDate);

        currentDate = new Date(
            currentDate.getFullYear(),
            currentDate.getMonth(),
            currentDate.getDate() + 1 // will increate month if over range
        );
    }
    console.log(dateArray);
    
    var container = document.getElementById('container');
    
    for (dateSlot in dateArray) {
        var label = document.createElement('label');
        var labelText = document.createTextNode(dateArray[dateSlot].toDateString());
        var input = document.createElement('input');
        
        label.appendChild(labelText);
        
        input.setAttribute("name","dayBox");
        input.setAttribute("onchange", "findTotal()");
        input.setAttribute("type","number");
        input.setAttribute("step","0.01"); 
        input.setAttribute("placeholder","00"); 
        input.setAttribute("min","0"); 
        input.setAttribute("max","10"); 
        input.setAttribute("value","8.00");

        container.appendChild(label);
        container.appendChild(input);
    }
    findTotal();
}

function findTotal(){
    var arr = document.getElementsByName('dayBox');
    var tot = 0;
    for (var i = 0; i<arr.length; i++){
        if (parseFloat(arr[i].value < 10)){
            arr[i].setAttribute.value = 10;
            console.log(arr[i].value)
        }
        if (parseFloat(arr[i].value)){
            tot += parseFloat(arr[i].value);
            console.log(tot)
        }
    }
    document.getElementById('total').value = tot.toPrecision(4);
}

function resetDateSlots() {
    
    function removeAllChildNodes(parent) {
        while(parent.firstChild) {
            parent.removeChild(parent.firstChild);
        }
    }

    var container = document.getElementById('container');
    removeAllChildNodes(container);
    
}
