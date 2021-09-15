//http://jsbin.com/uboqu3/1/edit?html,js,output
var tileSize = 0;
var numTileX = 0;
var numTileY = 0;
var mapa = null;
window.setInterval(desenhaTudo, 100);
var selectedTile = [0,0];
var mapaTilesLargura = 0;
var mapaTilesAltura = 0;
var windowWidth = 0;
var windowHeight = 0;
var mapName = "";
function tileName(tile, prefix="t_"){
    return prefix + (tile[0] * numTileX + tile[1]);
}

function geraMapa(){
    var altura = document.getElementById('mapHeight').value;
    var largura = document.getElementById('mapWidth').value;
    windowWidth = document.getElementById('windowWidth').value;
    windowHeight = document.getElementById('windowHeight').value;

    mapa = new Array(altura);
    for(var i = 0; i < altura; i++){
        mapa[i] = new Array(largura);
        for(var j =0; j < largura; j++){
            mapa[i][j] = null;
        }
    }
    mapaTilesAltura = altura;
    mapaTilesLargura = largura;
    console.log(mapa);
}
function insereTile(evt){
    if(mapaTilesAltura == 0 || mapaTilesLargura == 0)
        return;
    var x = evt.offsetX, y = evt.offsetY ;
   
    var l =  Math.floor(y/tileSize);
    var c =Math.floor(x / tileSize) 
    l = mapaTilesAltura - l -1;
    mapa[l][c] = [selectedTile[0],selectedTile[1]];
   
}
function desenhaMapa(){
    if(mapaTilesAltura == 0 || mapaTilesLargura == 0)
        return;
    var mapCanvas = document.getElementById('map');
    mapCanvas.width = mapaTilesLargura * tileSize;
    mapCanvas.height = mapaTilesAltura * tileSize;
    var ctx = mapCanvas.getContext('2d');
    for(var i  = 0; i < mapaTilesAltura; i++){
        for(var j =0; j < mapaTilesLargura; j++){
            if(mapa[i][j]!=null){
               
                renderTile(mapa[i][j], i, j, ctx);
            }
        }
    }
    ctx.beginPath();
    ctx.strokeStyle = "black";
    for(var i  = 0; i < mapaTilesAltura; i++){   
        ctx.moveTo(0, i*tileSize);
        ctx.lineTo(mapCanvas.width, i*tileSize);
    }
    for(var j =0; j < mapaTilesLargura; j++){
        ctx.moveTo(j*tileSize, 0);
        ctx.lineTo(j*tileSize, mapCanvas.height);
    }
    ctx.stroke();
}
function renderTile(tile,i, j, ctx){
    //console.log(tile);
    var img = document.getElementById('tileImage');
    var sy = tile[0]*tileSize;
    var sx = tile[1]*tileSize;
    var swidth = tileSize;
    var sheight = tileSize;
    //console.log(sx,sy,swidth,sheight,j*tileSize,i*tileSize,tileSize,tileSize);
    ctx.drawImage(img,sx,sy,swidth,sheight,j*tileSize,(mapaTilesAltura*tileSize)- i*tileSize-tileSize,tileSize,tileSize);
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#tileImage')
                .attr('src', e.target.result)
        };

        reader.readAsDataURL(input.files[0]);
        console.log(input.files[0]);
       mapName = input.files[0].name;
    }
}

function desenhaTileset(){
    var tilesetCanvas = document.getElementById('tileset');
    var image = document.getElementById('tileImage');

    
    if(document.getElementById('tileImage').src != null){
        tilesetCanvas.width = image.width;
        tilesetCanvas.height = image.height;
        var ctx = tilesetCanvas.getContext('2d');
        ctx.drawImage(image,0,0);

        if(tileSize > 0 && (tileSize%2==0)){

        
            ctx.beginPath();
            ctx.strokeStyle = "black";
            
            for(var i = 0; i <numTileY; i++){
                ctx.moveTo(0,i *tileSize);
                ctx.lineTo(image.width, i *tileSize);
                
            }
           for(var j = 0; j < numTileX; j++){
                ctx.moveTo(j * tileSize, 0);
                ctx.lineTo(j * tileSize, image.height);
            }
            ctx.stroke();
            ctx.beginPath();
            //tile selecionado.
            ctx.strokeStyle = "white";
            ctx.moveTo(selectedTile[1]*tileSize, selectedTile[0] *tileSize);
            ctx.rect(selectedTile[1]*tileSize, selectedTile[0] *tileSize, tileSize, tileSize);

            ctx.stroke();
        }
    }
}

function desenhaTudo(){
    desenhaTileset();
    desenhaMapa();

}

function toJSON(){
    var textArea = document.getElementById('jsonData');
    var r = Object();
    r.tileFile = mapName;
    r.tileSize = tileSize;
    r.width = mapaTilesLargura;
    r.height = mapaTilesAltura;
    r.windowWidth = windowWidth;
    r.windowHeight = windowHeight;
    var map_str = new Array(mapaTilesAltura);
    for(var i =0; i < mapaTilesAltura; i++){
        map_str [i] = new Array(mapaTilesLargura);
        for (var j = 0; j < mapaTilesLargura; j++){
            if(mapa[i][j] == null){
                map_str[i][j] = "";
            }
            else{
                map_str[i][j] = tileName(mapa[i][j]);
            }
        }
    }
    r.mapCels = map_str;
    textArea.innerHTML  = JSON.stringify(r);
    save("map.json",JSON.stringify(r));
}

function save(filename, data) {
    var blob = new Blob([data], {type: 'text/csv'});
    if(window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveBlob(blob, filename);
    }
    else{
        var elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob);
        elem.download = filename;        
        document.body.appendChild(elem);
        elem.click();        
        document.body.removeChild(elem);
    }
}

function selectTile(evt){
    var x = evt.offsetX, y = evt.offsetY;
    var image = document.getElementById('tileImage');
    
    selectedTile = [Math.floor(y/tileSize), Math.floor(x / tileSize) ];
    console.log("sel tile? " + selectedTile +" " + tileName(selectedTile));
}
function geraTileset(){
    if(document.getElementById('tileImage').src == null){
        alert("Selecione a imagem...");
        return;
    }
    tileSize = document.getElementById('tileSize').value;

    if(tileSize <=0){
        alert("Tamanho do tile pequeno demais...");
        return;
    }
    if(tileSize%2!=0){
        alert("o TIle deve ser múltiplo de 2 (16, 32, 64, ...");
        return;
    }
    var image = document.getElementById('tileImage');

    numTileX = image.width / tileSize;
    numTileY = image.height / tileSize;
}