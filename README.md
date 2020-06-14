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
![Project Fireopolis Architecture](https://github.com/flemingsiow/4everTech-Fireopolis_SCDFXIBM/blob/master/Project%20Fireopolis%20Architecture.jpg "Project Fireopolis Architecture")

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
![Project Fireopolis Roadmap](https://github.com/flemingsiow/4everTech-Fireopolis_SCDFXIBM/blob/master/Project%20Fireopolis%20Roadmap.jpeg "Project Fireopolis Roadmap")

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
1. Visit [Anaconda.com/downloads](https://www.anaconda.com/products/individual)
2. Select your OS Device
3. Download the .exe installer
4. Open and run the .exe installer

### Installing
Now you are ready to run the Python Flask Server. 

1. Open the Anaconda Prompt (Anaconda3)
2. Command Directory (cd) to where server.py is located
3. Type "python server.py" into the prompt. If successful, you should end up with something like this: 

```python
* Serving Flask app "server" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Restarting with windowsapi reloader
* Debugger is active!
* Debugger PIN: 207-535-095
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
## Live Demo
[Live Demo](https://www.fireopolis.flemingsiow.com)

## Built With
- [IBM Cloudant](https://cloud.ibm.com/catalog?search=cloudant#search_results) - The MySQL database used
- [IBM Node-RED](https://cloud.ibm.com/catalog?search=nodered#search_results) - The compute platform for handing logic
- [IBM Watson Machine Learning](https://cloud.ibm.com/catalog?search=Machine%20Learning#search_results) - To analyse the logic
- [IBM Watson Text-to-Speech](https://cloud.ibm.com/catalog?search=Text%20to%20Speech#search_results) - To convert the data into audio
- [IBM Internet of Things Platform](https://cloud.ibm.com/catalog?search=Internet%20of%20Things%20Platform#search_results)
- [Python Flask](https://flask.palletsprojects.com/en/1.1.x/) - The Webserver Dashboard
- [Twilio](https://www.twilio.com) - Communication Service

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Authors
- Fleming Siow - Initial work - []

## License
This project is licensed under the Apache 2 License - see the LICENSE file for details

## Acknowledgements
- Based on Billie Thompson's README template.


  




