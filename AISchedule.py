import schedule
import time
import notify2
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime

# Initialize notify2
notify2.init("Schedule Organizer")

# Training data
X_train = [[8], [10], [12], [18], [20]]
y_train = [
    "Wake up and go for a jog",
    "Complete math homework",
    "Lunch break",
    "Go for a run",
    "Dinner time"
]

# Train the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Function to send notification
def send_notification(task):
    notification = notify2.Notification("Task Reminder", task)
    notification.show()

# Function to add task to the schedule
def add_task(task, time):
    schedule.every().day.at(time).do(send_notification, task)

# Function to predict the next task
def predict_task():
    current_hour = datetime.now().hour
    next_task = clf.predict([[current_hour]])[0]
    print("Next task:", next_task)
    return next_task

# Main function
def main():
    # Add your tasks here
    add_task("Wake up and go for a jog", "8:00")
    add_task("Complete math homework", "10:00")
    add_task("Lunch break", "12:00")
    add_task("Go for a run", "18:00")
    add_task("Dinner time", "20:00")
    
    # Run the schedule
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
