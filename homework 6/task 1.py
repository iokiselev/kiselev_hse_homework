from datetime import datetime

the_moscow_times = datetime.strptime("Wednesday, October 2, 2002", "%A, %B %d, %Y")
the_guardian = datetime.strptime("Friday, 11.10.13", "%A, %d.%m.%y")
daily_news = datetime.strptime("Thursday, 18 August 1977", "%A, %d %B %Y")

print("The Moscow Times datetime format:", the_moscow_times)
print("The Guardian datetime format:", the_guardian)
print("Daily News datetime format:", daily_news)
