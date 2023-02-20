

function chatgptpycall(){
    
    const spawn = require('child_process').spawn;
    
    const result = spawn('python', ['~/py/chatgpt_api.py']);

    result.stdout.on('data', (result)=>{
        console.log(result.toString());
        
    })};

chatgptpycall();




