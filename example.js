//No third party modules needed
const https = require("https");
//URL for Seattle city information
const url =
  "https://maps.googleapis.com/maps/api/geocode/json?address=Seattle";
//Get request
https.get(url, res => {
  res.setEncoding("utf8");
  body = "";
  res.on("data", data => {
    body += data;
  });
  res.on("end", () => {
    //Parse through json nad places into array
    body = JSON.parse(body);
    console.log(
      `City: ${body.results[0].formatted_address} -`,
      `Latitude: ${body.results[0].geometry.location.lat} -`,
      `Longitude: ${body.results[0].geometry.location.lng}`
    );
  });
});