## iothon2019

IoThon 2019 was a 5G and IoT based hackathon where we innovated with Europe's top university-based 5G testing and experimental network. IoThon 2019, second in IoThon series was organized by the department of Communications and Networking (COMNET), School of Electrical Engineering, Aalto University along with Partners (Ericsson, Nokia, Telia, Siemens and RIOT) and several European universities (Athens University of Economics and Business, FU Berlin, Hamburg University of Applied Sciences and University of Basel). 

**[IoThon 2019](https://iothon.io/)**, Europe's second research-oriented open source IoT hackathon, took place in May 3-5, 2019 at Open Innovation House, Maarintie 6, 02150, Espoo, Finland.

![Iothon](images/iothon.png)

## Our solution
We participated in the Ericsson's challenge: Futuristic Aalto Campus, which consisted in address a range of critical environmental issues using cellular IoT and connected technologies. 

### Inspiration
We, as human nation, are always so proud of the technologies we develop, but compliant about them as well because they result in excessive energy consumption and waste production. One point we ignore is that, what creates the biggest waste is actually our way of using the technology, we take the resource we have for granted.

In Aalto University campus, you can observe many environment friendly solutions already implemented. However, another thing you can observe is that there are a lot of fully functioning spaces (in terms of electricity, air conditioning etc.) even though there are no one using or very little amount of people using.

Our idea is to reduce this kind of indefferent way of usage of facilities. The main point is, the functioning areas can be activated or deactivated dynamically in accordance with the number of people in the campus at that time.

### What it does
Basically, this is an application that aims to limit usage of some certain areas due to the crowd. For example, think that there are 100 people that uses the campus now and for 100 people all the buildings should not be operating at the same time. The application receives data from Arduino sensors by using MQTT protocol and based on the current status the system will determine an efficient way to load balancing the users among the rooms with the ultimate objective to lock rooms if there are no users in there. Furthermore, the system stores the information sent by the sensors into an SQLite database for further analysis and prediction using Machine Learning algorithms for instance.

### How we built it
We built the application by adapting the MQTT sketch on arduino device to connect by NB-IoT interface to the 5G Comnet core Network. After that we set up an ipip tunnel with a VM that provides public İP connectivity, this step was needed because within the Comnet 5G core there are only private İPs provisioned. Then, the arduino device sends the corresponding data throught MQTT by subscribing a topic to the MQTT broker running on our VM. After that, we create a python application that runs in a separate server on the internet (for instance it could be a cloud server) and the applications reads the data from the arduino device processing it and making decisions in real time notifying the users about the current status of the rooms. Since we did not have real-time data from sensors, we used mock data that is read from csv files. Finally, the data is saved into an SQL database.

![Architecture](images/architecture.png)

### Challenges we ran into
We had problems with 5G network regıstration using Telia SIM cards and making the arduino device working properly.

### Accomplishments that we're proud of
We are proud of our team work and the fact that we were able to develop a complete well functioning İoT application running entirely on 5G network.

### What we learned
We learnt how the 5G works in more detail, specially the NB-İoT air interface and the core network.

### What's next for Utilizing human impact on resource management
Our solution can be scaled to all the areas on campus considering more sensing data and parameters. Moreover, our vision is to be also extended not only for campus but also for smart cities.

Built with:
Python, Arduino, 5G, C
