All of these files are the assignments that I completed while in SENG 265 at UVic.

a1 & a2:
These are coded in C, a2 works off of a1. The problem we had to solve was reading survay answers from a .txt file and sorting and printing out the data in to the terminal in a format that is easier for the end user to understand and read. 

a3, a4, & a5:
These are coded in Python and work off eachother. 
a3 is the back end of a database that keeps a list of patients and each patient has a list of notes that can only be accessed by that patent.
a4 builds off of it and makes it more effecent and able to save patents even when the code is turned off. This is able to be done using DATO and Pickle to incript the files. The DATO files has all the patients information then each patient has a key that corisponds with a P{ickle file witch holds the patient notes. When the Controller is login all the files are read and added to internal lists that only the controller is able to access and change. 
a5 builds off of a4 and adds a rudimentory UI. You are able to:
- Login
- Search patient
- Create patient
- Update patient
- Delete patient
- List all patients is data base
- Retrive list of patients with same name searched with
- Add notes to patients
- Update notes
- Delete notes  
