function callSensorsAPI() {
    try {
        var response = httpGet('/read');
        console.log(response);
    } catch (error) {
        console.error(error);
    }
}

function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
}