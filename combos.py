# total_ad=ad_from_items + ad_from_runes + ad_per_level + base_ad
# bonus_ad=ad_from_items + ad_from_runes
# ad_from_items=raw_input
# ad_from_runes=raw_input
# base_ad=54.06
# level=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
# ad_per_level=2.83 * level
# skill=(1,2,3,4,5)
# E=0

TOTAL_AD = 10
BONUS_AD = 5

Q_LEVEL = 1
W_LEVEL = 1
E_LEVEL = 1

def is_ult_active():
  return True

def move_q(q_level, bonus_ad, total_ad):
  if q_level == 1:
    if is_ult_active():
      return 30 + 0.45 * total_ad * 0.2 * bonus_ad
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
  print(move_q(1, 10, 10))
  print('Move W at level 1 with 10 total AD and 10 bonus AD:')
  print(move_w(1, 10, 10))
  print('Move R at level 1 with 10 bonus AD:')
  print(move_r(1, 10))
