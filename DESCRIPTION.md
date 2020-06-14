# Fireopolis

Project Fireopolis aims to hasten the response to fire emergencies using IoT technology. It consists of an architecture that collects, 
and analyses key data to formulate vital information for both the community and responders to take quick action. Clients with devices may
access our Front End Dashboard server below: 

[Fireopolis Website](https://www.fireopolis.flemingsiow.com)

## Data Collection

To formulate a way to determine the intensity and spread of a fire, we will be installing several equipments as a device, which includes DTH11 (temperature and humidity) sensors, MQ-2 (smoke) sensors, as well as Raspberry Pi 8MP Camera Modules onto a Raspberry Pi GPIO. The device will capture data every 10 seconds.

  ### Location of Devices

  To get the most out of the data in a cheap and effective manner, our hardware device will be placed at strategic locations where there’s a higher possibility a fire may start. This includes cooking areas such as the Kitchen or Barbeque Pits. Areas near electronic devices, outlets are also vulnerable to a massive fire outbreak.

  ### Formatting the Data 

  Data and graphics captured by the device needs to be formatted and organised first before sending it to the cloud. Thus, each Raspberry Pi comes installed with a local Node-RED circuit that passes string datasets such as the Temperature, Humidity and Smoke Level into integers and captures and stores photos with the Raspberry Pi Camera enabled. All the data collected per data captured will then be stored as a single Javascript (JS) object and sent to the IBM Watson IoT Platform Server. 
  
## Data Analysis

Once all the data metrics are ready to go, it can then be analysed in detail in IBM’s Node-RED circuit within the cloud to formulate the status and condition of the resident’s homes. Using IoT technology, we hope to allow residents to monitor and track their appliances and home remotely. No doubt, we are the most vulnerable when we’re not aware of the situation around us. Responders such as firefighters too require prior data beforehand so they can plan out the appropriate approach to the incident. 

  ### Storing the Data 
  Non-sensitive data will be stored in IBM's Cloudant database for responders to monitor the situation nationally. This acts as the responder’s first information before an incident has occurred. If the data is found to be exceptionally abnormal, responders may directly call to check on the situation. Furthermore, the data stored here are useful for historic references. If unusual data captured is more frequently recorded over a specific location, this serves as an alert for possible undesired habits that may lead to or has led to fire outbreaks. Such habits should be controlled or avoided to ensure the well-being and safety of citizens. 
  
  ### Sending the Data to Our Front End Servers
  Using Node-RED’s JS function nodes, we are able to split the data into their different types and specific locations. Then, with a Node-RED UI Dashboard node, we converted the data into appropriate charts and graphics for easy visualisation of the data and hosted it on a live data dashboard. Afterwhich, we created a separate Front End Python Flask server. jQuery API was used to connect the applications together such that users are able to view the diagrams on our Front End servers. Our Front End Dashboard consists of a simple, friendly UI and UX design, using BootStrap. Other relevant graphics include a heatmap, purely hardcoded with JS to help users determine possible overly heated areas in an instance. A threshold can be set for individual locations as certain locations tend to vary in temperature, humidity and smoke level.  
  
  ### Formulating the Severity with the Data
  The data will also be sent to a trained machine learning algorithm to evaluate the data and make accurate predictions on how chaotic the incident is. Based on a certain threshold, also taking into account the location, it will gauge how intense is the condition of the place. Along with IBM Watson’s Machine Learning service, we plan to utilise their Visual Recognition service to analyse the scene, and objects like occupants and flammable objects. The final outcome will be the status of the incident, ranging from 1 to 5. If the status is below 2, the number of responders hired to the scene can be lowered and fire fighting equipment is kept to the minimal, this will greatly save emergency resources in the case of a more severe fire outbreak. This information is then collected back in the Node-RED circuit to be distributed to the Cloudant Database as well as our Front End servers. To identify a resident’s personal data dashboard from another, there will be a User Registration and Login System created with PHP and MySQL.

## Request & Response Measures 
Requests are facilitated across our Front End Dashboard Servers. We aim to simplify everyday tasks through remote communication and hence prevent possible fire outbreaks to occur due to these immediate actions taken. 

  ### Informing the Owner
  Our main priority is to reach out to the owner of the sensor that is found to exceed the recommended thresholds set. To achieve that, we will be using IBM Watson’s Text to Speech service as well as the Node-RED twilio node, which allows us to send messages via the Twilio service. If the data captured exceeded the thresholds, information about the status, including the temperature, humidity and smoke level will be sent via SMS to the owner’s phone. And on top of that, an automated call will be made giving a warning that a specific location of their house has unusual conditions, where the user may press “1” to receive more details of the condition. If the owner is logged in onto our Front End Dashboard, they may remotely control any smart IoT device paired with our dashboard. 

  ### Informing Residents
  We also plan to inform residents of the block in the scenario where the fire outbreak has spread significantly. Using Bluetooth services, nearby residents to the sensors that picked up the data on a possible fire will receive a notification on the analysis of the fire from our Node-RED circuit via the Twilio service . On top of that, IBM Watson’s Text to Speech service will convert those analysis into audio wav files and output it on loudspeakers positioned at every level of the residential block. The analysis includes the severity of the fire, the current location of the spread of the fire, and the most effective escape route based on the fire spread. This will reduce anxiety levels and coordinate evacuation measures to minimise casualties. 

  ### Informing the Respondents
  All of this information is also transmitted automatically to SCDF Firefighter responders, even happening alongside the emergency call. Other analysis may include the number of residents still not evacuated from the building. 

## Conclusion

Utilising the abilities of IoT technology, fireopolis can help residents respond quicker during a fire and speed up the process of evacuation. It also acts as early intervention to prevent fire from occurring. This means lesser people would require medical attention and rescuing, and leaves more resources for other emergencies.
