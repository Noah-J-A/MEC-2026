def add_task(name, category, importance, health_effects, duration):
    file = file.open("tasks.json", "a")
    task = {
        "name": name,
        "category": category,
        "importance": importance,
        "health_effects": health_effects,
        "duration": duration
    }
    file.append(str(task) + "\n")
    file.close()
    






