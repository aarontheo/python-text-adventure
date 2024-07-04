# CSE 310 - Module Report

Name: Aaron Theobald

## Part 1 - Module Planning

This section should be filled on the first Monday of the Sprint and submitted

### Section 1.1 - Module Selection

1. What Sprint is this for (1-5)?
5

2. Select the Module (with a single X) that you will do this Sprint:

| Module                    | Selected Module |
| ------------------------- | --------------- |
| Cloud Databases           |                 |
| Data Analysis             |                 |
| Game Framework            |                 |
| GIS Mapping               |                 |
| Mobile App                |                 |
| Networking                |                 |
| SQL Relational Databases  |                 |
| Web Apps                  |                 |
| C++                       |                 |
| Java                      |                 |
| Kotlin                    |                 |
| Erlang                    | X               |
| TypeScript                |                 |
| Rust                      |                 |
| Choose Your Own Adventure | X               |

3. Find the list of unique requirements for your selected module in the Module Summary in Canvas.  In some circumstances, you will need to modify the requirements based on the technology or language you selected.  For the Choose Your Own Adventure, you need to create your own requirements.  List the unique module requirements below:

1. Have a working client and server which can connect to each other and exchange information.
2. Client is able to get user input and send it to the server for parsing
3. Server is able to parse user command strings.
4. Server has child processes representing rooms and objects and can send descriptions to client in response to commands.

### Section 1.2 - Planning

During the Sprint, you will spend 4 hours in class meetings, 4 hours on your team project (2 of which during class), and 10 hours on your selected module.  Make a plan for your 10 hours by answering the questions below.  You should refer back to this plan and make adjustments during the Sprint.

1. What sources have you selected to learn the technical material?
I'm going to use ChatGPT and whatever I can find online about text-based games like zork.

2. What is your plan to practice the new material?  In other words, what is the order in which you plan to learn the material before working on your demonstration software?
- I will learn first how to connect my client to my server using a port and local IP address.
- Then, I will implement a server that allows arbitrary functions to be executed on various state machines. That way, I cna implement custom logic for different rooms and objects.

3. What demonstration software do you plan on submitting at the end of the Sprint (note that this can and may change)?
A basic demo of a text-based game.

1. Identify the days, times, and locations that you will work on the module.
Each day, between my two classes on each.

1. Identify both a technical risk and a behavioral risk that you anticipate may occur during this Sprint.  What is your mitigation plan?
I run the risk of overcomplicating my project.
I will keep it incredibly simple, use my existing design document, and focus on getting a working prototype.


## Part 2 - Time Log

This section should be filled out during the Sprint. 

Record all CSE 310 work that you do on your individual module or the team project.  Include time learning, practicing, developing, testing, and documenting.  Don't include time spent in the 4 class meetings (Planning, Stand-Up, Team Review, and Individual Review).  You will need to sum of these hours at the end of the Sprint. Note that the hours you report will affect your grades.

Note that `IM` stands for Individual Module and `TP` stands for Team Project.  

| Date   | Start Time | IM or TP | Description                                                                                                                        | Hours:Minutes |
| ------ | ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Jun 24 | 10:15      | IM       | Worked on the client and server connecting                                                                                         | 1:00          |
| Jun 24 | 12:30      | IM       | Got client/server nodes to connect, message passed from client node to server.                                                     | 0:30          |
| Jun 25 | 10:00      | IM       | Successfully made a start.sh script for the server, which configures everything and runs the start_link function.                  | 0:45          |
| Jun 28 | 10:30      | IM       | Started a new project directory in Python, I've decided to move to that language for now.                                          | 0:15          |
| Jun 29 | 12:00      | IM       | Started learning the curses library so I can make a text interface for my text game                                                | 1:00          |
| Jun 29 | 5:30       | IM       | Spent some time making classes for easier interaction with terminal windows from the curses library                                | 1:00          |
| Jul 2  | 3:30       | IM       | Worked on the parser functions                                                                                                     | 0:30          |
| Jul 3  | 12:40      | IM       | Started on classes, like Registry, Room, and Thing.                                                                                | 0:30          |
| Jul 3  | 8:00       | IM       | Researched the way that Python classes are assembled, started working towards a trait system as opposed to inheritance.            | 2:30          |
| Jul 4  | 9:30       | IM       | Continued research, implemented a system that lets me define 'trait' classes with custom methods and give them to Thing instances. | 2:00          |
| Jul 4  | 12:00      | IM       | Still working on it, the class trait system is working! I'm trying now to implement required attributes for Traits.                | 1:45          |
|        |            |          |                                                                                                                                    |               |

_Note: Add more rows as needed._


## Part 3 - Module Results

This section should be filled out at the end of the Sprint and submitted.

1. Put your GitHub link for your demonstration software here: 

2. Put your YouTube link for your code walkthrough and demo video here:

3. Complete the following checklist by either indicating "Yes" or "No". If you indicate "No" then provide an explanation of why beneath the table.

| Question                                                     | Response |
| ------------------------------------------------------------ | -------- |
| Are the links above public and working?                      |          |
| Did you complete all the unique requirements for the module? |          |
| Did you write at least 100 lines of code?                    |          |
| Did you fully complete the readme.md file?                   |          |
| Did you put the readme.md file in GitHub in the top folder?  |          |

4. If you completed a Stretch Challenge (as shown in the Module Description document in Canvas) then describe what you did.  If you did the Choose Your Own Adventure module, then you get to decide what qualifies as a Stretch Challenge.

5. Did you change your selected module during the middle of the Sprint?  If yes, then describe what you changed it to, when you changed it, and why you changed it.

6. Using the log above, fill in the total hours and minutes you spent on the individual module:

| Activity          | Total Hours:Minutes |
| ----------------- | ------------------- |
| Individual Module |                     |

7. What strategies (behavioral and technical) worked well during this Sprint?  What did not work well?  List some possible ways that you can improve next Sprint.

