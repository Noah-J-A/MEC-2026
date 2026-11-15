def add_task(name, category, importance, health_effects, duration):
def add_task(name,category,importance,health_effects,duration):
    file = file.open("tasks.json", "a")
    file = open("tasks.json", "a")
    task = {
        "name": name,
        "category": category,
        "importance": importance,
        "health_effects": health_effects,
        "duration": duration
    }
    file.append(str(task) + "\n")
    file.close()
    
#add_task("labratory","research",8,"none",120)

## for health
# bloodpressure = [low-end, high-end] mm Hg
# bone desnsity = max bone decay rate T-score difference per month. average of 1%-1.5% bone density per month
# heart rate = [low-end resting heart rate, high-end resting heart rate] (Maybe alter if astronaught is sleeping)
# body temp =  average 36.5°C to 38.5°C
# weight = rate of weight gain or loss that warrents a doctors visit or check in 

# sleep = average amount varies per person

