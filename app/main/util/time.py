from datetime import datetime

def between_time(current_datetime, time_start, time_end):
  FMT = '%Y-%m-%d %H:%M:%S'
  now = datetime.now()
  date_now = now.strftime("%Y-%m-%d")
  ts = datetime.strptime(date_now + ' ' + time_start, FMT)
  te = datetime.strptime(date_now + ' ' + time_end, FMT)
  case1 = current_datetime - ts
  case2 = te - current_datetime

  if (case1.days >= 0 and case2.days >= 0):
    return True
  
  return False