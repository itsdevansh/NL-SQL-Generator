import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Import necessary modules from the api package
from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
# The engine used is "text-babbage-001" with a temperature of 0.5 and a maximum number of tokens of 100
gpt = GPT(engine="text-davinci-003", temperature=0.5, max_tokens=100)

# Add examples of English queries and their corresponding SQL queries
gpt.add_example(Example("The following is the database architecture of a college student database:\n\"Students Table:\nstudent_id (Primary Key)\nfirst_name\nlast_name\ndate_of_birth\nemail\nphone\naddress\ncity\nstate\nzip_code\nCourses Table:\ncourse_id (Primary Key)\ncourse_name\ncourse_description\ncourse_credit\nEnrollments Table:\nenrollment_id (Primary Key)\nstudent_id (Foreign Key)\ncourse_id (Foreign Key)\nenrollment_date\nenrollment_status (e.g., enrolled, dropped, completed)\nInstructors Table:\ninstructor_id (Primary Key)\nfirst_name\nlast_name\nemail\nphone\nAssignments Table:\nassignment_id (Primary Key)\ncourse_id (Foreign Key)\ninstructor_id (Foreign Key)\nassignment_name\nassignment_description\nassignment_due_date\nGrades Table:\ngrade_id (Primary Key)\nstudent_id (Foreign Key)\nassignment_id (Foreign Key)\ngrade\ngrade_date\nDepartments Table:\ndepartment_id (Primary Key)\ndepartment_name\ndepartment_description\nMajors Table:\nmajor_id (Primary Key)\nmajor_name\nmajor_description\ndepartment_id (Foreign Key)\nStudent_Major Table:\nstudent_major_id (Primary Key)\nstudent_id (Foreign Key)\nmajor_id (Foreign Key)\nstart_date\nend_date\nStudent_Attendance Table:\nattendance_id (Primary Key)\nstudent_id (Foreign Key)\ncourse_id (Foreign Key)\nattendance_date\nattendance_status (e.g., present, absent, tardy)\n\"\n","Based on the above database architecture Convert the following English Question into an SQL query:"))
# gpt.add_example(Example("Count the number of players in the league with a height greater than 6 feet", "SELECT COUNT(*) FROM players WHERE height > 6"))
# gpt.add_example(Example("Retrieve the names and points per game of the top 5 scoring players", "SELECT name, points_per_game FROM players ORDER BY points_per_game DESC LIMIT 5"))
# gpt.add_example(Example("Find the average points per game for players on the Golden State Warriors", "SELECT AVG(points_per_game) FROM players WHERE team = 'Golden State Warriors'"))
# gpt.add_example(Example("Select the name and team of all players born in the state of California", "SELECT name, team FROM players WHERE birth_state = 'California'"))
# gpt.add_example(Example("Retrieve the total rebounds for all players in the league", "SELECT SUM(rebounds) FROM players"))

# Define UI configuration for the web app
config = UIConfig(
    description="English to SQL Query",
    button_text="Generate Query",
    placeholder=" ",
    show_example_form=False,
)

# Run the demo web app with the defined GPT object and UI configuration
demo_web_app(gpt, config)



#Reason for Priming the model
# The text-babbage-001 model is a pre-trained model that can generate SQL queries from natural language text. However, it is not specifically trained on the task of converting English statements to SQL queries. Therefore, by providing examples of English statements and their corresponding SQL queries, the model can learn the patterns and relationships between the two. This allows the model to generate more accurate and relevant SQL queries when given new English statements. Additionally, providing examples allows the model to fine-tune its understanding of the task and the specific dataset, so it can generate more accurate results.



# In the above code, the temperature parameter is used to control the randomness or "creativity" of the model's generated output. A lower temperature will result in more conservative or "conservative" output, while a higher temperature will result in more creative or "risky" output.

# In the code, a temperature of 0.5 is used. This setting is typically considered a balance between creativity and conservatism, as it allows the model to generate some variations in its output while still staying close to the examples provided. This setting is particularly useful when working with a pre-trained model, as it allows the model to generate output that is similar to the examples while still being unique.

# In general, the temperature parameter can be adjusted to suit the specific requirements of the task and dataset. A higher temperature may be useful when the model needs to generate more creative or varied output, while a lower temperature may be more appropriate for tasks that require more conservative or accurate output.