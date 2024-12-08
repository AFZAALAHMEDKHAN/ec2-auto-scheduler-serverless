# Serverless EC2 Instance Scheduler
![Screenshot (124)](https://github.com/user-attachments/assets/e2f2d519-417f-403d-a4f4-0e9758a04d14)
# Scenario:
In some companies, there is no need to run their EC2 instances 24/7; they require instances to operate during specific time periods, such as company working hours, from 8:00 AM in the morning to 5:00 PM in the evening. To address this scenario, I will implement two Lambda functions responsible for starting and stopping instances. These Lambda functions will be triggered by two CloudWatch Events in the morning and evening. This solution is fully serverless.
