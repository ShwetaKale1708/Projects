function get_data(){
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var add  = document.getElementById("add").value;
    var con = document.getElementById("con").value;
    
    result={
        "name":name,
        "email":email,
        "add":add,
        "con":con 
    }
    
    var a = [];
    
    a = JSON.parse(localStorage.getItem('session')) || [];
    
    a.push(result);
    
      
    localStorage.setItem('session', JSON.stringify(a));
    data= JSON.stringify(a);
    document.write(data)
    
    // var blob=new Blob([data],{type:"text/plain;charset=utf-8"});
    // saveAs(blob,"static.txt")     
}
// function get(){
//     document.write(data)
// }

