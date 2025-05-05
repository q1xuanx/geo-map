

function startSearch(){
    const nameCountry = document.getElementById('nameCountry').value;
    fetch(`http://127.0.0.1:8000/search?country=${nameCountry}`,{
        method:'GET', 
        credentials: 'include'
    })
    .then ((response) => response.json())
    .then(data => {
        if (data.code === 200){
            window.location.replace('http://127.0.0.1:5500/views/map.html')
        }else {
            alert("Not found !")
        }
    });
}