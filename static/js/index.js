function testAccuracy() {
    const file = document.getElementById('file').files[0]
    
    let data = new FormData();
    data.append('file', file);

    fetch('/dataset',{
        method:"post",
        body: data
    }).then(function (res) { 
        if(res.ok) sendData()
    }).catch(function() {
        alert("Error")
    });
}

function sendData(){
    const file = document.getElementById('file').files[0].name
    const type = document.getElementById('regression').checked ? document.getElementById('regression').value : document.getElementById('classification').value
    const algo = document.getElementById('algo').value

    fetch('/testmodel',{
        method:"post",
        headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            'file':file,
            'type':type, 
            'algo':algo
        })
    }).then(function (res) { 
        return res.json();
    }).then( function (data) {
        document.getElementById('testAccuracy').innerHTML = 'R2: '+data['testR2score']+", MAE: "+data['testMae'];
        document.getElementById('trainAccuracy').innerHTML = 'R2: '+data['trainR2score']+", MAE: "+data['trainMae'];
    });
}