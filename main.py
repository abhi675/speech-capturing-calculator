
import datetime
import pyttsx3
import speech_recognition as sr

print('Initializing calculator')
Master='Abhishek'
# speak function will pronounce the speech
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#Function function will wish you on the initializing of jarvis
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning '+Master) 
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon '+ Master)

    else:
        speak('Good Evening' + Master)
    

#Function will take command from microphone
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        audio=r.listen(source)

    try:
        print('Recognizing..')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print('Say that again please')
        query=None

    return query 

#Main programe starts here

speak('Initializing Calculator...')
wishMe()
speak("how can i help you {}".format(Master))
query=takeCommand()

# logic
def number(str,i,n):
    result=""
    while i<n and str[i].isdigit():
        result+=str[i]
        i+=1

    return (int(result),i)


def solve(ch,number1,number2):
    if ch=='+':
        return number1+number2
    elif ch=='-':
        return number1-number2

    elif ch=='*':
        return number1*number2
    elif ch=='/':
        return number1/number2


def calculator(str):
    st=[]
    ch=[]
    n=len(str)
    i=0
    while i<n:
        if str[i].isdigit():
            temp1=number(str,i,n)
            if len(ch)>0 and (ch[len(ch)-1]=='*' or ch[len(ch)-1]=='/'):
                temp=solve(ch[len(ch)-1],int(st[len(st)-1]),temp1[0])
                st.pop()
                ch.pop()
                st.append(temp)

            else:
                st.append(temp1[0])
            i=temp1[1]

        elif str[i]=='/' or str[i]=='*' or str[i]=='+' or str[i]=='-':
            ch.append(str[i])
            i+=1

    while len(st)>1:
        temp1=st[len(st)-1]
        st.pop()
        temp2=st[len(st)-1]
        st.pop()
        temp3=ch[len(ch)-1]
        ch.pop()
        temp4=solve(temp3,temp2,temp1)
        st.append(temp4)

    print(st[0])
    return st[0]

if query is None:
    speak('{} Please say something to do'.format(Master))

else:
    temp=query.split(" ")
    str=''
    for elm in temp:
        if elm.isdigit():
            str=str+elm

        elif elm=='+' or elm =='-' or elm=='/':
            str=str+elm
        
        elif elm=='x':
            str=str+'*'

    speak(calculator(str))
