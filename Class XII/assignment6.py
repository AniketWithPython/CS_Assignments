import random

questions=[{'question': 'What does CPU stand for?', 'correct_answer': 'Central Processing Unit', 'options': ['Central Processing Unit', 'Central Process Unit', 'Computer Personal Unit', 'Central Processor Unit']}, {'question': 'When Gmail first launched, how much storage did it provide for your email?', 'correct_answer': '1GB', 'options': ['1GB', '512MB', '5GB', 'Unlimited']}, {'question': 'The programming language Swift was created to replace what other programming language?', 'correct_answer': 'Objective-C', 'options': ['Objective-C', 'C#', 'Ruby', 'C++']}, {'question': 'HTML is what type of language?', 'correct_answer': 'Markup Language', 'options': ['Markup Language', 'Macro Language', 'Programming Language', 'Scripting Language']}, {'question': 'What amount of bits commonly equals one byte?', 'correct_answer': '8', 'options': ['8', '1', '2', '64']}, {'question': 'In the programming language Java, which of these keywords would you put on a variable to make sure it doesn&#039;t get modified?', 'correct_answer': 'Final', 'options': ['Final', 'Static', 'Private', 'Public']}, {'question': 'If you were to code software in this language you&#039;d only be able to type 0&#039;s and 1&#039;s.', 'correct_answer': 'Binary', 'options': ['Binary', 'JavaScript', 'C++', 'Python']}, {'question': 'What does the Prt Sc button do?', 'correct_answer': 'Captures what&#039;s on the screen and copies it to your clipboard', 'options': ['Captures what&#039;s on the screen and copies it to your clipboard', 'Nothing', 'Saves a .png file of what&#039;s on the screen in your screenshots folder in photos', 'Closes all windows']}, {'question': 'What is the most preferred image format used for logos in the Wikimedia database?', 'correct_answer': '.svg', 'options': ['.svg', '.png', '.jpeg', '.gif']}, {'question': 'In web design, what does CSS stand for?', 'correct_answer': 'Cascading Style Sheet', 'options': ['Cascading Style Sheet', 'Counter Strike: Source', 'Corrective Style Sheet', 'Computer Style Sheet']}, {'question': 'What is the code name for the mobile operating system Android 7.0?', 'correct_answer': 'Nougat', 'options': ['Nougat', 'Ice Cream Sandwich', 'Jelly Bean', 'Marshmallow']}, {'question': 'On Twitter, what was the original character limit for a Tweet?', 'correct_answer': '140', 'options': ['140', '120', '160', '100']}, {'question': 'In Hexadecimal, what color would be displayed from the color code? #00FF00?', 'correct_answer': 'Green', 'options': ['Green', 'Red', 'Blue', 'Yellow']}, {'question': 'What does LTS stand for in the software market?', 'correct_answer': 'Long Term Support', 'options': ['Long Term Support', 'Long Taco Service', 'Ludicrous Transfer Speed', 'Ludicrous Turbo Speed']}, {'question': 'The numbering system with a radix of 16 is more commonly referred to as ', 'correct_answer': 'Hexidecimal', 'options': ['Hexidecimal', 'Binary', 'Duodecimal', 'Octal']}, {'question': 'Which programming language shares its name with an island in Indonesia?', 'correct_answer': 'Java', 'options': ['Java', 'Python', 'C', 'Jakarta']}, {'question': 'How long is an IPv6 address?', 'correct_answer': '128 bits', 'options': ['128 bits', '32 bits', '64 bits', '128 bytes']}, {'question': 'In computing, what does MIDI stand for?', 'correct_answer': 'Musical Instrument Digital Interface', 'options': ['Musical Instrument Digital Interface', 'Musical Interface of Digital Instruments', 'Modular Interface of Digital Instruments', 'Musical Instrument Data Interface']}, {'question': 'In computing, what does LAN stand for?', 'correct_answer': 'Local Area Network', 'options': ['Local Area Network', 'Long Antenna Node', 'Light Access Node', 'Land Address Navigation']}, {'question': 'What language does Node.js use?', 'correct_answer': 'JavaScript', 'options': ['JavaScript', 'Java', 'Java Source', 'Joomla Source Code']}]


maps={"A":0,"B":1,"C":2,"D":3}

def main():
    norepeat=[]
    score=0
    for i in range(4):
        while True:
            n=random.randrange(20)
            if n in norepeat:
                continue
            else:
                norepeat.append(n)
                break
        qs=questions[n]
        print(qs["question"])
        ops=qs["options"]
        random.shuffle(ops)

        print("A)",ops[0],"B)",ops[1],"C)",ops[2],"D)",ops[3])
        while True:
            resp=input("Enter response (A/B/C/D): ")
            if resp not in "AaBbCcDd":
                print("Invalid response")
            else:
                break
        if ops[maps[resp.upper()]]==qs['correct_answer']:
            score+=1

    print(f"\nYour final score is {score}/4")

while True:
    main()
    yn=input("\nDo you want to continue?(Y/N): ")
    if yn in 'Nn':
        break
