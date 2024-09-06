# Health AI Assistant API

An API that analyzes user health data and offers personalized advice using OpenAI's ChatGPT via the OpenAI library, built with Django and Django REST Framework.

## Features

- **Sleep Condition**: Identifies users who have slept less than 6 hours over the past week and provides personalized advice.
- **Steps Condition 1**: Finds users who have reached 10,000 steps today and offers motivational feedback.
- **Steps Condition 2**: Detects users who have walked 50% less this week compared to the previous week and provides guidance.

## Technologies Used

- Python 3.x
- Django
- Django REST Framework
- OpenAI API (ChatGPT)

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system.
- An OpenAI API key. You can obtain one by signing up at [OpenAI](https://beta.openai.com/signup/).

### Installation

1. **Clone the repository**:

    - git clone https://github.com/avinashrajput124/Health-AI-Assistant.git
    - cd backend
    
2. **Create a virtual environment (optional but recommended)**:
    - python -m venv venv
    -  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages**:
    - pip install -r requirements.txt

4. **Configure the OpenAI API key**:
    - touch .env
    - Replace path 'your-openai-api-key' with your actual OPENAI_API_KEY path.

5. **Apply database migrations**:
    - python manage.py migrate

6. **Create a superuser (to access the Django admin interface)**:
    - python manage.py createsuperuser

7. **Populate database with sample data**:
    - Run the management command to populate the database with sample data:
        - python manage.py populate_data

8. **Run the development server**:
    - python manage.py runserver


## API Usage

1. **Endpoints**
    - Sleep Condition: GET /api/sleep-condition/
    - Steps Condition 1: GET /api/steps-condition-1/
    - Steps Condition 2: GET /api/steps-condition-2/

2. **Example Requests**
    - Sleep Condition:
        - GET /api/steps-condition/
        - HTTP 200 OK
        - Allow: GET, HEAD, OPTIONS
        - Content-Type: application/json
        - Vary: Accept
        - URL http://localhost:8000/api/sleep-condition/

    - Steps Condition 1:
        - GET /api/steps-condition-1/
        - HTTP 200 OK
        - Allow: GET, HEAD, OPTIONS
        - Content-Type: application/json
        - Vary: Accept
        - URL http://localhost:8000/api/steps-condition-1/
    
    - Steps Condition 2:
        - GET /api/steps-condition-2/
        - HTTP 200 OK
        - Allow: GET, HEAD, OPTIONS
        - Content-Type: application/json
        - Vary: Accept
        - URL http://localhost:8000/api/steps-condition-2/


3. **Example Response**
    -  Sleep Condition:-
  
      
        [

          {
              "user": "a2f9537e",
              "ai_response": "Hi Mason! It looks like you're skimping on sleep, which can impact your energy and overall well-being. Try setting a bedtime routine to help you wind                     down and aim for at least 7-8 hours of rest each night. Your body will thank you! You've got this! 💤😊"
          },
       
          {
                "user": "f48d5775",
                "ai_response": "Hi Liam! It looks like you’re getting way less sleep than you need. Try to gradually increase your sleep time to at least 7-8 hours. Consider setting a                 bedtime routine, limiting screen time before bed, and creating a cozy sleep environment. You got this—better sleep can really boost your health and energy! 🌙✨"
          },
       
          {
                "user": "5efabf3b",
                "ai_response": "Hey Avinash! 🌟 It looks like you're not getting enough sleep. Try to gradually increase your sleep time to 7-8 hours. Establish a relaxing bedtime                      routine, limit screen time before bed, and create a cozy sleep environment. You got this! Sweet dreams await! 😴✨"
          },
       
          {
                "user": "680dd909",
                "ai_response": "Hi Liam! It looks like you're getting much less sleep than you need. Try to gradually increase your sleep time to around 7-8 hours a night. Establish a                 calming bedtime routine, limit screen time before bed, and create a cozy sleep environment. You got this—better sleep can make a big difference in how you feel!"
          },
       
          {
                "user": "f56f42f2",
                "ai_response": "Hey Olivia! It looks like you're not getting nearly enough sleep. Try to gradually increase your sleep to at least 7-8 hours a night. Maybe start by                     going to bed 15 minutes earlier and see how it feels! Good rest will boost your energy and overall well-being. You've got this! 🌟"
          }
        ]







    - Steps Condition 1:




      [
      {
          "user": "Mason Williams",
          "ai_response": "Hey Mason! Awesome job with 7014 steps today! Just a little push and you might hit 10,000 soon—keep it up! Every step counts towards your health,                       and  you’re doing fantastic. Let’s aim for even more movement tomorrow! 😊"
      },
      
      {
       "user": "Liam Johnson",
        "ai_response": "Liam, awesome job on those 10,922 steps! Keep up the fantastic work—it’s making a big difference for your health. Remember to stay hydrated and                         consider mixing in some strength training this week for well-rounded fitness. You’ve got this! 🌟"
      },

      {
        "user": "Avinash Garcia",
        "ai_response": "Avinash, fantastic job on those 13,892 steps! Keep up the active lifestyle. Maybe aim for a walk in nature tomorrow to mix it up and relax. You've got                  this! 🌟👏"
      },
      
      {
        "user": "Liam Brown",
        "ai_response": "Liam, amazing job on those 14,212 steps! Keep up that fantastic energy—you're doing wonders for your heart and overall well-being. Maybe challenge                      yourself to add a few minutes of strength training or stretching to balance it out. You're on the right track! 🎉"
      },
   
      {
        "user": "Olivia Smith",
        "ai_response": "Olivia, you're doing fantastic with those 12,925 steps! Keep up the great work, and consider mixing in some strength training a couple of times a week                 for overall fitness. You've got this!"
      }
  
      ]






    - Steps Condition 2:
  
        [

        {
                "user": "Mason Williams",
                "ai_response": "Hey Mason! Great job hitting 7014 steps this week—that's an improvement from last week! 🎉 Keep up that momentum and aim to maintain or increase those                     step counts. Consistency is key, and every little bit contributes to your overall health. You've got this! Keep walking! 🚶‍♂️💪"
        },
      
        {
                "user": "Liam Johnson",
                "ai_response": "Hey Liam! Great job getting in over 10,000 steps! Even though you took a tiny dip this week, you're still doing awesome compared to last week. Keep                     aiming for that step goal, and maybe try to add a short walk or two if you can. You've got this! 😊🏃‍♂️"
        },
      
        {
                "user": "Avinash Garcia",
                "ai_response": "Hey Avinash! Great job on keeping up with your steps! Even though you took slightly fewer steps this week, consistency is key. Aim to hit that 14,000                   mark again, and if you can, add a few extra minutes of walking each day. You've got this—keep it up and stay active! 😊"
         },
      
        {
                "user": "Liam Brown",
                "ai_response": "Hey Liam! Great job on hitting 14,212 steps last week! That’s an awesome achievement. While there was a slight dip this week, you're still doing                         fantastic. Keep aiming for those daily walks, and maybe even add a few minutes more each day to boost your steps. You've got this—stay active and keep up the great                     work! 🌟"
        },
      
        {
                "user": "Olivia Smith",
                "ai_response": "Hey Olivia! Great job on hitting 12,925 steps this week! That's an improvement from last week, so keep up the awesome work! To stay consistent, aim for                 a little extra each day—maybe a brisk walk or some dancing? You've got this! 🌟"
        },
   
        ]

## Thanks

Thank you for checking out the Health AI Assistant API! 
