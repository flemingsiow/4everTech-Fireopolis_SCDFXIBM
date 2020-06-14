# 4everTech-Fireopolis_SCDFXIBM
We are a group of students who wishes to tap on IoT automatic and remoteless capabilities to save lives in a disaster

## Contents
  1.  [Short Description](#short-description)
  2.  [Demo Video][#demo-video]
  3.  [The Architecture][#the-architecture]
  4.  [Long Description][#long-description]
  5.  [Project Roadmap][#project-roadmap]
  6.  [Getting Started][#getting-started]
  7.  [Running the Tests][#running-the-tests]
  8.  [Live Demo][#live-demo]
  9.  [Built With][#built-with]
  10. [Contributing][#contributing]
  11. [Versioning][#versioning]
  12. [Authors][#authors]
  13. [License][#license]
  14. [Acknowledgments][#acknowledgments]
  
## Short Description
### What's the problem?
### How can technology help?
### The idea

## Demo Video

## The Architecture 
![Product Fireopolis Architecture](https://github.com/flemingsiow/4everTech-Fireopolis_SCDFXIBM/blob/master/Product%20Fireopolis%20Architecture.png "Product Fireopolis Architecture")

  1. Equipment attached to a Raspberry Pi GPIO collect essential data on the condition of the surroundings.
  2. Local Node-RED circuit will format the data before sending it to the IBM IoT server.
  3. Once all the metrics are ready, the data will be analysed in IBM Node-RED within IBM Cloud.
  4. The IBM Node-RED is in charge of facilitating these 4 functions:
      * Store the data as an object in the IBM Cloudant Database for quick access to all the data.
      * Display the data as charts and graphics to be sent to our Front End Python Flask servers.
      * Connect to a IBM Watson Machine Learning Algorithm and formulate the severity of the incident. 
      * IBM Watson Text to Speech service converts data into audio to the Twilio service (Optional) and output through microphones. 
  5. Users can communicate to the IBM Node-RED circuit through our Front End servers to perform remote tasks. 
  
  ## Long Description
  
  ## Project Roadmap
  
  




