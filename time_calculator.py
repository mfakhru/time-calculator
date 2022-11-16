def add_time(start, duration, day=None):
  if duration == '0:00':
    new_time = start
    return new_time
    
  week_days = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday"]
  
  new_time = ''
  later = ''
  num_days = int()
  newstart = start[:-2]
  pp = start[-2:]

  _start = newstart.split(':')
  _dur = duration.split(':')

  hh = int(_start[0]) + int(_dur[0])
  mm = int(_start[1]) + int(_dur[1])

  if mm > 60:
      new_mm = mm % 60
      mm = str(new_mm).zfill(2)
      hh += 1
  
  if hh >= 12:
      num_hh = int(round((hh / 12), 0))
      num_days = int(round((num_hh / 2), 0))
      if pp == 'AM' and num_days != 1: 
          pp = 'PM'
      else: 
          pp = 'AM'
          later = f'({num_days} days later)'
          if num_days == 0 or num_days == 1:
              later = '(next day)'
      hh = hh % 12
      if hh == 0:
          hh = 12

  if day != None:
      idx = week_days.index(day.lower())
      idx_day = (idx + num_days) % 7
      day = week_days[idx_day].title()
      if pp == 'AM':
        new_time = f'{hh}:{mm} {pp}, {day} {later}'
      else:
        new_time = f'{hh}:{mm} {pp}, {day}'
  else: 
      if pp == 'AM':
        new_time = f'{hh}:{mm} {pp} {later}'
      else:
        new_time = f'{hh}:{mm} {pp}'
  
  return new_time
