date_str = '2009-06-15'

date_list = date_str.split('-')
date_list.reverse()
date_str_f = '/'.join(date_list)
print(date_str_f)
