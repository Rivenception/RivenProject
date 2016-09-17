ad_from_runes=input('What is your AD from runes: ')
level=input('What is your level: ')
ad_from_items=input('What is your AD from items: ')
base_ad=54.06
ad_per_level=3 * level
# ad_per_level need to figure out floats.
# skill=(1,2,3,4,5)
# E=0

bonus_ad = ad_from_items + ad_from_runes
total_ad = bonus_ad + ad_per_level + base_ad

print bonus_ad
print total_ad

TOTAL_AD = 10
BONUS_AD = 5

if level == 1:
  q_level = 1
  w_level = 0
  r_level = 0
if level == 2:
  q_level = 1
  w_level = 1
  r_level = 0
if level == 3:
  q_level = 1
  w_level = 1
  r_level = 1
if level == 4:
  q_level = 2
  w_level = 1
  r_level = 1
if level == 5:
  q_level = 3
  w_level = 1
  r_level = 1
if level == 6:
  q_level = 3
  w_level = 1
  r_level = 1
if level == 7:
  q_level = 4
  w_level = 1
  r_level = 1
if level == 8:
  q_level = 5
  w_level = 1
  r_level = 1
if level == 9:
  q_level = 5
  w_level = 1
  r_level = 1
if level == 10:
  q_level = 3
  w_level = 1
  r_level = 1
if level == 11:
  q_level = 3
  w_level = 1
  r_level = 2
if level == 12:
  q_level = 3
  w_level = 1
  r_level = 2
if level == 13:
  q_level = 3
  w_level = 1
  r_level = 2
if level == 14:
  q_level = 3
  w_level = 2
  r_level = 2
if level == 15:
  q_level = 3
  w_level = 3
  r_level = 2
if level == 16:
  q_level = 3
  w_level = 3
  r_level = 3
if level == 17:
  q_level = 3
  w_level = 4
  r_level = 3
if level == 18:
  q_level = 3
  w_level = 5
  r_level = 3

def is_ult_active():
  return False

def move_q(q_level, bonus_ad, total_ad):
  if q_level == 1:
    if is_ult_active():
      return 10 + 0.45 * total_ad * 0.2 * bonus_ad
    else:
      return 10 + 0.4 * total_ad
  if q_level == 2:
    if is_ult_active():
      return 30 + 0.45 * total_ad * 0.2 * bonus_ad
    else:
      return 30 + 0.45 * total_ad
  if q_level == 3:
    if is_ult_active():
      return 50 + .5 * total_ad * 0.2 * bonus_ad
    else:
      return 50 + .5 * total_ad
  if q_level == 4:
    if is_ult_active():
      return 70 + 5.5 * total_ad * 0.2 * bonus_ad
    else:
      return 70 + 5.5 * total_ad
  if q_level == 5:
    if is_ult_active():
      return 90 + 0.6 * total_ad * 0.2 * bonus_ad
    else:
      return 90 + 0.6 * total_ad

def move_w(w_level, bonus_ad, total_ad):
  if w_level == 1:
    if is_ult_active():
      bonus_ad = 1.2 * bonus_ad
      return 50 + 1.0 * bonus_ad
    else:
      return 50 + 1.0 * bonus_ad
  if w_level == 2:
    if is_ult_active():
      bonus_ad = 1.2 * bonus_ad
      return 80 + 1.0 * bonus_ad
    else:
      return 80 + 1.0 * bonus_ad
  if w_level == 3:
    if is_ult_active():
      bonus_ad = 1.2 * bonus_ad
      return 80 + 1.0 * bonus_ad
    else:
      return 110 + 1.0 * bonus_ad
  if w_level == 4:
    if is_ult_active():
      bonus_ad = 1.2 * bonus_ad
      return 140 + 1.0 * bonus_ad
    else:
      return 140 + 1.0 * bonus_ad
  if w_level == 5:
    if is_ult_active():
      bonus_ad = 1.2 * bonus_ad
      return 170 + 1.0 * bonus_ad
    else:
      return 170 + 1.0 * bonus_ad

def move_r(r_level, bonus_ad):
  if r_level == 1:
    return 100 + 0.6 * bonus_ad
  if r_level == 2:
    return 150 + 0.6 * bonus_ad
  if r_level == 3:
    return 200 + 0.6 * bonus_ad

# QW=Q + R
# ERQ=E + R + Q
# ER2WRQ3=E + R + 2 + W + R + Q3
# RQ3=R + Q3
# EWQ=E + W + Q

if __name__ == '__main__':
  print('Move Q at level 1 with 10 total AD and 10 bonus AD:')
  print q_level
  print(move_q(q_level, total_ad, bonus_ad))
  print('Move W at level 1 with 10 total AD and 10 bonus AD:')
  print w_level
  print(move_w(w_level, total_ad, bonus_ad))
  print('Move R at level 1 with 10 bonus AD:')
  print r_level
  print(move_r(r_level, bonus_ad))
