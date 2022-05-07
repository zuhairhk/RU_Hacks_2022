# **Digitized Daniel**
## A multipurpose Discord Bot

Using primarily the *nextcord* API as well as others for the various features, the *Digitized Daniel* bot can do it all. Below is a brief rundown of each feature:

## **Light Controller**

With the help of the *TuyaIoT* API, any smart device can be controlled over Discord with Digitized Daniel using *slash commands*.
```
/light
``` 
Is used to change the state of the bulb (ON/OFF)
```
/colour_set
```
Is used to set the colour of the bulb, colours available are red, orange, yellow, green, cyan, blue, and pink
```
/mode
```
Is used to toggle between different modes for the light which change the lights frequency and behaviour accordingly. Avaiable modes are white, colour, scene, and music. 

*White*: Pure white light, similar to natural daylight

*Colour*: Various colours available 

*Scene*: Allows the user to create conditions that control the bulb, such as external brightness 

*Music*: Changes colour to synchronize with music playing

## **Search Function**
With Digitized Daniel, Google searches are possible right in Discord!
```
/search
```
Is used to call the function, followed by whatever you'd like to search. Digitized Daniel will return the first result from Google. 
<<<<<<< HEAD

## **Pomodoro Timer**
Having trouble focusing when you're trying to study? The *Pomodoro Technique* is a method of staying focused by working for an interval of time, then taking a break for a smaller interval, and repeating this process. This increases productivity and prevents burnout.

 Digitized Daniel has a function to set a timer and keep track of how much time has elapsed, through Discord. 
 ```
 $start x y
 ```
 Is the command to start a Pomodoro timer, where *x* is the study time interval and *y* is the break time interval.
 ```
 $time
 ```
 Displays how much time is left in the current study/break interval.