import matplotlib.pyplot as plot
import json

with open("Class.json", "r") as file:
    school_class = json.load(file)
    
    hight_level = 0
    middle_level = 0
    low_level = 0
    
    for pupil in school_class["Class"]:
        if pupil["Evaluations"] == "Відмінник":
            hight_level += 1
        elif pupil["Evaluations"] == "Хорошист":
            middle_level += 1
        elif pupil["Evaluations"] == "Двієчник":
            low_level += 1
            
    pupil_count = len(school_class["Class"])
    
plot.title("Рівень оцінок у класі")
plot.pie([hight_level, middle_level, low_level], labels = ["Відмінник", "Хорошист", "Двієчник"], colors = ["darkblue", "blue", "lightblue"], autopct="%1.1f%%")

plot.show()
