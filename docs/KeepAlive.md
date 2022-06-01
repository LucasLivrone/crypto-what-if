### Keep Alive

Heroku enables AutoIdle in order to put non-critical apps to sleep after 30 minutes of inactivity.    
The app will be reactivated once it receives an HTTP request.   
With the free plan this cannot be disabled. However, there is a way to keep the service alive and avoid downtimes.

#### Cron-job.org
Cron-Job.org is a free webapp that let you schedule an HTTP request.    
It is highly customizable but in order to keep crypto-what-if tool the normal settings and scheduling a request every 15 minutes is enough to avoid AutoIdle.   