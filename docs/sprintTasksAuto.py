# this script should take features from our requirements and automatically output
# a list of tasks for the sprint and then output them as a .md file
# it should also take completed features and add them to the completed features list of that sprint

import re

# read in the requirements file
with open("featuresParagraph.md", "r") as file:
    requirements = file.read()

# split the requirements into a list of features
features = requirements.split("\n")

# create a list to store the tasks for the sprint
sprintTasks = []

# create a list to store the completed features for the sprint
completedFeatures = []

# loop through the features
for feature in features:
    # remove the leading and trailing whitespace
    feature = feature.strip()

    # check if the feature is a task
    if feature.startswith("-"):
        # remove the leading dash
        feature = feature[1:]

        # add the task to the sprint tasks list
        sprintTasks.append(feature)
    else:
        # add the completed feature to the completed features list
        completedFeatures.append(feature)
# create a string to store the sprint tasks
sprintTasksString = ""

# loop through the sprint tasks
for task in sprintTasks:
    # add the task to the sprint tasks string
    sprintTasksString += f"- {task}\n"

# create a string to store the completed features
completedFeaturesString = ""

# loop through the completed features
for feature in completedFeatures:
    # add the completed feature to the completed features string
    completedFeaturesString += f"- {feature}\n"

# create a string to store the sprint tasks and completed features
sprintTasksAndCompletedFeaturesString = sprintTasksString + completedFeaturesString

# write the sprint tasks and completed features to a file
with open("sprintTasks.md", "w") as file:
    file.write(sprintTasksAndCompletedFeaturesString)

